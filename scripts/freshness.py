"""Generated "Last wiki update" clock for the landing page and the machine entry points.

Reads progress/source_revision.json, docs/progress.jsonl (or docs/progress.json), and the
wiki main commit. Does not invent a timestamp and refuses a time later than now.
The v15.03 release compile date stays the historic wiki compile clock.

Called from build_machine_files.py before build_ai_surfaces.py so one run is stable.
"""
import json, os, re, subprocess
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.environ.get('SITE_URL', 'https://proteinfolding-grokbot.github.io/retained-atlas/').rstrip('/')

def mst():
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo('America/Phoenix')
    except Exception:
        return timezone(timedelta(hours=-7))

MST = mst()

def git_out(args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()

def to_mst(iso):
    dt = datetime.fromisoformat(iso.replace('Z', '+00:00'))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=MST)
    return dt.astimezone(MST).replace(microsecond=0)

def wiki_main():
    """(full sha, MST ISO). origin/main when this checkout can see it, else main, else HEAD."""
    for spec in ('origin/main', 'main', 'HEAD'):
        try:
            raw = git_out(['log', '-1', '--format=%H %cI', spec])
        except (subprocess.CalledProcessError, OSError):
            continue
        if not raw or ' ' not in raw:
            continue
        sha, iso = raw.split(' ', 1)
        return sha, to_mst(iso).isoformat(timespec='seconds')
    raise SystemExit('freshness: cannot read a wiki main commit')

def latest_progress():
    path = os.path.join(ROOT, 'docs/progress.jsonl')
    latest = None
    if os.path.exists(path):
        for line in open(path, encoding='utf-8'):
            if not line.strip():
                continue
            date = json.loads(line).get('date')
            if date and (latest is None or str(date) > latest):
                latest = str(date)
    if latest:
        return latest
    prog = os.path.join(ROOT, 'docs/progress.json')
    if os.path.exists(prog):
        clocks = json.load(open(prog, encoding='utf-8')).get('clocks') or {}
        if clocks.get('latest_progress_entry'):
            return clocks['latest_progress_entry']
    raise SystemExit('freshness: no progress entry date in docs/progress.jsonl')

def compile_date(banner):
    m = re.search(r'v15\.03 release compile date (\d{4}-\d{2}-\d{2})', banner)
    if m:
        return m.group(1)
    m = re.search(r'compiled (\d{4}-\d{2}-\d{2})', banner)
    if m:
        return m.group(1)
    prog = os.path.join(ROOT, 'docs/progress.json')
    if os.path.exists(prog):
        clocks = json.load(open(prog, encoding='utf-8')).get('clocks') or {}
        if clocks.get('wiki_compile'):
            return clocks['wiki_compile']
    raise SystemExit('freshness: cannot find the v15.03 release compile date')

def assert_not_future(dt, label):
    now = datetime.now(MST)
    if dt > now:
        raise SystemExit(f'freshness: {label} {dt.isoformat()} is later than now {now.isoformat()}')

def facts():
    os.chdir(ROOT)
    rev = json.load(open('progress/source_revision.json', encoding='utf-8'))
    if rev.get('scientific_breakthrough') is not False:
        raise SystemExit('freshness: source revision scientific_breakthrough is not false')
    banner = open('overrides/main.html', encoding='utf-8').read()
    compile_d = compile_date(banner)
    latest = latest_progress()
    latest_dt = datetime.fromisoformat(latest).replace(tzinfo=MST)
    assert_not_future(latest_dt, 'latest progress entry')
    sha, iso = wiki_main()
    commit_dt = datetime.fromisoformat(iso)
    assert_not_future(commit_dt, 'wiki main commit')
    wet_full = rev['wetlab_main']['sha']
    tip_full = rev['research_branch']['tip']
    branch = rev['research_branch']['name']
    not_main = bool(rev['research_branch'].get('not_wetlab_main'))
    where = 'research branch, not on main' if not_main else 'research branch'
    wet, tip, short = wet_full[:8], tip_full[:8], sha[:8]
    body = (
        f'Newest progress entry {latest}. Wiki main commit {commit_dt.date().isoformat()} ({short}, {iso}). '
        f'WetLabEngine main {wet}. Research tip {tip} on {branch} ({where}). '
        f'Progress: /progress.jsonl. llms.txt: /llms.txt. '
        f'The v15.03 release compile date {compile_d} is a separate historic clock. '
        f'scientific_breakthrough: false. Pillar 3 open. Not a completed Theory of Everything.'
    )
    line = 'Last wiki update: ' + body
    banner_text = (
        f'v15.03 retained · scientific_breakthrough: false · Pillar 3 open · '
        f'v15.03 release compile date {compile_d} · last X 2026-09-24 · v15.45 operator visualized · '
        f'Last wiki update {latest} (wiki main {short}, {iso}; WetLabEngine main {wet}; '
        f'research tip {tip}, {where}) · Not a completed Theory of Everything'
    )
    return {
        'schema': 'retained-atlas.freshness/v1',
        'role': 'Generated landing-page clock. Not a claim, not STATUS.md, and not the v15.03 release compile date.',
        'scientific_breakthrough': False,
        'pillar_3': 'open',
        'compile_date': compile_d,
        'compile_label': 'v15.03 release compile date',
        'latest_progress_entry': latest,
        'wiki_main_sha': sha,
        'wiki_main_short': short,
        'wiki_main_commit': iso,
        'wetlab_main': wet,
        'wetlab_main_sha': wet_full,
        'research_tip': tip,
        'research_tip_sha': tip_full,
        'research_branch': branch,
        'research_not_on_main': not_main,
        'date_modified': iso,
        'line': line,
        'meta': line,
        'banner': banner_text,
        'progress_path': '/progress.jsonl',
        'llms_path': '/llms.txt',
    }

def fill_marker(text, name, body):
    start, end = f'<!-- freshness:{name}:start -->', f'<!-- freshness:{name}:end -->'
    block = start + '\n' + body.rstrip('\n') + '\n' + end
    pat = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.S)
    if pat.search(text):
        return pat.sub(lambda m: block, text, count=1)
    raise SystemExit(f'freshness: missing marker {name}')

def replace_prefixed(text, prefix, newline):
    pat = re.compile(rf'^{re.escape(prefix)}.*$', re.M)
    if pat.search(text):
        return pat.sub(newline, text, count=1), True
    return text, False

def canonicalize_cite(cite, compile_d):
    """One citation sentence and one required-pieces bullet.

    An earlier substitution matched the bare words ``compile date (DATE)``
    inside a bullet that already began ``v15.03 release compile date``.
    The unmatched prefix stayed, so every regeneration appended another
    ``v15.03 release``. Both patterns below consume every repeated prefix
    and write exactly one. A second call returns the same text.
    """
    sentence = f"Retained Atlas. v15.03 release compile date {compile_d}."
    cite, n_sentence = re.subn(
        r'Retained Atlas\. (?:(?:v15\.03 release )+compile date|Compiled) \d{4}-\d{2}-\d{2}\.',
        sentence,
        cite,
        count=1,
    )
    if n_sentence != 1:
        raise SystemExit('freshness: cite.txt citation sentence not found')
    bullet = f"- v15.03 release compile date ({compile_d})"
    cite, n_bullet = re.subn(
        r'^- (?:v15\.03 release )*compile date \(\d{4}-\d{2}-\d{2}\)\s*$',
        bullet,
        cite,
        count=1,
        flags=re.M,
    )
    if n_bullet != 1:
        raise SystemExit('freshness: cite.txt required-pieces compile-date bullet not found')
    if cite.count(bullet) != 1:
        raise SystemExit('freshness: cite.txt compile-date bullet is not unique')
    if 'v15.03 release v15.03 release' in cite:
        raise SystemExit('freshness: cite.txt still repeats the v15.03 release prefix')
    return cite

def apply(f=None):
    os.chdir(ROOT)
    f = f or facts()
    public = {k: v for k, v in f.items() if k != 'banner'}
    os.makedirs('docs/data', exist_ok=True)
    json.dump(public, open('docs/data/freshness.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open('docs/data/freshness.json', 'a', encoding='utf-8').write('\n')

    # Banner. The three protected phrases stay word for word.
    banner = open('overrides/main.html', encoding='utf-8').read()
    new_banner = re.sub(
        r'\{% block announce %\}.*?\{% endblock %\}',
        '{% block announce %}' + f['banner'] + '{% endblock %}',
        banner, count=1, flags=re.S)
    if new_banner == banner and f['banner'] not in banner:
        raise SystemExit('freshness: announce block not found in overrides/main.html')
    for phrase in ('scientific_breakthrough: false', 'Pillar 3 open', 'Not a completed Theory of Everything', 'Last wiki update'):
        if phrase not in new_banner:
            raise SystemExit(f'freshness: banner lost "{phrase}"')
    open('overrides/main.html', 'w', encoding='utf-8').write(new_banner)

    idx = open('docs/index.md', encoding='utf-8').read()
    idx = re.sub(r'^description:.*$', 'description: ' + json.dumps(f['meta'], ensure_ascii=False), idx, count=1, flags=re.M)
    if re.search(r'^date_modified:', idx, re.M):
        idx = re.sub(r'^date_modified:.*$', 'date_modified: ' + json.dumps(f['date_modified'], ensure_ascii=False), idx, count=1, flags=re.M)
    else:
        idx = idx.replace('description: ' + json.dumps(f['meta'], ensure_ascii=False) + '\n',
                          'description: ' + json.dumps(f['meta'], ensure_ascii=False) + '\n'
                          + 'date_modified: ' + json.dumps(f['date_modified'], ensure_ascii=False) + '\n', 1)
    links = 'Progress: [/progress.jsonl](progress.jsonl) · [/llms.txt](llms.txt)'
    home = (
        f"@aaronspradlin · v15.03 release compile date {f['compile_date']}\n\n"
        f"Last wiki update\n:   {f['line']}\n\n"
        f"{links}\n"
    )
    idx = fill_marker(idx, 'home', home)
    idx = re.sub(r'(^Wiki compile\n:   ).*$', r'\g<1>v15.03 release compile date ' + f['compile_date'], idx, count=1, flags=re.M)
    clocks = (
        'Last wiki update\n'
        f":   {f['line']}\n\n"
        f"{links}\n\n"
        'Separate from the v15.03 release compile date above, the last X field note, and GitHub STATUS.md. Not a STATUS gate.'
    )
    idx = fill_marker(idx, 'clocks', clocks)
    counts = re.search(r'(\d+ wiki · \d+ packages · \d+ spine · \d+ notebook)', idx)
    counts = counts.group(1) if counts else '85 wiki · 74 packages · 139 spine · 195 notebook'
    footer = (
        f"v15.03 release compile date {f['compile_date']} · last X 2026-09-24 · Last wiki update {f['latest_progress_entry']} · {counts}\n\n"
        f"{counts} · v15.03 release compile date {f['compile_date']} · Last wiki update {f['latest_progress_entry']}"
    )
    idx = fill_marker(idx, 'footer', footer)
    open('docs/index.md', 'w', encoding='utf-8').write(idx)

    yml = open('mkdocs.yml', encoding='utf-8').read()
    copyright = (
        f"v15.03 release compile date {f['compile_date']} from @aaronspradlin and proteinfoldingengine/WetLabEngine. "
        f"Last wiki update {f['latest_progress_entry']}. Last ingested X 2026-09-24. "
        'Source-available for noncommercial research and evaluation only. '
        'No commercial, product, platform, or service use without written permission.'
    )
    yml2, n = re.subn(r'^copyright:.*$', 'copyright: ' + json.dumps(copyright, ensure_ascii=False), yml, count=1, flags=re.M)
    if n != 1:
        raise SystemExit('freshness: mkdocs.yml copyright line missing')
    open('mkdocs.yml', 'w', encoding='utf-8').write(yml2)

    llms = open('docs/llms.txt', encoding='utf-8').read()
    section = (
        '## Last wiki update (generated; not the wiki compile clock and not STATUS.md)\n\n'
        f"{f['line']}\n\n"
        f"{BASE}/progress.jsonl\n{BASE}/llms.txt\n{BASE}/data/freshness.json\n\n"
    )
    pat = re.compile(r'## Last wiki update \(generated.*?\n(?=## )', re.S)
    if pat.search(llms):
        llms = pat.sub(section, llms, count=1)
    elif '## Cite and license' in llms:
        llms = llms.replace('## Cite and license', section + '## Cite and license', 1)
    else:
        raise SystemExit('freshness: llms.txt has no place for the last wiki update section')
    open('docs/llms.txt', 'w', encoding='utf-8').write(llms)

    small = open('docs/llms-small.txt', encoding='utf-8').read()
    small_line = 'last_wiki_update: ' + f['line']
    small, ok = replace_prefixed(small, 'last_wiki_update: ', small_line)
    if not ok:
        small = small.replace('compile: ' + f['compile_date'] + '\n', 'compile: ' + f['compile_date'] + '\n' + small_line + '\n', 1)
        if small_line not in small:
            small = small.replace('scientific_breakthrough: false\n', 'scientific_breakthrough: false\n' + small_line + '\n', 1)
    open('docs/llms-small.txt', 'w', encoding='utf-8').write(small)

    c01 = open('docs/llms/c01-clocks.txt', encoding='utf-8').read()
    c01_line = 'Last wiki update (separate from the three clocks above; not a STATUS gate): ' + f['line']
    c01, ok = replace_prefixed(c01, 'Last wiki update (separate from the three clocks above; not a STATUS gate): ', c01_line)
    if not ok:
        anchor = 'If a search hit looks newer than STATUS.md, it is not current science.\n'
        if anchor not in c01:
            raise SystemExit('freshness: c01-clocks.txt anchor missing')
        c01 = c01.replace(anchor, anchor + '\n' + c01_line + '\n', 1)
    open('docs/llms/c01-clocks.txt', 'w', encoding='utf-8').write(c01)

    c09 = open('docs/llms/c09-retrieve.txt', encoding='utf-8').read()
    c09_line = 'Last wiki update (not the compile clock and not STATUS.md): ' + f['line']
    c09, ok = replace_prefixed(c09, 'Last wiki update (not the compile clock and not STATUS.md): ', c09_line)
    if not ok:
        anchor = 'Progress feed (chronological, append-only): '
        pos = c09.find(anchor)
        if pos < 0:
            raise SystemExit('freshness: c09-retrieve.txt progress line missing')
        end = c09.find('\n', pos)
        c09 = c09[:end + 1] + c09_line + '\n' + c09[end + 1:]
    open('docs/llms/c09-retrieve.txt', 'w', encoding='utf-8').write(c09)

    cite = open('docs/cite.txt', encoding='utf-8').read()
    cite = canonicalize_cite(cite, f['compile_date'])
    if canonicalize_cite(cite, f['compile_date']) != cite:
        raise SystemExit('freshness: cite.txt compile-date rewrite is not idempotent')
    cite_line = 'Last wiki update (not the compile date): ' + f['line']
    cite, ok = replace_prefixed(cite, 'Last wiki update (not the compile date): ', cite_line)
    if not ok:
        cite = cite.replace('Required pieces:\n', cite_line + '\n\nRequired pieces:\n', 1)
    open('docs/cite.txt', 'w', encoding='utf-8').write(cite)

    part = open('docs/wiki/ai-participate.md', encoding='utf-8').read()
    bullet = '- **Last wiki update is a separate label.** ' + f['line'] + ' It does not move a claim and it is not a STATUS.md gate.'
    part, n = re.subn(r'^- \*\*Last wiki update is a separate label\.\*\*.*$', bullet, part, count=1, flags=re.M)
    if n != 1:
        needle = "- **Don't merge clocks.**"
        if needle not in part:
            raise SystemExit('freshness: ai-participate.md clocks bullet missing')
        part = part.replace(needle, bullet + '\n' + needle, 1)
    open('docs/wiki/ai-participate.md', 'w', encoding='utf-8').write(part)

    tools = open('docs/tools.json', encoding='utf-8').read()
    clock = {
        'latest_progress_entry': f['latest_progress_entry'],
        'wiki_main_commit': f['wiki_main_commit'],
        'wiki_main': f['wiki_main_short'],
        'wetlab_main': f['wetlab_main'],
        'research_tip': f['research_tip'],
        'research_branch': f['research_branch'],
        'research_not_on_main': f['research_not_on_main'],
        'v15_03_release_compile_date': f['compile_date'],
        'note': 'Separate from the v15.03 release compile date, the last X note, and STATUS.md. Not a claim.',
        'line': f['line'],
    }
    encoded = json.dumps(clock, ensure_ascii=False, separators=(',', ':'))
    if '"last_wiki_update":' in tools:
        tools2, n = re.subn(r'"last_wiki_update":\{.*?\}(?=,?"status_md")', '"last_wiki_update":' + encoded, tools, count=1)
        if n != 1:
            raise SystemExit('freshness: tools.json last_wiki_update could not be replaced')
        tools = tools2
    else:
        tools = tools.replace('"clocks":{', '"clocks":{"last_wiki_update":' + encoded + ',', 1)
    open('docs/tools.json', 'w', encoding='utf-8').write(tools)

    cantos = open('docs/cantos.json', encoding='utf-8').read()
    sentence = json.dumps(f['line'], ensure_ascii=False)
    if '"last_wiki_update":' in cantos:
        cantos2, n = re.subn(r'"last_wiki_update":"(?:\\.|[^"\\])*"', '"last_wiki_update":' + sentence, cantos, count=1)
        if n != 1:
            raise SystemExit('freshness: cantos.json last_wiki_update could not be replaced')
        cantos = cantos2
    else:
        cantos = cantos.replace('"scientific_breakthrough":false,', '"scientific_breakthrough":false,"last_wiki_update":' + sentence + ',', 1)
    open('docs/cantos.json', 'w', encoding='utf-8').write(cantos)
    print('freshness:', f['latest_progress_entry'], f['wiki_main_short'], f['wiki_main_commit'], 'wetlab', f['wetlab_main'], 'research', f['research_tip'])

if __name__ == '__main__':
    apply()
