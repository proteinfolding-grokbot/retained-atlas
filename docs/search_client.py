#!/usr/bin/env python3
"""Reference client for the static Retained Atlas search index (GitHub Pages cannot run ?q= queries).
usage: python search_client.py "receiver identification" [--mode keyword|tfidf] [--kind wiki|package|note|term|post] [--limit 10]
Downloads https://proteinfolding-grokbot.github.io/retained-atlas/search.json once and ranks locally.
Every hit keeps its claimStatus. A newer-looking hit never beats /wiki/live-gates or WetLabEngine STATUS.md."""
import json,re,sys,math,argparse,urllib.request
URL='https://proteinfolding-grokbot.github.io/retained-atlas/search.json'
def load(src=URL):
    if src.startswith('http'):
        with urllib.request.urlopen(src) as r: return json.load(r)
    return json.load(open(src,encoding='utf-8'))
def toks(ix,q):
    t=ix['tokenizer']; stop=set(t['stopwords'])
    return [w for w in re.findall(t['pattern'],q.lower()) if w not in stop and len(w)>=t['min_len']]
def search(ix,q,mode='tfidf',kind=None,limit=10):
    docs=[d for d in ix['docs'] if not kind or d['kind']==kind]; out=[]
    if mode=='keyword':
        ql=q.lower(); terms=toks(ix,q) or [ql]
        for d in docs:
            title=(d.get('title') or '').lower(); hay=' '.join([title,(d.get('dek') or '').lower(),' '.join(d.get('tags') or []).lower(),d.get('body','').lower()])
            if ql in hay or all(t in hay for t in terms):
                s=(1000 if ql in title else 0)+sum(hay.count(t) for t in terms); out.append((s,d))
    else:
        idf=dict(ix['idf']); qt=toks(ix,q); w={t:idf.get(t,ix['idf_default']) for t in qt}; n=math.sqrt(sum(v*v for v in w.values())) or 1
        for d in docs:
            dw=dict(d['tfidf']); s=sum(v/n*dw.get(t,0) for t,v in w.items())
            if s>0: out.append((s,d))
    out.sort(key=lambda x:-x[0])
    return [{'score':round(s,4),'id':d['id'],'kind':d['kind'],'title':d['title'],'claimStatus':d.get('claimStatus'),'url':d['url'],
             'snippet':(d.get('dek') or d.get('body',''))[:240]} for s,d in out[:limit]]
if __name__=='__main__':
    a=argparse.ArgumentParser(); a.add_argument('q'); a.add_argument('--mode',default='tfidf',choices=['keyword','tfidf'])
    a.add_argument('--kind'); a.add_argument('--limit',type=int,default=10); a.add_argument('--index',default=URL); o=a.parse_args()
    print(json.dumps(search(load(o.index),o.q,o.mode,o.kind,o.limit),ensure_ascii=False,indent=1))
