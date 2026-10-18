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
| `scripts/build_machine_files.py` | Regenerates `docs/llms.txt` and `docs/claims.jsonl` from page front matter + the ledger |
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

`docs/llms.txt` and `docs/claims.jsonl` are generated; don't hand-edit them.

## Rules

- Claim boundaries and status markers are kept word-for-word. Don't promote `not-claimed` or `restricted` to a result.
- Bots open pull requests. Only Aaron merges to `main`. See `CONTENT_UPDATE.md`.

License: source-available for noncommercial research and evaluation only. No commercial, product, platform, or service use without written permission.
