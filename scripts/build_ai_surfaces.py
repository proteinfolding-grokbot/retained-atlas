"""Regenerate the AI-vector surfaces from the wiki itself. Run after any research page edit
(build_machine_files.py calls this; CI runs it before `mkdocs build`). Deterministic: same inputs,
same bytes, so nightly PR diffs only show real changes.

Writes:
  docs/progress.jsonl  chronological research updates, one JSON object per line (append-friendly view)
  docs/progress.json   same entries + schema/clocks header
  docs/progress.txt    short plain-text tail for small context windows
  docs/search.json     full static lexical index (keyword + tf-idf) over wiki/package pages + corpus notes/posts/terms
  docs/llms-full.txt   one-file dump: llms.txt, llms-small, cantos, progress, claims ledger
  docs/llms.txt        only the "## Latest progress" block is rewritten
  docs/bot_comms.jsonl|.json|.txt  coordination log from comms/bot_comms.jsonl (+ the tables on wiki/bot-communications.md)

Progress entries are *extracted*, never invented:
  - `### YYYY-MM-DD · <title>` headings (the CONTENT_UPDATE.md format, e.g. run logs), badge from `Badge: **X**`;
  - legacy month-ladder headings `## 9 Jun — ...` whose section carries a standalone badge line;
  - progress/seed.jsonl: hand-curated clock snapshots quoted from existing pages.
Statuses are copied from the page; this script never upgrades anything."""
import json,glob,os,re,math,collections,html
BASE=os.environ.get('SITE_URL','https://proteinfolding-grokbot.github.io/retained-atlas/').rstrip('/')
try:
    from markdown.extensions.toc import slugify as _slug
    def slugify(t): return _slug(t,'-')
except Exception:
    import unicodedata
    def slugify(t):
        t=unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode()
        t=re.sub(r'[^\w\s-]','',t).strip().lower(); return re.sub(r'[-\s]+','-',t)
STAT=['supported','restricted','open','corrected','not claimed','not-claimed','stopped','closed','method']
STATUS_RE=re.compile(r'^(Supported|Restricted|Open|Corrected|Not claimed|Not-claimed|Stopped)\s*$')
MON={m:i for i,m in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(),1)}

def front(s):
    m=re.match(r'---\n(.*?)\n---\n',s,re.S); fm={}
    if not m: return fm,s
    for line in m.group(1).splitlines():
        k,_,v=line.partition(': ')
        try: fm[k]=json.loads(v)
        except Exception: fm[k]=v
    return fm,s[m.end():]

def page_url(p): return BASE+'/'+('' if p=='index' else (p[:-6] if p.endswith('/index') else p)+'/')

def plain(md):
    t=re.sub(r'<div class="ra-math">.*?</div>\s*</div>|<span class="katex.*?</span></span></span>','',md,flags=re.S)
    t=re.sub(r'<video.*?</video>|<audio.*?</audio>','',t,flags=re.S)
    t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t)
    t=re.sub(r'!\[([^\]]*)\]\([^)]*\)',r'\1',t); t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t)
    t=re.sub(r'\{#[^}]*\}','',t); t=re.sub(r'[*`>#|]+',' ',t); t=t.replace('\\','')
    return re.sub(r'\s+',' ',t).strip()

def strip_boiler(body):
    # the shared three-clocks banner and causal-stack nav repeat on every page; drop them from search text
    body=re.sub(r'Three clocks · signal over hype.*?\[Two stacks\]\([^)]*\)\n','',body,flags=re.S)
    body=re.sub(r'\nCausal stack\n\n(?:\d+\.\s+\[[^\n]*\n)+','\n',body)
    return body

def links(sec):
    out=[]
    for u in re.findall(r'\]\((https?://[^)\s]+)\)',sec):
        if u not in out: out.append(u)
    return out[:8]

def location(text):
    # conservative; the page is authoritative
    if re.search(r'research[ -]branch|not on main|not merged|research/|off-main|unmerged|not into main',text,re.I): return 'research_branch'
    if re.search(r'GitHub-only',text): return 'github_only'
    if re.search(r'\b(?:On|on) main\b|merged (?:to|into) main',text): return 'main'
    if re.search(r'x\.com/aaronspradlin/status',text): return 'x_field_note'
    return 'not_stated'

def norm(s): s=s.strip().lower(); return 'not-claimed' if s in ('not claimed','not-claimed') else s

# ---------- bot communications (coordination log, not research progress) ----------
# Source: hand-curated comms/bot_comms.jsonl (one dated event per line) + comms/bots.json (roster, credits).
# Writes docs/bot_comms.jsonl|.json|.txt and the two generated tables on docs/wiki/bot-communications.md.
# Runs before the pages are read so the search index sees the rendered tables. Every row is Not claimed.
COMMS_SRC,COMMS_PAGE='comms/bot_comms.jsonl','docs/wiki/bot-communications.md'
if os.path.exists(COMMS_SRC):
    def _mins(t):
        m=re.match(r'(\d{1,2}):(\d{2}) (AM|PM)$',t or '')
        return (int(m.group(1))%12+(12 if m.group(3)=='PM' else 0))*60+int(m.group(2)) if m else 24*60
    comms=[json.loads(l) for l in open(COMMS_SRC,encoding='utf-8') if l.strip()]
    for c in comms:
        if c.get('status')!='not-claimed': raise SystemExit(f"bot_comms {c.get('id')}: status must be not-claimed")
    comms.sort(key=lambda c:(c['date'],_mins(c.get('time_mst')),c['id']))
    roster=json.load(open('comms/bots.json',encoding='utf-8')) if os.path.exists('comms/bots.json') else {}
    with open('docs/bot_comms.jsonl','w',encoding='utf-8') as o:
        for c in comms: o.write(json.dumps(c,ensure_ascii=False)+'\n')
    json.dump({'schema':'retained-atlas.bot-comms/v1','base':BASE,'page':BASE+'/wiki/bot-communications/',
      'time_zone':'America/Phoenix (MST, UTC-7)',**roster,
      'fields':{'id':'stable event id','date':'YYYY-MM-DD (MST)','time_mst':'h:mm AM/PM MST or null','kind':'wiki_pr | wiki_commit | wiki_commit_note | wiki_pr_comment | coordination | handoff | direction | thread | review_record | heartbeat',
                'from':'who acted','to':'who it was for','channel':'where it happened','location':'wiki_main | wiki_pr_open | research_branch | wiki_ops',
                'status':'always not-claimed','summary':'plain-language summary (private messages are summarized, never quoted)','refs':'public links','does_not_show':'boundary'},
      'rules':['Coordination log only: not research progress, not a claim, never changes a status.',
               'Research-branch items are not on main.','Private agent messages appear only as dated plain summaries.','scientific_breakthrough: false'],
      'count':len(comms),'events':comms},open('docs/bot_comms.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    BT=['# Retained Atlas — bot communications (newest first)','',f'Feed: {BASE}/bot_comms.jsonl · {BASE}/bot_comms.json · page: {BASE}/wiki/bot-communications/',
        'Coordination log, not research progress. Every row is not-claimed. Research-branch items are not on main. Times MST. scientific_breakthrough: false','']
    for c in reversed(comms[-40:]):
        BT.append(f"{c['date']}{(' '+c['time_mst']) if c.get('time_mst') else ''} [{c['kind']}] [{c['location']}] {c['from']} -> {c['to']}: {c['summary']}")
    open('docs/bot_comms.txt','w',encoding='utf-8').write('\n'.join(BT)+'\n')
    def _ref(u):
        repo='wiki' if '/retained-atlas/' in u else 'WetLabEngine'
        for pat,fmt in ((r'issuecomment-(\d+)','comment {}'),(r'/actions/runs/(\d+)','run {}'),(r'/commit/([0-9a-f]{7})','`{}`'),(r'/pull/(\d+)$',repo+' PR #{}')):
            m=re.search(pat,u)
            if m: return f'[{fmt.format(m.group(1))}]({u})'
        return f'[link]({u})'
    def _cell(t): return (t or '').replace('|','\\|').replace('\n',' ')
    def _table(rows,cols):
        out=['| '+' | '.join(h for h,_ in cols)+' |','| '+' | '.join('---' for _ in cols)+' |']
        for c in rows: out.append('| '+' | '.join(_cell(f(c)) for _,f in cols)+' |')
        return '\n'.join(out)
    when=lambda c:c['date']+(' · '+c['time_mst'] if c.get('time_mst') else '')
    refs=lambda c:', '.join(_ref(u) for u in c.get('refs') or []) or 'private (summarized)'
    tl=_table([c for c in comms if c['kind']!='wiki_commit'],[('When (MST)',when),('From → to',lambda c:f"{c['from']} → {c['to']}"),('Channel',lambda c:c['channel']),('What happened',lambda c:c['summary']),('Sources',refs)])
    cm=_table([c for c in comms if c['kind']=='wiki_commit'],[('When (MST)',when),('Pushed by',lambda c:c['from']),('Commit',refs),('Message',lambda c:c['summary'])])
    if os.path.exists(COMMS_PAGE):
        pg=open(COMMS_PAGE,encoding='utf-8').read()
        for tag,tbl in (('timeline',tl),('commits',cm)):
            pg=re.sub(rf'(<!-- bot-comms:{tag}:start -->\n).*?(<!-- bot-comms:{tag}:end -->)',lambda m:m.group(1)+'\n'+tbl+'\n\n'+m.group(2),pg,flags=re.S)
        open(COMMS_PAGE,'w',encoding='utf-8').write(pg)

pages=[]
for f in sorted(glob.glob('docs/**/*.md',recursive=True)):
    s=open(f,encoding='utf-8').read(); fm,body=front(s); pages.append((f[5:-3],fm,body))

# ---------- progress ----------
entries=[]
for p,fm,body in pages:
    if not p.startswith('wiki/'): continue
    year=str(fm.get('date','2026'))[:4]; used=collections.Counter()
    heads=list(re.finditer(r'^(#{2,3}) (.+?)\s*$',body,re.M))
    for i,h in enumerate(heads):
        lvl,title=h.group(1),h.group(2)
        end=heads[i+1].start() if i+1<len(heads) else len(body)
        sec=body[h.end():end]
        idm=re.search(r'\{#([^}]+)\}\s*$',title); title_clean=re.sub(r'\s*\{#[^}]+\}\s*$','',title)
        anchor=idm.group(1) if idm else slugify(title_clean)
        if not idm:
            used[anchor]+=1
            if used[anchor]>1: anchor=f'{anchor}_{used[anchor]-1}'
        a=re.match(r'(\d{4}-\d{2}-\d{2})\s*·\s*(.+)$',title_clean)
        b=re.match(r'(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b(?: (\d{4}))?\s*(.*)$',title_clean)
        if a and lvl=='###':
            date,t=a.group(1),a.group(2)
            bm=re.search(r'Badge:\s*\*\*([^*]+)\*\*',sec); status=norm(bm.group(1)) if bm else None
            detail=re.sub(r'^Badge:\s*','',re.search(r'^Badge:.*$',sec,re.M).group(0)).replace('**','') if bm else None
            sm=re.search(r'\*\*Plain summary:\*\*\s*(.+)',sec) or re.search(r'Plain summary:\**\s*(.+)',sec)
            dm=re.search(r'\*\*Does NOT show:\*\*\s*(.+)',sec) or re.search(r'Does NOT show:\**\s*(.+)',sec)
            summary=plain(sm.group(1)) if sm else plain(sec)[:500]
            dns=plain(dm.group(1)) if dm else None
            fmt='dated-entry'
        elif b and lvl=='##':
            st=[l for l in sec.splitlines() if STATUS_RE.match(l.strip())]
            if not st: continue  # undated badge -> not a progress item
            date=f"{b.group(3) or year}-{MON[b.group(2)]:02d}-{int(b.group(1)):02d}"
            t=fm.get('title',p)+': '+(re.sub(r'^[—–-]\s*','',b.group(4)).strip() or title_clean)
            status=norm(st[0]); detail=None
            paras=[x for x in re.split(r'\n\s*\n',sec) if x.strip() and not x.lstrip().startswith(('<','!['))]
            summary=plain(paras[0])[:500] if paras else ''
            dns=None; fmt='ladder-section'
        else: continue
        claims=sorted(set(re.findall(r'\b(atlas:[a-z0-9][a-z0-9-]*)',sec)))
        e={'id':f'{p[5:]}#{anchor}','date':date,'title':plain(t),'status':status,'status_detail':detail,
           'location':location(sec+' '+t),'claim_ids':claims,'summary':summary,'does_not_show':dns,
           'page':page_url(p),'url':page_url(p)+'#'+anchor,'sources':links(sec),'format':fmt}
        entries.append(e)
# dated ledger claims (date = first explicit date in the claim text; status copied from the ledger)
anchors={}
for p,fm,body in pages:
    for i in re.findall(r'id="(atlas:[a-z0-9-]+)"',body):
        if i not in anchors or p=='wiki/claim-ledger': anchors[i]=p
for l in open('claims/ledger.jsonl',encoding='utf-8'):
    if not l.strip(): continue
    c=json.loads(l)
    m=re.search(r'\b(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (\d{4})\b',c.get('text',''))
    if not m: continue
    pg=anchors.get(c['id'],'wiki/claim-ledger')
    entries.append({'id':'claim/'+c['id'],'date':f"{m.group(3)}-{MON[m.group(2)]:02d}-{int(m.group(1)):02d}",'title':c.get('title',''),
      'status':norm(c.get('status','')),'status_detail':None,'location':location(c.get('text','')),'claim_ids':[c['id']],
      'summary':c.get('text',''),'does_not_show':c.get('doesNotShow'),'page':page_url(pg),
      'url':page_url(pg)+('#'+c['id'] if c['id'] in anchors else ''),'sources':[],'format':'ledger-claim'})
if os.path.exists('progress/seed.jsonl'):
    for l in open('progress/seed.jsonl',encoding='utf-8'):
        if l.strip(): e=json.loads(l); e.setdefault('format','seed'); entries.append(e)
seen=set(); uniq=[]
for e in sorted(entries,key=lambda e:(e['date'],e['id'])):
    if e['id'] in seen: continue
    seen.add(e['id']); uniq.append(e)
entries=uniq
with open('docs/progress.jsonl','w',encoding='utf-8') as o:
    for e in entries: o.write(json.dumps(e,ensure_ascii=False)+'\n')
compile_m=re.search(r'compiled (\d{4}-\d{2}-\d{2})',open('overrides/main.html',encoding='utf-8').read())
clocks={'wiki_compile':compile_m.group(1) if compile_m else None,
        'latest_progress_entry':entries[-1]['date'] if entries else None,
        'scientific_breakthrough':False,
        'note':'Clocks are separate. latest_progress_entry is the newest dated wiki entry, not a STATUS.md change and not an X post.'}
json.dump({'schema':'retained-atlas.progress/v1','base':BASE,'clocks':clocks,
  'fields':{'id':'stable <slug>#<anchor>','date':'YYYY-MM-DD of the research event (seed clock rows: observed at compile)',
            'status':'badge copied from the page: supported|restricted|open|corrected|not-claimed|stopped',
            'location':'main | research_branch | github_only | x_field_note | clock_snapshot | not_stated (inferred conservatively from the entry text; the page is authoritative)',
            'claim_ids':'ledger ids (claims.jsonl) anchored inside the entry','does_not_show':'claim boundary when the entry states one',
            'url':'canonical wiki anchor','sources':'commit / run / X links quoted by the entry'},
  'rules':['Never upgrade a status from this feed. The wiki page and WetLabEngine STATUS.md are authoritative.',
           'Restricted research-branch items are not on main and are not STATUS gates.','scientific_breakthrough: false'],
  'count':len(entries),'entries':entries},open('docs/progress.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
T=['# Retained Atlas — progress (newest first)','',f'Feed: {BASE}/progress.jsonl · {BASE}/progress.json · contract: {BASE}/wiki/ai-participate/',
   f"Wiki compile: {clocks['wiki_compile']} · newest dated entry: {clocks['latest_progress_entry']} · scientific_breakthrough: false",
   'Badges are copied from the pages. Restricted research-branch work is not on main and not a STATUS gate. Do not upgrade.','']
for e in reversed(entries[-40:]):
    T.append(f"{e['date']} [{e['status']}] [{e['location']}] {e['title']}")
    T.append(f"  {e['url']}"+(f"  claims: {', '.join(e['claim_ids'])}" if e['claim_ids'] else ''))
open('docs/progress.txt','w',encoding='utf-8').write('\n'.join(T)+'\n')

# ---------- search index ----------
corpus=json.load(open('docs/corpus.json',encoding='utf-8'))
docs=[]
for p,fm,body in pages:
    if p in ('search',) or not fm.get('title'): continue
    kind='package' if p.startswith('packages/') else ('wiki' if p.startswith('wiki/') else 'page')
    text=plain(strip_boiler(body))
    docs.append({'id':('pkg:' if kind=='package' else 'wiki:')+(p.split('/',1)[-1] if '/' in p else p),'kind':kind,
      'title':fm.get('title'),'dek':fm.get('dek') or fm.get('description') or '','tags':fm.get('tags') or [],
      'claimStatus':fm.get('claimStatus'),'date':fm.get('date'),'url':page_url(p),'body':text})
for r in corpus['records']:
    if r['kind'] in ('note','post','term'):
        h=r.get('href') or ''; m=re.match(r'^(/[^#]*)(#.*)?$',h)
        url=(BASE+(m.group(1).rstrip('/')+'/' if m.group(1)!='/' else '/')+(m.group(2) or '')) if m else h
        docs.append({'id':r['id'],'kind':r['kind'],'title':r.get('title'),'dek':r.get('dek',''),'tags':r.get('tags') or [],
          'claimStatus':r.get('claimStatus'),'date':r.get('date'),'url':url,'sourceUrl':r.get('sourceUrl'),'body':r.get('body','')})
STOP=set('a an and are as at be by for from has have in is it its of on or that the this to was were with not no but than then which who what when where how also into only same one two any can its their there these those been will would should may might does do did our we you he she they them his her'.split())
def toks(t): return [w for w in re.findall(r'[a-z0-9][a-z0-9._-]*[a-z0-9]|[a-z0-9]',t.lower()) if w not in STOP and len(w)>1]
df=collections.Counter(); tfs=[]
for d in docs:
    tf=collections.Counter(toks(' '.join([d['title'] or '']*3+[d['dek'] or '']*2+[' '.join(d['tags'])]*2+[d['body']])))
    tfs.append(tf); df.update(tf.keys())
N=len(docs); idf={w:round(math.log((N+1)/(c+1))+1,4) for w,c in df.items() if c>=2}
idf_default=round(math.log((N+1)/2)+1,4)
for d,tf in zip(docs,tfs):
    w={t:(1+math.log(c))*idf.get(t,idf_default) for t,c in tf.items()}
    n=math.sqrt(sum(v*v for v in w.values())) or 1
    top=sorted(w.items(),key=lambda x:(-x[1],x[0]))[:48]
    d['tfidf']=[[t,round(v/n,4)] for t,v in top]  # [term, weight] pairs (not an object: keeps keys like scientific_breakthrough out of key:value form)
docs.sort(key=lambda d:d['id'])
json.dump({'schema':'retained-atlas.search/v1','base':BASE,'static':True,
  'how_to_query':('GitHub Pages is static: /search.json ignores ?q=. Download this file once and rank locally. '
    'keyword: case-insensitive substring/term match over title, dek, tags, body (title hits first). '
    'tfidf: tokenize the query like the index (lowercase, [a-z0-9._-] terms, stopwords dropped), weight each query term by idf '
    '(idf and doc.tfidf are lists of [term, weight] pairs; idf_default if absent), score = sum(query_weight * doc_weight[term]) with the query vector L2-normalized. Reference client: '+BASE+'/search_client.py. '
    'Keep claimStatus with every hit. A hit that looks newer never beats /wiki/live-gates or WetLabEngine STATUS.md.'),
  'modes':['keyword','tfidf'],'kinds':sorted(set(d['kind'] for d in docs)),'count':N,
  'tokenizer':{'pattern':'[a-z0-9][a-z0-9._-]*[a-z0-9]|[a-z0-9]','lowercase':True,'stopwords':sorted(STOP),'min_len':2},
  'idf_default':idf_default,'idf':[[t,v] for t,v in sorted(idf.items())],'docs':docs,
  'scientific_breakthrough':False},open('docs/search.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))

# ---------- llms.txt latest-progress block ----------
lt=open('docs/llms.txt',encoding='utf-8').read()
blk=['## Latest progress (generated from /progress.jsonl — badges copied, never upgraded)','']
for e in reversed(entries[-8:]): blk.append(f"- {e['date']} [{e['status']}] [{e['location']}] {e['title']} — {e['url']}")
blk+=['',f'Full feed: {BASE}/progress.jsonl · {BASE}/progress.txt','','']
new=re.sub(r'## Latest progress.*?(?=^## )','\n'.join(blk),lt,flags=re.S|re.M) if '## Latest progress' in lt else lt
open('docs/llms.txt','w',encoding='utf-8').write(new)

# ---------- llms-full.txt ----------
F=['# Retained Atlas — llms-full (generated; one file for models that want everything)','',
   f'Base: {BASE}/ · generated from the repo by scripts/build_ai_surfaces.py · scientific_breakthrough: false','']
for f in ['docs/llms.txt','docs/llms-small.txt','docs/cantos.txt']+sorted(glob.glob('docs/llms/c*.txt'))+['docs/progress.txt']+(['docs/bot_comms.txt'] if os.path.exists('docs/bot_comms.txt') else [])+['docs/cite.txt']:
    F+=[f'======== {BASE}/{f[5:]} ========','',open(f,encoding='utf-8').read().rstrip(),'']
F+=[f'======== {BASE}/claims.jsonl ========','']
for l in open('claims/ledger.jsonl',encoding='utf-8'):
    if l.strip():
        c=json.loads(l); F.append(f"- {c['id']} [{c.get('status')}] {c.get('title','')}: {c.get('text','')}")
open('docs/llms-full.txt','w',encoding='utf-8').write('\n'.join(F)+'\n')
print(f'ai surfaces: {len(entries)} progress entries, {N} search docs, {len(idf)} idf terms')
