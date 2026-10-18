"""One-time: snapshot every protected status line / claim boundary from the ORIGINAL archive
into claims/protected_lines.json. claim_guard.py fails a PR if any of these disappear or change."""
import re,json,glob,os
from bs4 import BeautifulSoup
A='../source-archive'
KW=re.compile(r'scientific_breakthrough|Theory of Everything|merged to main|not on main|Pillar 3|Not claimed|Not Einstein|Supported four|supported four|noncommercial|identity|Identity|License',re.I)
def norm(t): return re.sub(r'\s+',' ',t.replace('·',' ')).strip()
def built_path(route):
    if route=='/': return 'index.html'
    return route.strip('/')+'/index.html'
out={}
for f in sorted(glob.glob(f'{A}/pages/*.html'))+sorted(glob.glob(f'{A}/extra-pages/*.html')):
    r=os.path.basename(f)[:-5].replace('_','/'); r='/' if r=='/index' else r
    s=BeautifulSoup(open(f,encoding='utf-8',errors='replace').read(),'lxml')
    m=s.find('article') or s.find('main')
    if not m: continue
    for t in m.find_all(['script','style','svg','noscript']): t.decompose()
    lines=set()
    for chunk in re.split(r'(?<=[.!?])\s+|\n',m.get_text('\n')):
        c=norm(chunk)
        if len(c)>=8 and KW.search(c): lines.add(c)
    if lines: out[built_path(r)]=sorted(lines)
json.dump(out,open('claims/protected_lines.json','w'),ensure_ascii=False,indent=1)
print(len(out),'pages',sum(map(len,out.values())),'protected lines')
