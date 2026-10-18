# Retained Atlas

Compiled research wiki of Aaron Spradlin (@aaronspradlin), rebuilt from the Grok-hosted original at https://aaronspradlin.grok.me (archived 2026-10-18) as a static MkDocs Material site published by GitHub Pages.

**Status (unchanged from the original):** v15.03 retained · `scientific_breakthrough: false` · Pillar 3 open · Not a completed Theory of Everything. Gravity is a candidate, not a result.

## Layout

| Path | What |
|---|---|
| `docs/index.md` | Home page |
| `docs/wiki/*.md` | Wiki pages, one per original `/wiki/<slug>` route (same slug) |
| `docs/labs.md`, `docs/glossary.md`, `docs/search.md` | Other top-level pages |
| `docs/llms/*.txt` | The nine cantos (closed ingest units), copied verbatim |
| `docs/data/` | Original machine files: `corpus.json`, `cantos.*`, `qa.json`, `tools.json`, `cite.txt`, `search.json`, `llms-small.txt` |
| `claims/ledger.jsonl` | Source-of-truth claim ledger (one JSON object per line: `id`, `status`, `title`, `text`, ...) |
| `scripts/build_machine_files.py` | Regenerates `docs/data/llms-site.txt` and `docs/data/claims-pages.jsonl` from page front matter |
| `scripts/claim_guard.py` | CI: fails if a protected status line / claim boundary is removed or a claim is removed or upgraded |
| `scripts/check_links.py` | CI: internal link + anchor checker for the built site |
| `scripts/audit_migration.py` | Re-runnable completeness audit vs the original grok.me site (see AUDIT.md) |
| `scripts/import_archive.py` | One-time importer used for the migration (kept for provenance) |
| `overrides/main.html` | Site-wide status banner |
| `.github/workflows/pages.yml` | Builds and deploys on every push to `main` |

Each page starts with YAML front matter: `title`, `route` (original URL path), `source`, and where known `date`, `claimStatus` (`supported` / `restricted` / `not-claimed` / ...), `tags`, `dek`.

## Build locally

```
pip install mkdocs-material "mkdocs<2"
python scripts/build_machine_files.py
mkdocs serve
```

`docs/llms.txt`, `docs/claims.jsonl` and the other root data files are byte-identical copies of the original site. `docs/claims.jsonl` must equal `claims/ledger.jsonl`; add claims to the ledger and copy it. `docs/data/llms-site.txt` and `docs/data/claims-pages.jsonl` are generated, so don't hand-edit them. Every PR runs `.github/workflows/pr-checks.yml`.

## Rules

- Claim boundaries and status markers are kept word-for-word. Don't promote `not-claimed` or `restricted` to a result.
- Bots open pull requests. Only Aaron merges to `main`. See `CONTENT_UPDATE.md`.

License: source-available for noncommercial research and evaluation only. No commercial, product, platform, or service use without written permission.
