"""Migration audit: original grok.me site vs new MkDocs site.
usage: python scripts/audit_migration.py NEW_BASE [--extra] > report.json
NEW_BASE e.g. https://proteinfolding-grokbot.github.io/retained-atlas"""
import sys,re,json,hashlib,urllib.parse,concurrent.futures as cf
import requests
from bs4 import BeautifulSoup
ORIG='https://aaronspradlin.grok.me'; NEW=sys.argv[1].rstrip('/')
S=requests.Session(); S.headers['User-Agent']='retained-atlas-audit'
def get(u):
    for _ in range(3):
        try: return S.get(u,timeout=30)
        except Exception as e: err=e
    raise err
sm=get(ORIG+'/sitemap.xml').text
urls=[u.replace(ORIG,'') or '/' for u in re.findall(r'<loc>([^<]+)</loc>',sm)]
if '--extra' in sys.argv:
    urls+=[l.strip() for l in open(sys.argv[sys.argv.index('--extra')+1]) if l.strip()]
def newurl(p):
    if p=='/': return NEW+'/'
    if re.search(r'\.\w+$',p): return NEW+p
    return NEW+p+'/'
DROP=['script','style','svg','noscript','button','input','form']
def extract(html,orig):
    s=BeautifulSoup(html,'lxml')
    m=(s.find('article') or s.find('main')) if orig else (s.select_one('article.md-content__inner') or s.find('article'))
    if m is None: return None
    for t in m.find_all(DROP):
        if t.name=='button' and (t.find('img') or t.find('video')): t.unwrap(); continue
        if t.name=='svg' and t.find_parent(class_='katex'): continue
        t.decompose()
    for t in m.select('a.headerlink, .md-source-file, .md-content__button'): t.decompose()
    for k in m.select('.katex-mathml'): k.decompose()
    text=m.get_text('\n')
    imgs=[urllib.parse.urlparse(i.get('src','')).path.split('/')[-1] for i in m.find_all('img')]
    return dict(text=text,
        headings=[norm(h.get_text(' ')) for h in m.find_all(['h1','h2','h3','h4'])],
        links=[norm(a.get_text(' ')) for a in m.find_all('a',href=True) if norm(a.get_text(' ')) not in ('','#')],
        tables=len(m.find_all('table')),code=len(m.find_all('pre')),
        math=len([k for k in m.select('.katex') if not k.find_parent(class_='katex')]),
        images=[i for i in imgs if i and i!='favicon.svg'],videos=len(m.find_all('video')),
        title=(s.title.string or '').strip() if s.title else '',
        description=(s.find('meta',attrs={'name':'description'}) or {}).get('content',''))
def norm(t): return re.sub(r'\s+',' ',t.replace('·',' ').replace('\u200b','')).strip()
def key(t): return re.sub(r'[^\w]','',norm(t).lower())
def sentences(t):
    out=[]
    for chunk in re.split(r'(?<=[.!?])\s+|\n',t):
        c=norm(chunk)
        if len(key(c))>=12: out.append(c)
    return out
def audit(p):
    o=get(ORIG+p); n=get(newurl(p)); o.encoding=n.encoding='utf-8'
    r={'path':p,'orig_status':o.status_code,'new_url':newurl(p),'new_status':n.status_code}
    if n.status_code!=200: r['coverage']=0.0; return r
    ct=o.headers.get('content-type','')
    if 'text/html' not in ct:
        r['kind']='file'; r['byte_identical']=o.content==n.content
        r['sha_orig']=hashlib.sha256(o.content).hexdigest()[:16]; r['sha_new']=hashlib.sha256(n.content).hexdigest()[:16]
        r['coverage']=100.0 if r['byte_identical'] else 0.0; return r
    eo,en=extract(o.text,True),extract(n.text,False)
    r['kind']='page'
    if not eo or not en: r['coverage']=0.0; r['error']='no article'; return r
    nk=key(en['text']); ss=sentences(eo['text'])
    miss=[x for x in ss if key(x) not in nk]
    r['sentences']=len(ss); r['missing_sentences']=miss
    r['coverage']=round(100*(len(ss)-len(miss))/len(ss),2) if ss else 100.0
    def lost(a,b):
        b=list(b); out=[]
        for x in a:
            if x in b: b.remove(x)
            else: out.append(x)
        return out
    r['missing_headings']=[h for h in eo['headings'] if key(h) not in {key(x) for x in en['headings']}]
    r['missing_links']=lost([key(x) for x in eo['links']],[key(x) for x in en['links']])
    r['missing_images']=lost(eo['images'],en['images'])
    for k in ('tables','code','math','videos'):
        r[k]=[eo[k],en[k]]
    r['title']=en['title']; r['description']=bool(en['description'])
    return r
with cf.ThreadPoolExecutor(8) as ex: res=list(ex.map(audit,urls))
json.dump(res,sys.stdout,ensure_ascii=False,indent=1)
