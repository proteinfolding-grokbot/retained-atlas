"""Claim guard (runs in CI after `mkdocs build`).
Fails if:
  1. any protected status line / claim boundary (claims/protected_lines.json) is missing from the built page;
  2. `scientific_breakthrough: true` (or any value other than false) appears anywhere in docs/;
  3. a claim id in the base branch's claims ledger disappears, or its status is upgraded
     (open/corrected/stopped/not claimed -> restricted -> supported);
  4. docs/claims.jsonl is not identical to claims/ledger.jsonl;
  5. the site-wide boundaries (banner, license) are gone.
usage: python scripts/claim_guard.py [BASE_LEDGER_FILE]"""
import sys,re,json,glob,os
from bs4 import BeautifulSoup
ERR=[]
def key(t): return re.sub(r'[^\w]','',re.sub(r'\s+',' ',t.replace('·',' ')).lower())
# 1 protected lines
prot=json.load(open('claims/protected_lines.json'))
cache={}
for path,lines in prot.items():
    f='site/'+path
    if not os.path.exists(f): ERR.append(f'protected page removed: {path} ({len(lines)} protected lines)'); continue
    s=BeautifulSoup(open(f,encoding='utf-8').read(),'lxml'); a=s.select_one('article') or s
    k=key(a.get_text('\n'))
    for l in lines:
        if key(l) not in k: ERR.append(f'{path}: protected line missing or changed: "{l}"')
# 2 scientific_breakthrough
for f in glob.glob('docs/**/*',recursive=True)+['mkdocs.yml','overrides/main.html']:
    if os.path.isdir(f) or not f.endswith(('.md','.html','.txt','.json','.jsonl','.yml')): continue
    for m in re.finditer(r'scientific_breakthrough["\']?\s*[:=]\s*["\']?(\w+)',open(f,encoding='utf-8',errors='replace').read()):
        if m.group(1).lower()!='false': ERR.append(f'{f}: scientific_breakthrough set to {m.group(1)}')
# 3/4 claims ledger
RANK={'supported':2,'restricted':1}
def load(p): return {c['id']:c for c in (json.loads(l) for l in open(p,encoding='utf-8') if l.strip())}
head=load('claims/ledger.jsonl')
base=load(sys.argv[1]) if len(sys.argv)>1 and os.path.exists(sys.argv[1]) else load('claims/ledger.jsonl')
for i,c in base.items():
    if i not in head: ERR.append(f'claim removed from ledger: {i}'); continue
    b,h=c.get('status',''),head[i].get('status','')
    if RANK.get(h.lower(),0)>RANK.get(b.lower(),0): ERR.append(f'claim {i} status upgraded {b} -> {h}')
if open('docs/claims.jsonl','rb').read()!=open('claims/ledger.jsonl','rb').read():
    ERR.append('docs/claims.jsonl differs from claims/ledger.jsonl (published ledger must equal the reviewed ledger)')
# 5 site-wide
banner=open('overrides/main.html').read()
for p in ['scientific_breakthrough: false','Pillar 3 open','Not a completed Theory of Everything']:
    if p not in banner: ERR.append(f'site banner lost: "{p}"')
if 'Source-available for noncommercial research and evaluation only' not in open('mkdocs.yml').read(): ERR.append('license line removed from mkdocs.yml')
if ERR:
    print('CLAIM GUARD FAILED:'); [print(' -',e) for e in ERR]; sys.exit(1)
print(f'claim guard OK: {sum(map(len,prot.values()))} protected lines on {len(prot)} pages, {len(head)} ledger claims, none removed or upgraded')
