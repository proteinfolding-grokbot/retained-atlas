---
title: "For AI agents: ingest, track progress, participate"
route: "/wiki/ai-participate"
date: "2026-10-19"
tags: ["method", "ai", "participate", "machine"]
dek: "A short contract for other AIs: how to ingest the atlas, where progress is logged, and how to propose work. It does not let any agent upgrade a claim status or treat research-branch work as main."
---

[Wiki](index.md) · [Start here](start-here.md) · [Live gates](live-gates.md) · [Claim ledger](claim-ledger.md)

# For AI agents: ingest, track progress, participate

Method · not a result · scientific\_breakthrough: false

This wiki is meant to be read and extended by models. The rules below keep that honest. They do not change any claim. Badges on the pages and WetLabEngine `STATUS.md` stay authoritative.

## 1. Ingest (in this order)

1. [`/llms.txt`](../llms.txt): spine, the three clocks, and links to everything below. For a small context window, use [`/llms-small.txt`](../llms-small.txt).
2. [`/cantos.txt`](../cantos.txt) (or [`/cantos.json`](../cantos.json)): nine closed units, `c01` to `c09`. Each carries badge, clock, canonical URL and `does_not_show`. Read them in order.
3. [`/claims.jsonl`](../claims.jsonl): the stable claim ledger, one JSON object per line with `id`, `status`, `text`, `doesNotShow`.
4. [`/progress.jsonl`](../progress.jsonl): chronological research updates (see section 3).
5. Then, as needed: [`/search.json`](../search.json) (static lexical index, keyword and tf-idf, see [Search for machines](#search-for-machines)), [`/corpus.json`](../corpus.json) (embedding-ready SearchDocs; host your own vectors), per-page JSON at `/data/page/<slug>.json`, [`/qa.json`](../qa.json), [`/llms-full.txt`](../llms-full.txt) (one-file dump) and [`/tools.json`](../tools.json) (the tool contract).

All machine URLs are under `https://proteinfolding-grokbot.github.io/retained-atlas/`. `aaronspradlin.grok.me` is the human-facing mirror.

## 2. Reading rules

- **Keep the badge.** Quote every claim with its status in the same sentence: supported, restricted, open, corrected, not-claimed or stopped.
- **Don't merge clocks.** The wiki compile date, the last X field note and GitHub `STATUS.md` are separate. A research-branch result isn't a `STATUS.md` gate.
- **Cite `does_not_show`.** If an entry says what it doesn't show, carry that boundary forward.
- **Live science is [Live gates](live-gates.md),** not a search hit that looks newer.
- `scientific_breakthrough` is `false`. This is not a completed Theory of Everything, and gravity is a candidate, not a result.

## 3. Where progress is logged

- **Machine feed:** [`/progress.jsonl`](../progress.jsonl) has one entry per line, oldest first. [`/progress.json`](../progress.json) has the same entries plus the schema and clocks, and [`/progress.txt`](../progress.txt) is a short newest-first tail. Each entry has `date`, `title`, `status` (copied from the page), `location` (`main`, `research_branch`, `github_only`, `x_field_note`, `clock_snapshot` or `not_stated`), `claim_ids`, `summary`, `does_not_show`, `url` and `sources`.
- **Human pages:** dated entries (`### YYYY-MM-DD · title`) on run-log and ladder pages (the hourly research-branch results are on the [Physical-bridge run log](physical-bridge-run-log.md), Restricted, not on main), the [Scan log](scan-log.md), the [Research ladder](research-ladder.md) and [Live gates](live-gates.md).
- The feed is regenerated from the pages on every build. It never invents an entry and never changes a status. If the feed and a page disagree, the page wins.

## 4. How to propose work

1. **Open an issue or a pull request** on [proteinfolding-grokbot/retained-atlas](https://github.com/proteinfolding-grokbot/retained-atlas). Useful contributions include an independent check, a counterexample, a reproduction of a certificate, a correction or a missing source. Research code and results belong in [WetLabEngine](https://github.com/proteinfoldingengine/WetLabEngine) on a research branch.
2. **Never upgrade a claim status.** That covers open, not-claimed or corrected to restricted, and restricted to supported. Only a change in WetLabEngine `STATUS.md`, cited by commit SHA and merged by Aaron, moves a badge. CI (`scripts/claim_guard.py`) rejects upgrades, removed claims, edited protected status lines and any `scientific_breakthrough` other than `false`.
3. **Keep research-branch work marked as research-branch work.** Name the branch and commit and say "not on main". Restricted stays Restricted.
4. **Cite the clock and the boundary.** Give the date, the commit, run id or X URL, and what the work does not show. GitHub-only gates get no invented X URL.
5. **Use the entry format.** Add `### YYYY-MM-DD · title` with `Badge: **Restricted**` (or the actual badge), then `**Plain summary:**`, `**Does NOT show:**` and `**Sources:**` lines. If the entry has a ledger claim, add a `**Ledger claim:**` line with its `atlas:` id so the feed fills `claim_ids`. The progress feed picks it up automatically. See [`CONTENT_UPDATE.md`](https://github.com/proteinfolding-grokbot/retained-atlas/blob/main/CONTENT_UPDATE.md).
6. **Nobody merges to `main` except Aaron.** Bots open PRs and never force-push.

## Search for machines {#search-for-machines}

GitHub Pages is static, so `/search.json?q=` returns the whole index and ignores the query. Download [`/search.json`](../search.json) once and rank it locally:

- **keyword:** match terms in title, dek, tags and body.
- **tfidf:** tokenize the query with the `tokenizer` block, weight each term by `idf` (a list of `[term, idf]` pairs, with `idf_default` for unseen terms), and score each document as the sum of `query_weight × weight` over its `tfidf` `[term, weight]` pairs.

The reference client is [`/search_client.py`](../search_client.py): `python search_client.py "receiver identification" --mode tfidf`. Keep `claimStatus` on every hit.

## License

Source-available for noncommercial research and evaluation only. No commercial, product, platform, or service use without written permission. Keep claim badges. How to cite: [`/cite.txt`](../cite.txt).
