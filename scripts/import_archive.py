"""Importer: grok.me archive -> docs/*.md  (v2, migration-fixes)
Keeps images, KaTeX math (pre-rendered HTML), original heading ids, separated badges,
JSON/Cite links, and the /wiki, /packages, /labs, /notes, /timeline routes."""
import re,json,os,glob,shutil
from bs4 import BeautifulSoup, NavigableString
import inspect,textwrap,markdownify as _mdf
# Python-Markdown needs 4-space list nesting; markdownify indents by bullet width (2-3). Pad bullets to 4.
_src=textwrap.dedent(inspect.getsource(_mdf.MarkdownConverter.convert_li)).replace("bullet = bullet + ' '","bullet = (bullet + ' ').ljust(4)").replace("bullet_indent = ' ' * bullet_width","bullet_indent = ' ' * 4").replace("text = bullet + text[bullet_width:]","text = bullet + text[4:]")
_ns={}; exec(_src,vars(_mdf),_ns)
class _Conv(_mdf.MarkdownConverter): convert_li=_ns['convert_li']
def md(html,**o): return _Conv(**o).convert(html)
A='../source-archive'; ORIG='https://aaronspradlin.grok.me'
corp={}
for r in json.load(open(f'{A}/corpus.json'))['records']:
    if r['href'] not in corp or r['kind']=='wiki': corp[r['href']]=r
FILES=sorted(glob.glob(f'{A}/pages/*.html'))+sorted(glob.glob(f'{A}/extra-pages/*.html'))
def route_of(f):
    r=os.path.basename(f)[:-5].replace('_','/'); return '/' if r=='/index' else r
ROUTES={route_of(f) for f in FILES}
DATA={'/llms.txt','/llms-small.txt','/cantos.txt','/cantos.json','/qa.json','/claims.jsonl','/tools.json','/corpus.json','/cite.txt','/search.json','/favicon.svg'}
def target(p):
    if p in ('/',''): return 'index.md'
    if p in ('/wiki','/packages'): return p[1:]+'/index.md'
    if p in DATA or p.startswith('/llms/') or p.startswith('/artifacts/'): return p[1:]
    if re.search(r'\.\w+$',p): return p[1:]
    return p[1:]+'.md'
def rel(h,dest):
    if h.startswith(ORIG): h=h[len(ORIG):] or '/'
    if not h.startswith('/') or h.startswith('//'): return h
    p,_,frag=h.partition('#'); p,_,q=p.partition('?')
    if p=='/page.json':
        m=re.search(r'slug=([\w-]+)',q); t='data/page/'+m.group(1)+'.json' if m else 'data/corpus.json'
    else:
        p=p.rstrip('/') or '/'
        if not (p in ROUTES or p in DATA or p.startswith('/llms/') or p.startswith('/artifacts/')): return ORIG+h
        t=target(p)
    t=os.path.relpath(t,os.path.dirname(dest[5:]) or '.')
    return t+('#'+frag if frag else '')
def dest_of(route):
    return 'docs/'+target(route)
n=0
for f in FILES:
    route=route_of(f)
    s=BeautifulSoup(open(f,encoding='utf-8',errors='replace').read(),'html.parser')
    m=s.find('article') or s.find('main')
    if not m: continue
    for t in m.find_all('button'):
        if t.find('img') or t.find('video'): t.unwrap()
    for t in m.find_all(['script','style','button','noscript','input','form']): t.decompose()
    for h in m.find_all(['h2','h3','h4']):
        for a in h.find_all('a'):
            if a.get_text(strip=True)=='#': a.decompose()
    for t in m.find_all('svg'):
        if not t.find_parent(class_='katex'): t.decompose()
    dest=dest_of(route)
    for a in m.find_all('a',href=True): a['href']=rel(a['href'],dest)
    # math: keep pre-rendered KaTeX HTML verbatim
    math=[]
    for k in m.select('.katex-display, .katex'):
        if k.find_parent(class_='katex') or k.find_parent(class_='katex-display'): continue
        disp='katex-display' in (k.get('class') or [])
        math.append(('\n\n<div class="ra-math">'+str(k)+'</div>\n\n') if disp else str(k))
        k.replace_with(NavigableString(f'RAMATH{len(math)-1}X'))
    # images
    for i in m.find_all(['img','source','video']):
        for at in ('src','poster'):
            if i.get(at): i[at]=rel(i[at],dest)
    bdir=dest[5:-3] if not dest.endswith('index.md') else os.path.dirname(dest[5:])
    for v in m.find_all('video'):
        v['style']='max-width:100%'
        for i in [v]+v.find_all('source'):
            for at in ('src','poster'):
                if i.get(at) and not i[at].startswith('http'):
                    absp=os.path.normpath(os.path.join(os.path.dirname(dest[5:]),i[at]))
                    i[at]=os.path.relpath(absp,bdir or '.')
        math.append('\n\n'+str(v)+'\n\n'); v.replace_with(NavigableString(f'RAMATH{len(math)-1}X'))
    # badges / meta rows: separate run-together inline items
    for d in m.find_all('div'):
        cls=' '.join(d.get('class') or [])
        kids=[c for c in d.children if getattr(c,'name',None) or str(c).strip()]
        if 'flex' in cls and len(kids)>1 and all(getattr(c,'name',None) in ('span','a') for c in kids):
            for c in kids[1:]: c.insert_before(NavigableString(' · '))
    # block content inside links breaks Markdown links: flatten (headings stay headings, linked)
    for a in m.find_all('a',href=True):
        if a.find('img') or a.find('video'): continue
        h=a.find(['h2','h3','h4','h5'])
        if h:
            rest=' '.join(x.get_text(' ',strip=True) for x in a.find_all(['p','div','span'],recursive=True) if not x.find(['h2','h3','h4','h5']) and x.get_text(strip=True) and x not in h.descendants and not x.find(['p','div','span']))
            nh=s.new_tag(h.name); na=s.new_tag('a',href=a['href']); na.string=h.get_text(' ',strip=True); nh.append(na)
            wrap=s.new_tag('div'); wrap.append(nh)
            if rest: pp=s.new_tag('p'); pp.string=rest; wrap.append(pp)
            a.replace_with(wrap)
        elif a.find(['div','p','span','br']):
            t=' '.join(a.get_text(' ',strip=True).split()); a.clear(); a.string=t
    # escape literal braces (attr_list) and pipes inside table cells
    for tn in m.find_all(string=True):
        if tn.find_parent(['code','pre']) or tn.find_parent(class_='katex'): continue
        t=str(tn)
        if '{' in t or '}' in t or ('|' in t and tn.find_parent(['td','th'])):
            t=t.replace('{','RALBR⟧').replace('}','RARBR⟧')
            if tn.find_parent(['td','th']): t=t.replace('|','RAPIPE⟧')
            tn.replace_with(NavigableString(t))
    # keep original heading ids so in-page links resolve
    for h in m.find_all(['h2','h3','h4']):
        if h.get('id'): h.append(NavigableString(' RAID'+h['id']+'⟧'))
    for e in m.find_all(id=True):
        if e.name in ('h2','h3','h4') or e.find_parent(class_='katex'): continue
        e.insert(0,NavigableString('RAANC'+e['id']+'⟧ '))
    body=md(str(m),heading_style='ATX')
    body=re.sub(r'RAANC(.+?)⟧ ?',lambda x:'<span id="'+x.group(1).replace('\\','')+'"></span>',body)
    body=re.sub(r' RAID(.+?)⟧\s*$',lambda x:' {#'+x.group(1).replace('\\','')+'}',body,flags=re.M)
    body=re.sub(r'RAID(.+?)⟧',lambda x:'',body)
    # blank line before a list item that follows paragraph text (avoid lazy continuation)
    L=body.split('\n'); out=[]; fence=False; LI=re.compile(r'^\s*(\d+\.|[*+-])\s+\S')
    for ln in L:
        if ln.lstrip().startswith('```'): fence=not fence
        if not fence and LI.match(ln) and out and out[-1].strip() and not LI.match(out[-1]): out.append('')
        elif not fence and ln.strip() and not ln[0].isspace() and not LI.match(ln) and out and out[-1].strip() and LI.match(out[-1]): out.append('')
        out.append(ln)
    body='\n'.join(out)
    body=body.replace('RALBR⟧','\\{').replace('RARBR⟧','\\}').replace('RAPIPE⟧','\\|')
    body=re.sub(r'RAMATH(\d+)X',lambda x:math[int(x.group(1))],body)
    body=re.sub(r'\n{3,}','\n\n',body).strip()
    title=(s.title.string if s.title and s.title.string else route).split(' · ')[0].strip()
    desc=s.find('meta',attrs={'name':'description'})
    r=corp.get(route,{})
    fm={'title':title,'route':route,'source':ORIG+(route if route!='/' else '')}
    if desc and desc.get('content'): fm['description']=desc['content']
    for k in('date','claimStatus','tags','dek'):
        if r.get(k): fm[k]=r[k]
    if 'description' not in fm and r.get('dek'): fm['description']=r['dek']
    os.makedirs(os.path.dirname(dest),exist_ok=True)
    with open(dest,'w') as o: o.write('---\n'+''.join(f'{k}: {json.dumps(v,ensure_ascii=False)}\n' for k,v in fm.items())+'---\n\n'+body+'\n')
    n+=1
# data files: original paths, byte-identical (plus legacy data/ copies)
os.makedirs('docs/data/page',exist_ok=True)
for p in ['corpus.json','cantos.json','cantos.txt','qa.json','tools.json','cite.txt','search.json','llms-small.txt','llms.txt','claims.jsonl']:
    shutil.copy(f'{A}/{p}','docs/'+p)
    if p not in ('llms.txt','claims.jsonl'): shutil.copy(f'{A}/{p}','docs/data/'+p)
for p in glob.glob(f'{A}/page-json/*.json'): shutil.copy(p,'docs/data/page/')
shutil.copytree(f'{A}/llms','docs/llms',dirs_exist_ok=True)
shutil.copytree(f'{A}/artifacts','docs/artifacts',dirs_exist_ok=True)
os.makedirs('docs/assets',exist_ok=True)
for p in['og.jpg','favicon.svg']: shutil.copy(f'{A}/{p}','docs/assets/'+p)
shutil.copy(f'{A}/claims.jsonl','claims/ledger.jsonl')
print('pages',n)
