"""One-time importer: grok.me archive -> docs/*.md"""
import re,json,os,glob,shutil
from bs4 import BeautifulSoup
from markdownify import markdownify as md
A='../source-archive'
corp={}
for r in json.load(open(f'{A}/corpus.json'))['records']:
    if r['href'] not in corp or r['kind']=='wiki': corp[r['href']]=r
os.makedirs('docs/wiki',exist_ok=True)
ROUTES=set()
for f in glob.glob(f'{A}/pages/*.html'):
    r=os.path.basename(f)[:-5].replace('_','/'); ROUTES.add('/' if r=='/index' else r)
def target(p):
    if p.startswith('/wiki/'): return 'wiki/'+p[6:]+'.md'
    if p in('/',''): return 'index.md'
    if p.startswith('/llms/'): return p[1:]
    if p in ('/llms.txt','/claims.jsonl'): return p[1:]
    if re.search(r'\.\w+$',p): return 'data/'+p[1:]
    return p[1:]+'.md'
def rel(h,dest):
    if h.startswith('https://aaronspradlin.grok.me'): h=h[len('https://aaronspradlin.grok.me'):] or '/'
    if not h.startswith('/') or h.startswith('//'): return h
    p,_,frag=h.partition('#'); p=p.split('?')[0].rstrip('/') or '/'
    if not (p in ROUTES or p.startswith('/llms') or p=='/labs' or re.search(r'\.\w+$',p)): return 'https://aaronspradlin.grok.me'+h
    t=os.path.relpath(target(p),os.path.dirname(dest[5:]) or '.')
    return t+('#'+frag if frag else '')
n=0;out=[]
for f in sorted(glob.glob(f'{A}/pages/*.html')):
    route=os.path.basename(f)[:-5].replace('_','/')
    route='/' if route=='/index' else route
    s=BeautifulSoup(open(f,encoding='utf-8',errors='replace').read(),'html.parser')
    m=s.find('article') or s.find('main')
    if not m: continue
    for t in m.find_all(['script','style','svg','button','noscript','input','form']): t.decompose()
    if route.startswith('/wiki/'): dest=f'docs/wiki/{route[6:]}.md';d=1
    elif route=='/': dest='docs/index.md';d=0
    else: dest=f'docs/{route[1:]}.md';d=0
    for a in m.find_all('a',href=True): a['href']=rel(a['href'],dest)
    title=(s.title.string or route).split(' · ')[0].strip()
    body=re.sub(r'\n{3,}','\n\n',md(str(m),heading_style='ATX',strip=['img'])).strip()
    r=corp.get(route,{})
    fm={'title':title,'route':route,'source':'https://aaronspradlin.grok.me'+(route if route!='/' else '')}
    for k in('date','claimStatus','tags','dek'):
        if r.get(k): fm[k]=r[k]
    with open(dest,'w') as o: o.write('---\n'+''.join(f'{k}: {json.dumps(v,ensure_ascii=False)}\n' for k,v in fm.items())+'---\n\n'+body+'\n')
    n+=1
# labs page only in corpus
if not os.path.exists('docs/labs.md') and '/labs' in corp:
    r=corp['/labs'];open('docs/labs.md','w').write(f'---\ntitle: {json.dumps(r["title"])}\nroute: "/labs"\nclaimStatus: "{r["claimStatus"]}"\n---\n\n# {r["title"]}\n\n*{r["dek"]}*\n\n{r["body"]}\n');n+=1
# data files
os.makedirs('docs/data',exist_ok=True)
for p in ['corpus.json','cantos.json','cantos.txt','qa.json','tools.json','cite.txt','search.json','llms-small.txt']:
    shutil.copy(f'{A}/{p}','docs/data/'+p)
shutil.copytree(f'{A}/llms','docs/llms',dirs_exist_ok=True)
os.makedirs('docs/assets',exist_ok=True)
for p in['og.jpg','favicon.svg']: shutil.copy(f'{A}/{p}','docs/assets/'+p)
shutil.copy(f'{A}/claims.jsonl','data_claims_source.jsonl')
print('pages',n)
