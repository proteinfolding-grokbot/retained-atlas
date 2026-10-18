"""Regenerate docs/llms.txt and docs/claims.jsonl from docs/**/*.md front matter + claims/ledger.jsonl.
Run before `mkdocs build` (the Actions workflow does this)."""
import json,glob,os,re
BASE=os.environ.get('SITE_URL','https://proteinfolding-grokbot.github.io/retained-atlas/').rstrip('/')
pages=[]
for f in sorted(glob.glob('docs/**/*.md',recursive=True)):
    s=open(f).read(); m=re.match(r'---\n(.*?)\n---\n',s,re.S)
    if not m: continue
    fm={}
    for line in m.group(1).splitlines():
        k,_,v=line.partition(': ')
        try: fm[k]=json.loads(v)
        except Exception: fm[k]=v
    p=f[5:-3]; url=BASE+'/'+('' if p=='index' else p+'/')
    pages.append((p,fm,url))
claims=[json.loads(l) for l in open('claims/ledger.jsonl') if l.strip()]
with open('docs/claims.jsonl','w') as o:
    for c in claims: o.write(json.dumps(c,ensure_ascii=False)+'\n')
    for p,fm,url in pages:
        if fm.get('claimStatus'):
            o.write(json.dumps({'id':'page:'+p,'status':fm['claimStatus'],'title':fm.get('title'),'text':fm.get('dek',''),'url':url,'date':fm.get('date')},ensure_ascii=False)+'\n')
L=['# Retained Atlas','','Compiled research wiki of Aaron Spradlin (@aaronspradlin).',
'Thesis: start with identities that cannot be erased. Do not smuggle entropy, area laws, causal order, or a metric. Ask what geometry, if any, is forced to appear. Gravity is a candidate, not a result.',
'','scientific_breakthrough: false · Not a completed Theory of Everything · Pillar 3 open','',
f'Public: {BASE}/','Original (Grok-hosted, archived): https://aaronspradlin.grok.me','X archive: https://x.com/aaronspradlin','GitHub evidence: https://github.com/proteinfoldingengine/WetLabEngine','',
'## Preferred ingest (cantos)','','Each canto is a closed unit: badge, clock, canonical URL, does_not_show. Read in order. Do not merge clocks.','']
L+=[f'- {BASE}/llms/{os.path.basename(x)}' for x in sorted(glob.glob('docs/llms/*.txt'))]
L+=['',f'Claims ledger: {BASE}/claims.jsonl · Corpus: {BASE}/data/corpus.json','','## Pages','']
L+=[f"- [{fm.get('title',p)}]({url})"+(f" [{fm['claimStatus']}]" if fm.get('claimStatus') else '')+(f": {fm['dek']}" if fm.get('dek') else '') for p,fm,url in pages]
open('docs/llms.txt','w').write('\n'.join(L)+'\n')
print(len(pages),'pages,',len(claims),'ledger claims')
