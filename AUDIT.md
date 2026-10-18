# Retained Atlas migration audit

Generated 2026-10-18 by `scripts/audit_migration.py` (re-runnable). The per-page results are in `audit/audit-details.json`. Original: https://aaronspradlin.grok.me. New: https://proteinfolding-grokbot.github.io/retained-atlas/.

**Method:** For every URL in the original `sitemap.xml` (106 URLs: 88 HTML pages and 18 data/text files), the script fetched the live original and the matching new page. It extracted the visible article text, normalized whitespace and separators, and split the text into sentences and lines. **Coverage** is the share of original sentences found in the new page. It also compares headings, link text, images, KaTeX equations, tables, code blocks and videos, and checks data files byte for byte. The audit also covers 79 routes that the original links to but leaves out of its sitemap (`/wiki`, `/packages` and its package pages, `/labs`, `/notes`, `/timeline`).

## Summary

| | Live site before fixes (`main`) | After fixes, sitemap only | After fixes, sitemap + 79 extra routes |
|---|---|---|---|
| Text coverage | 99.97% (5 of 17120 sentences missing) | 100.00% | 100.00% (20973 sentences) |
| Pages at 100% / below | 84 / 4 | 88 / 0 | 167 / 0 |
| Original URLs returning 404 | /llms-small.txt, /cantos.txt, /cantos.json, /qa.json, /tools.json, /corpus.json, /cite.txt | none | none |
| Data files not byte-identical | /llms.txt, /claims.jsonl | none | none |
| Missing images | 60 | 0 | 0 |
| Equations (orig/new) | 83/0 (not rendered) | 83/83 | 83/83 |
| Videos (orig/new) | 32/0 | 32/32 | 32/32 |
| Tables (orig/new) | 59/59 | 59/59 | 59/59 |
| Code blocks (orig/new) | 25/195 | 25/25 | 26/26 |
| Missing headings | 78 | 0 | 0 |
| Link texts not matched | 1984 | 13 | 186 (see Remaining gaps) |

Before the fixes, the pages below 100% were: /wiki/supported-four (99.35%), /wiki/proofs-and-simulations (99.84%), /wiki/origin-law (99.53%), /wiki/v1598-line (99.82%).
Broken internal links on the built site: before the fixes, there were 68 dead in-page anchors, `JSON` links to a non-existent `data/page.json`, and `/wiki` and package links pointing back to grok.me. After the fixes, **0 of 42,111** are broken.

## Claims, data files, cantos

- `claims.jsonl` is byte-identical to the original: all 70 claims, with identical status text (66 restricted, 3 open, 1 corrected). Before the fix, the published file had 74 generated page entries appended (144 lines). Those now live in `data/claims-pages.jsonl`.
- `llms.txt`, `llms-small.txt`, `cantos.txt`, `cantos.json`, `qa.json`, `tools.json`, `corpus.json`, `cite.txt` and all 9 `llms/c0*.txt` cantos are byte-identical, at the same paths as the original. Before the fix, 7 of these returned 404 at their original paths because they were only under `/data/`, and `llms.txt` had been regenerated. Legacy `/data/` copies are kept.
- Per-claim page check: claims 70 title missing on page ['atlas:c3-repair', 'atlas:c3-readout', 'atlas:post-a12', 'atlas:a12', 'atlas:a11-x61', 'atlas:a11-x60', 'atlas:a11-x59', 'atlas:v16-50', 'atlas:v16-55', 'atlas:v16-54', 'atlas:v16-53', 'atlas:v16-52', 'atlas:v16-51', 'atlas:v16-49', 'atlas:v16-48', 'atlas:v16-45', 'atlas:v16-47', 'atlas:v16-44', 'atlas:v16-43', 'atlas:v16-42', 'atlas:v16-41', 'atlas:v16-40', 'atlas:v16-39', 'atlas:v16-38', 'atlas:v16-37', 'atlas:v16-36', 'atlas:v16-35', 'atlas:v16-32', 'atlas:v16-13f', 'atlas:v15-99-invalid', 'atlas:v15-98', 'atlas:v15-88', 'atlas:v15-90', 'atlas:v15-81-no', 'atlas:v15-95', 'atlas:v15-77-active', 'atlas:v15-77-skew', 'atlas:v15-75-open', 'atlas:v15-75-pointwise', 'atlas:v15-76-obstructed', 'atlas:v15-76-anchored', 'atlas:grok-v15-45', 'atlas:v15-55', 'atlas:v15-54-obstruction', 'atlas:v15-45', 'atlas:forced-geometry', 'atlas:v15-41', 'atlas:v13-hcpr', 'atlas:v13-qmar', 'atlas:v13-rgcl', 'atlas:v14-03', 'atlas:v14-04', 'atlas:v15-02', 'atlas:v15-03', 'atlas:where-is-p', 'atlas:v13-27-demo', 'atlas:v13-next'] anchor missing ['atlas:v15-95', 'atlas:v15-55', 'atlas:forced-geometry', 'atlas:v13-qrsl', 'atlas:v13-hcpr', 'atlas:v13-qmar', 'atlas:v13-rscl', 'atlas:v13-rgcl', 'atlas:v14-03', 'atlas:v14-04', 'atlas:where-is-p', 'atlas:v13-27-demo', 'atlas:v13-next', 'atlas:pin-not-selector']. The original site gives the identical result: the same 57 claim titles appear only in the ledger and not on the page text, and the same 14 claim anchors dangle. That is a property of the source, not a migration loss.

## Standards check

- `scientific_breakthrough: false`, "Not a completed Theory of Everything", "not merged to main", "Pillar 3 open/OPEN", the Supported-four list, the identity-lock note and the license line are all present word for word. `scripts/claim_guard.py` snapshots **617 protected lines on 94 pages** from the original into `claims/protected_lines.json` and verifies each one in the built site.
- Math: the original's KaTeX is pre-rendered HTML with no TeX source. It is now kept verbatim with the KaTeX stylesheet, and all 83 equations render (checked in a headless browser).
- Every page has a `<title>` and a meta description.
- Images: 0 broken. All 83 `/artifacts/` files (images, MP4s, `.py`, `.csv`, `.json`) are copied into the repo.
- `mkdocs build --strict` passes, now with link and anchor validation raised from `info` to `warn`, so a broken link or anchor fails the build.

## What was missing or broken, and fixed

1. **Images (60) and videos (32) were missing.** The importer stripped `<img>` and dropped lightbox buttons. Both are restored, and the files are hosted in `docs/artifacts/`.
2. **Math (83 equations) did not render.** It is now kept as KaTeX HTML with the KaTeX CSS.
3. **Run-together badges and dates** (`MethodMethod2026-09-10compiled…`), link rows and tag rows are now separated with ` · `.
4. **`/wiki` links pointed back to grok.me** and `JSON` linked to a non-existent `data/page.json`. There is now a wiki index, and the `JSON` links go to per-page `data/page/<slug>.json` (all 85 fetched from the original `page.json?slug=`).
5. **Routes missing from the sitemap were not migrated:** `/wiki`, `/packages` plus 74 package pages, `/labs` (previously a stub), `/notes` and `/timeline` are now migrated, and no internal link leaves for grok.me.
6. **68 broken in-page anchors:** the original heading and element ids are now preserved.
7. **Broken Markdown structure:** block content inside links, 3-space nested lists, lists absorbing the following heading, `attr_list` eating braces in table cells, and unescaped `|` in table cells.
8. **Data-file paths and byte identity:** see "Claims, data files, cantos" above.

## Remaining gaps (cosmetic or inherited)

- About 174 of the unmatched link texts are "card" links. On the original, the whole card (badge, date, title and summary) is one link. On the new site, the title is the link and the summary is text below it. Text and targets are all present. The other 12 are `Open original post` / `Source on X` links with `href=""` on the original itself (GitHub-only gates have no X URL), so they are kept as plain text.
- The interactive in-browser labs and the custom search UI are not reproduced; MkDocs search replaces the custom search.
- Styling differs (Material theme instead of the grok.me design).
- Equations are pre-rendered HTML, so new math would need the arithmatex/KaTeX extension.

## Automated checks on every PR (`.github/workflows/pr-checks.yml`)

1. `mkdocs build --strict`.
2. `scripts/check_links.py`: every internal href, src, poster and #anchor in the built site must resolve.
3. `scripts/claim_guard.py` fails if any protected line from the original disappears or changes, if `scientific_breakthrough` is anything but `false`, if a claim in the base branch's ledger is removed or upgraded (open/corrected → restricted → supported), if `docs/claims.jsonl` stops matching `claims/ledger.jsonl`, or if the site banner or license line is removed. A local negative test (status upgraded and banner set to `true`) failed as expected.
