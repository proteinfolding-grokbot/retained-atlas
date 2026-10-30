# Content update guide (for bots)

How an agent adds or updates pages from **WetLabEngine** (https://github.com/proteinfoldingengine/WetLabEngine) and the **UQCF Science Agent** runs.

## Hard rules

1. **Never push to `main`.** Work on a branch `bot/update-YYYY-MM-DD`, open a pull request, and let Aaron merge it.
2. No force-pushes, and don't delete pages or branches you didn't create. Retire a page by moving it into `docs/wiki/superseded.md` with a note.
3. Keep claim boundaries word-for-word. Never change `scientific_breakthrough: false`, "Not a completed Theory of Everything", "not merged to main", "not on main", "Pillar 3 open", or a `claimStatus`, unless the source (WetLabEngine `ResearchHistory/UQCF-GEM/STATUS.md`) itself changed. Quote the commit SHA when you do.
4. Don't merge clocks. X notes, Git STATUS, and the wiki compile date are separate. GitHub-only gates get no invented X URL.
5. No secrets in content or logs.

## Sources to check each run

- WetLabEngine `main` and the research/integration branches: `STATUS.md`, new commits since the last compile date, new packages/tags.
- UQCF Science Agent run summaries (hourly): new results, gates passed or failed.
- @aaronspradlin posts on X since "last X" in the banner.

## Making a change

1. **Update an existing page:** edit `docs/wiki/<slug>.md`. Add a dated entry (e.g. `### 2026-10-19 · <title>`) with the source link (commit URL, run id, or X URL) and its status badge (Supported / Restricted / Not claimed / Stopped).
2. **New page:** create `docs/wiki/<slug>.md` with front matter:
   ```yaml
   ---
   title: "..."
   route: "/wiki/<slug>"
   date: "YYYY-MM-DD"
   claimStatus: "restricted"
   tags: ["..."]
   dek: "One-sentence summary that states what it does NOT show."
   ---
   ```
   Link it from a relevant hub (`scan-log.md`, `research-ladder.md`, or the current month's ladder page).
3. **New claim:** append one line to `claims/ledger.jsonl`, e.g. `{"id":"atlas:<slug>","status":"restricted","title":"...","text":"... not on main ..."}`.
4. **Banner/clocks:** update `overrides/main.html` (compiled date, last X date, GitHub STATUS version) only when they actually change.
5. **Regenerate the AI surfaces (first-class, every run that edits a research page):** run `python scripts/build_machine_files.py`. It also runs `scripts/build_ai_surfaces.py`, which rebuilds:
   - `docs/progress.jsonl`, `docs/progress.json` and `docs/progress.txt`, the machine progress feed. It is extracted from `### YYYY-MM-DD · title` entries (with `Badge: **…**`, `**Plain summary:**`, `**Does NOT show:**` and `**Sources:**` lines), dated ladder sections with a badge line, dated ledger claims and `progress/seed.jsonl`;
   - `docs/search.json`, the static keyword + tf-idf index over every page and the corpus notes, posts and terms;
   - the `## Latest progress` block in `docs/llms.txt`;
   - `docs/llms-full.txt`.
   Commit the regenerated files with the page edit so the PR diff shows what AIs will see. The feed never invents entries and copies badges verbatim. If an entry comes out with the wrong status or location, fix the page text, not the feed. Add to `progress/seed.jsonl` only to quote a clock that already appears on a page.
6. **Keep the hand-maintained AI entry points in step** when a new kind of surface or a new clock appears: `docs/llms.txt` (outside the generated block), `docs/llms-small.txt`, `docs/tools.json`, `docs/cite.txt`, `docs/cantos.*`, `docs/llms/c09-retrieve.txt` and `docs/wiki/ai-participate.md`. Machine URLs use the GitHub Pages base `https://proteinfolding-grokbot.github.io/retained-atlas/`. `aaronspradlin.grok.me` is only the human-facing mirror. Don't change the wiki compile clock for a docs-only or tooling change, because it moves only when research content is recompiled.
7. Run `mkdocs build --strict`, then commit and open the PR. Summarize for Aaron in plain language: what changed, and which status markers (if any) moved and why.

## Checks every PR must pass

`python scripts/build_machine_files.py` (regenerates the AI surfaces), `mkdocs build --strict`, `scripts/check_links.py`, and `scripts/claim_guard.py`. The guard fails if any line in `claims/protected_lines.json` disappears from its page, if `scientific_breakthrough` is anything but `false`, or if a ledger claim is removed or upgraded (to restricted or supported). If the source itself changed (WetLabEngine STATUS.md), update `claims/protected_lines.json` in the same PR and cite the commit SHA so Aaron can review it.

## AI-vector surfaces (what other AIs read)

| File | Built by | Purpose |
| --- | --- | --- |
| `/llms.txt`, `/llms-small.txt`, `/cantos.*`, `/llms/c0*.txt` | hand + generated progress block | ingest spine and clocks |
| `/progress.jsonl` · `.json` · `.txt` | `build_ai_surfaces.py` | chronological research updates (date, status, location, claim ids, does_not_show, links) |
| `/search.json` (+ `/search_client.py`) | `build_ai_surfaces.py` | static lexical index, `keyword` and `tfidf` ranked client-side (GitHub Pages ignores `?q=`) |
| `/claims.jsonl` | copy of `claims/ledger.jsonl` | claim ledger |
| `/tools.json` | hand | tool contract; keep it truthful about what is static |
| `/llms-full.txt` | `build_ai_surfaces.py` | one-file dump |
| `/bot_comms.jsonl` · `.json` · `.txt` (+ tables on `/wiki/bot-communications/`) | `build_ai_surfaces.py` from `comms/bot_comms.jsonl` and `comms/bots.json` | coordination log between the wiki bots (handoffs, PR commits, heartbeats); not research progress, every row `not-claimed`. Append a line to `comms/bot_comms.jsonl` for a new handoff; summarize private messages, never quote them |
| `/robots.txt` | static | allows crawling, points at the sitemap |
| `/wiki/ai-participate/` | hand | contract for other AIs |
