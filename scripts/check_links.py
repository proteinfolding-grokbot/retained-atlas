"""Offline internal link checker for the built site/ directory: every internal href/src
(and #anchor) must resolve. External links are not fetched (X/GitHub rate-limit CI)."""
import os,sys,glob,urllib.parse
from bs4 import BeautifulSoup
ROOT='site'; bad=[]; ids={}
import re
PREFIX=urllib.parse.urlparse(re.search(r'^site_url:\s*(\S+)',open('mkdocs.yml').read(),re.M).group(1)).path or '/'
def page_ids(f):
    if f not in ids:
        s=BeautifulSoup(open(f,encoding='utf-8').read(),'lxml'); ids[f]={e['id'] for e in s.find_all(id=True)}
    return ids[f]
n=0
for f in glob.glob(ROOT+'/**/*.html',recursive=True):
    s=BeautifulSoup(open(f,encoding='utf-8').read(),'lxml')
    for e in s.find_all(['a','img','source','video','link','script']):
        for at in ('href','src','poster'):
            u=e.get(at)
            if not u or u.startswith(('http:','https:','mailto:','data:','javascript:','//')): continue
            n+=1; p=urllib.parse.urlparse(u)
            if p.path.startswith('/'):
                rp=p.path[len(PREFIX):] if p.path.startswith(PREFIX) else None
                if rp is None: bad.append(f'{f[len(ROOT)+1:]}: {u} (outside site)'); continue
                t=os.path.join(ROOT,urllib.parse.unquote(rp))
            else: t=os.path.normpath(os.path.join(os.path.dirname(f),urllib.parse.unquote(p.path))) if p.path else f
            if os.path.isdir(t): t=os.path.join(t,'index.html')
            if not os.path.exists(t): bad.append(f'{f[len(ROOT)+1:]}: {u} (404)'); continue
            if p.fragment and t.endswith('.html') and p.fragment not in page_ids(t):
                bad.append(f'{f[len(ROOT)+1:]}: {u} (missing anchor)')
print(f'{n} internal links checked, {len(bad)} broken')
for b in bad[:200]: print(' -',b)
sys.exit(1 if bad else 0)
