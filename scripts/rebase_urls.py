"""One-time, idempotent: point AI entry surfaces (llms/cantos/cite/tools/qa) at the GitHub Pages base.
aaronspradlin.grok.me stays the human-facing mirror (it iframes this site). Research text is not touched;
only URLs are rewritten. Usage: python scripts/rebase_urls.py"""
import re,glob
BASE='https://proteinfolding-grokbot.github.io/retained-atlas'
FILES=['docs/llms.txt','docs/llms-small.txt','docs/cite.txt','docs/tools.json','docs/cantos.txt','docs/cantos.json','docs/qa.json']+sorted(glob.glob('docs/llms/*.txt'))
def sub(m):
    p=m.group(1) or ''
    if p.startswith('/page.json'):
        s=re.search(r'slug=([a-z0-9-]+)',p); return f'{BASE}/data/page/{s.group(1)}.json' if s else f'{BASE}/data/page/'
    if p.startswith('/search.json'): return f'{BASE}/search.json'
    w=re.match(r'(/(?:wiki|packages)/[a-z0-9-]+)(.*)',p)
    if w: return f'{BASE}{w.group(1)}/{w.group(2)}'
    return BASE+(p or '/')
n=0
for f in FILES:
    s=open(f,encoding='utf-8').read()
    t,k=re.subn(r'https://aaronspradlin\.grok\.me(/[^\s"\'<>)\]]*?)?(?=[\s"\'<>)\]]|\.(?:\s|$)|$)',sub,s)
    if t!=s: open(f,'w',encoding='utf-8').write(t); n+=k; print(f,k)
print(n,'urls rebased')
