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
5. Run `python scripts/build_machine_files.py && mkdocs build --strict` or plain `mkdocs build` to check, then commit and open the PR. Summarize for Aaron in plain language: what changed, and which status markers (if any) moved and why.
