---
title: "WetLabEngine protein audit"
route: "/wiki/protein-audit"
source: "https://aaronspradlin.grok.me/wiki/protein-audit"
date: "2026-09-19"
claimStatus: "restricted"
tags: ["protein", "audit", "biophysics", "Villin", "WetLabEngine"]
dek: "White-box science contract at the GitHub root. Engine is a Supported tool. Custom protein-mechanism program CLOSED 19 Sep 2026 on current evidence. Folding results stay Restricted/Corrected."
---

[Wiki](https://aaronspradlin.grok.me/wiki)

# WetLabEngine protein audit

White-box science contract at the GitHub root. Engine is a Supported tool. Custom protein-mechanism program CLOSED 19 Sep 2026 on current evidence. Folding results stay Restricted/Corrected.

AppliedAppliedRestricted2026-09-19compiled 2026-10-107 min read3 claims[6 X sources](#x-sources)

[Original on X](https://x.com/aaronspradlin/status/2044155484039705016)[Package: WetLabEngine (root)](https://aaronspradlin.grok.me/packages/wetlab-root)[JSON](../data/page.json)[Cite](../data/cite.txt)

proteinauditbiophysicsVillinWetLabEngine

On this page

* [Repository map](#repository-map)
* [The engine](#the-engine)
* [Run this first](#run-this-first)
* [Villin HP35 — the X result](#villin-hp35-the-x-result)
* [X ledger versus GitHub-only labs](#x-ledger-versus-github-only-labs)
* [Same pattern, other domains](#same-pattern-other-domains)
Causal stack

1. [00

   Astra / global consistency](astra.md)
2. [01

   Genesis Pin](genesis-pin.md)
3. [02

   Retained pruning-order history](causal-stack.md)
4. [03

   Admissible slice](causal-stack.md)
5. [04

   L1 (closed)](causal-stack.md)
6. [05

   L2 (closed)](causal-stack.md)
7. [06

   L3 hyperedge memory T\_H + D\_L3](causal-stack.md)
8. [07

   L4 H₄ rank lift](causal-stack.md)
9. [08

   Discrete atlas / scalar accessibility](retained-atlas.md)
10. [09

    GEM-bridge / gravity](emergent-gravity.md)

19 Sep 2026 — program CLOSED on current evidence

Author correction: computational signals were real; a distinct transferable new folding mechanism was not established. Final held-out transfer +~2.6% (p≈0.46) / −5.6% (p≈0.49). 16 Sep README: Labs/[p53](p53-campaign.md) and Labs/[MECP2](mecp2-rett.md) withdrawn — do not rely on them as validation. Reopen only for new independent evidence. Full note: /wiki/protein-closeout.

proteinfoldingengine/WetLabEngine is [Aaron Spradlin](aaron-spradlin.md)’s public working tree. The repository root is a white-box protein-simulation audit engine. Nested under Labs/ are two GitHub-only coarse-grained campaigns ([p53](p53-campaign.md), [MECP2](mecp2-rett.md)). Nested under Tmp/TOE are the geometry-from-information packages this wiki already indexes, plus the April 2026 folding-side bridge packet on [1UAO](protein-bridge-v9.md) and [1L2Y](protein-bridge-v9.md). Villin HP35 [R\_t](uqcf-gem.md) is the X-posted controlled-case result. Those four protein objects are one research area only because they share an author, a science-contract style, and a GitHub tree — not because they share a proven law.

Do not mix the tool with the science

The engine can confirm or refute a numeric constraint in findings.json. That is a Supported tooling claim. [p53](p53-campaign.md), [MECP2](mecp2-rett.md), Villin HP35, and frozen [v9](protein-bridge-v9.md) on [1UAO](protein-bridge-v9.md)/[1L2Y](protein-bridge-v9.md) are Restricted in-silico results. None of them is a folding oracle, a cancer or [Rett](mecp2-rett.md) therapy, AlphaFold refuted, or a TOE confirmation.

## Repository map[#](#repository-map)

| Path | What it is | Wiki | Badge |
| --- | --- | --- | --- |
| / | UnifiedAuditEngine.py v5.7, SCHEMA.md (findings.json 2.2), ManuscriptBuilder.py, Colab notebook | protein-audit | supported (tool) |
| Labs/[p53](p53-campaign.md) | 12-run [p53](p53-campaign.md) DBD campaign, Aug 2025. [R248Q](p53-campaign.md) electrostatic vs [Y220C](p53-campaign.md) kinetic trap. | [p53](p53-campaign.md)-campaign | restricted |
| Labs/[MECP2](mecp2-rett.md) | 19-run [Rett](mecp2-rett.md) MBD–DNA campaign, Aug 2025. InterfaceAnneal rescue + honest DEVIATION on Run 5. | [mecp2](mecp2-rett.md)-[rett](mecp2-rett.md) | restricted |
| Tmp/TOE/uqcf\_bridge\_v9\_\* | Frozen [v9](protein-bridge-v9.md) bridge on [1UAO](protein-bridge-v9.md) and [1L2Y](protein-bridge-v9.md). Backbone-ordering, not full fold. Posted 12 Apr 2026. | protein-bridge-[v9](protein-bridge-v9.md) | restricted |
| X, 14 Apr 2026 | Villin HP35: identical snapshot, different fate from hidden [R\_t](uqcf-gem.md). Author tagged speculative. | protein-audit | restricted |
| Tmp/TOE/ | Geometry-from-information program (atlas, [holonomy](holonomy.md), SPARC, batteries). Already indexed. | program | mixed |
| retained-atlas-agent/ | Governor loop / constitution for atlas runs. Sibling tooling, not a folding result. | [c3](c3-governor.md)-governor | restricted |

Start at the root README. Labs/ PNG and PDB files are Git LFS; markdown reports, CSVs, and findings.json are in the ordinary tree. Tmp/TOE is a separate program that happens to live in the same repo.

## The engine[#](#the-engine)

WetLabEngine is an open-source audit engine for protein simulation campaigns. A JSON manifest (findings.json) defines experiments, human-readable claims, and machine-testable constraints (for example best\_final\_RMSD\_A ≤ 20.0). UnifiedAuditEngine.py (v5.7 in the current tree) checks those constraints against CSVs, PDBs, and images, then optionally sends artifacts to Gemini for qualitative review. Output is Biophysics\_Final\_Report.md plus machine-readable JSON. ManuscriptBuilder.py writes the prose body; the appendix is assembled deterministically from the verification report so the AI cannot rewrite the verdict table.

* Science contract: SCHEMA.md, findings.json v2.2 ([p53](p53-campaign.md)) / v3.3 ([MECP2](mecp2-rett.md)). Every metric in a constraint must be declared in metrics\_vocabulary.
* Deterministic verdicts: CONFIRMED, DEVIATION, INDETERMINATE. Tail-median RMSD from diagnostics\_timeseries.csv is the preferred single source of truth.
* AI peer review is qualitative and does not override the numeric verdict. Claim-integrity and cross-artifact triage are logged beside it.
* Thesis block: count\_runs\_meeting aggregation across the campaign. The engine can fail a thesis even if individual runs pass.
* License on the repo: CC BY-NC-SA 4.0, plus Spradlin’s later commercial-use restriction on the public research stream.

Minimal findings.json constraint (SCHEMA 2.2)

```
{
  "canonical_claim": {
    "type": "rescue_protocol",
    "statement": "Contact-anneal + PhiKan083 improves Y220C (RMSD ≤ 20 Å).",
    "constraints": [
      { "metric": "best_final_RMSD_A", "op": "<=", "value": 20.0 }
    ]
  }
}
```

Supported

As a tool: claims written into findings.json can be numerically confirmed or refuted against the bound raw artifacts. That is the engine’s job. It is not a folding oracle and not a TOE.

## Run this first[#](#run-this-first)

GitHub is the working copy. This page is the cheapest entry. Start with Labs/[MECP2](mecp2-rett.md), not Villin and not a new disease protein. The posted UnifiedAuditEngine.py is Colab-oriented: it hardcodes PROJECT\_NAME = [MECP2](mecp2-rett.md), clones ProteinFoldingEngine/Results-AI-Audit-Engine, looks for Projects/[MECP2](mecp2-rett.md)/findings.json, and exits if a Gemini key is missing. Do not expect python UnifiedAuditEngine.py to score Labs/[MECP2](mecp2-rett.md) as a local folder.

Two entries, one contract

Full engine (his README): Colab + API\_KEY.txt + Gemini qualitative review. Deterministic half (this atlas): a stdlib script that reads findings.json and tail-median RMSD from diagnostics\_timeseries.csv. PNG/PDB Git LFS files are not required. This compile ran the deterministic half on 7 Sep 2026. Gemini peer review was not rerun.

1. Clone only Labs/[MECP2](mecp2-rett.md). Skip git lfs pull — CSVs and findings.json are ordinary files.
2. Download wetlab\_deterministic\_audit.py from this page (Open source). It is a pedagogical reconstruction of verdict\_from\_constraint, not a dump of UnifiedAuditEngine.py.
3. python3 wetlab\_deterministic\_audit.py Labs/[MECP2](mecp2-rett.md)
4. Green: CONFIRMED 15, DEVIATION 1, INDETERMINATE 3, and smoke PASS on Run 5.
5. Optional: python3 wetlab\_deterministic\_audit.py Labs/[p53](p53-campaign.md) --no-smoke. Expect Run 9 INDETERMINATE if the ContactAnneal folder is missing.
6. To run his full engine, follow the repo README in Colab with a Gemini key. That path clones a different data repo.

Labs/MECP2 deterministic smoke

[Open source](../data/artifacts/py/wetlab_deterministic_audit.py)

```
git clone --depth 1 --filter=blob:none --sparse https://github.com/proteinfoldingengine/WetLabEngine.git
cd WetLabEngine
git sparse-checkout set Labs/MECP2
# put wetlab_deterministic_audit.py in this directory (download from this page), then:
python3 wetlab_deterministic_audit.py Labs/MECP2
```

Expected MECP2 output (this compile, 7 Sep 2026)

```
CONFIRMED 15   DEVIATION 1   INDETERMINATE 3
thesis count_runs_meeting (best_final_RMSD_A <= 4.5): 16 >= 3  PASS
smoke PASS: Run 5 is DEVIATION (tail-median RMSD 3.06 Å vs contracted ≥ 20 Å).
```

| Campaign | This compile | Load-bearing cell | What a green run does not show |
| --- | --- | --- | --- |
| Labs/[MECP2](mecp2-rett.md) | 15 CONFIRMED / 1 DEVIATION / 3 INDETERMINATE | Run 5 DEVIATION at 3.06 Å against ≥ 20 Å | Gemini rerun; [Rett](mecp2-rett.md) therapy; native folding |
| Labs/[p53](p53-campaign.md) | 11 CONFIRMED / 0 DEVIATION / 1 INDETERMINATE | Run 9 INDETERMINATE (ContactAnneal folder missing) | The manuscript’s 18.9 Å rescue independently re-read |

Stdlib tail-median of diagnostics\_timeseries.csv versus findings.json constraints. [MECP2](mecp2-rett.md) matches the campaign abstract. [p53](p53-campaign.md) matches Table 1 in order (WT/[R248Q](p53-campaign.md) 26.71 vs 26.6 Å; native-start 3.82 vs 4.0 Å) except Run 9, which this tree cannot score.

* Run 5 is the smoke test that the engine can fail a claim. If it comes back CONFIRMED, stop and inspect — do not drop the DEVIATION.
* Thesis count\_runs\_meeting can pass while a run-level claim fails: Run 5’s 3.06 Å still counts toward RMSD ≤ 4.5.
* dataset\_root in findings.json is a Colab path (/content/Results-AI-Audit-Engine/Projects/[MECP2](mecp2-rett.md)). The smoke script ignores it and resolves source\_folder under the campaign directory you cloned.
* Live /labs is a [recoverability](recoverability.md) toy. It is not this auditor.

Supported

This compile independently scored Labs/[MECP2](mecp2-rett.md)/findings.json against the bound diagnostics CSVs: 15 CONFIRMED, 1 DEVIATION (Run 5, 3.06 Å vs ≥ 20 Å), 3 INDETERMINATE. Thesis count\_runs\_meeting passed (16 ≥ 3). That is a tooling reproduction. It is not a Gemini rerun, not a [Rett](mecp2-rett.md) therapy, and not native folding.

## Villin HP35 — the X result[#](#villin-hp35-the-x-result)

On 14 Apr 2026 Aaron asked Grok to peer-review a Villin HP35 claim from the WetLabEngine pipeline. The posted numbers: two chains with identical visible conformation can still have different folding fates because of hidden retained history [R\_t](uqcf-gem.md). G\_t-only models miss it. Grok’s in-thread review treated the pipeline as working on controlled/sample cases. A 26 Apr follow-up used stronger AlphaFold language; this atlas keeps the 14 Apr speculative tag as the governing voice.

AUC(Gt​+Rt​)≈0.9569vsGt​ alone

> The ROC lift (AUC G\_t + [R\_t](uqcf-gem.md) ≈ 0.9569 vs G\_t alone) shows real predictive signal from [R\_t](uqcf-gem.md). The matched-state divergence (50.2 % far-[R\_t](uqcf-gem.md) vs 1.3 % close-[R\_t](uqcf-gem.md), +48.9 % spread) directly falsifies pure visible-state completeness.
>
> [@grok, 14 Apr 2026](https://x.com/grok/status/2044149250192212227)

> This is all speculative and they have better things to do for now then react to another one of the wild claims.
>
> [@aaronspradlin, 14 Apr 2026](https://x.com/aaronspradlin/status/2044155484039705016)

Restricted

On the posted Villin HP35 controlled cases, adding retained state [R\_t](uqcf-gem.md) lifts AUC and opens a matched-pair divergence gap versus G\_t-only. This is not a claim that AlphaFold is refuted, and it is not a folding oracle.

[Source on X](https://x.com/aaronspradlin/status/2044155484039705016)

## X ledger versus GitHub-only labs[#](#x-ledger-versus-github-only-labs)

| Date | Object | Where it lives | What to cite |
| --- | --- | --- | --- |
| 22–23 Aug 2025 | [p53](p53-campaign.md) DBD campaign (12 runs) | GitHub Labs/[p53](p53-campaign.md) — no load-bearing X field note in this compile | [p53](p53-campaign.md)-campaign + findings.json |
| 26–28 Aug 2025 | [MECP2](mecp2-rett.md) MBD–DNA campaign (19 runs) | GitHub Labs/[MECP2](mecp2-rett.md) — no load-bearing X field note in this compile | [mecp2](mecp2-rett.md)-[rett](mecp2-rett.md) + findings.json |
| 12 Apr 2026 | Frozen [v9](protein-bridge-v9.md) on [1UAO](protein-bridge-v9.md) / [1L2Y](protein-bridge-v9.md) | X thread + Tmp/TOE/uqcf\_bridge\_v9\_\* | protein-bridge-[v9](protein-bridge-v9.md) |
| 14 Apr 2026 | Villin HP35 [R\_t](uqcf-gem.md) | X, tagged speculative the same day | this page |
| 26 Apr 2026 | AlphaFold-never-solved restatement | X reply quoting the 14 Apr numbers | restricted restatement, not a promotion |
| 1 May 2026 | Critical-path recurrence including protein | X | applied-stack — recurrence, not a unification proof |
| 10 May 2026 | Work stays on X/GitHub; others free to use protein folding | X | open-science / method |

X is the archive of record for posted results. GitHub Labs/ campaigns that never became field notes are still part of the working tree and must be indexed honestly, not promoted to X-posted science.

## Same pattern, other domains[#](#same-pattern-other-domains)

The 1 May 2026 critical-path post treats protein folding, [fractal TSP](tsp-backbone.md), SPARC holdouts, and live project plans as rhyming [recoverability](recoverability.md) problems: preserve what remained coherent, deform what is stressed, reset only what went stale. Recurrence is not a unification proof. The 10 May question — what unifies proteins, [RCLC](hubble-tension.md), [critical path](critical-path.md), and [TSP](tsp-backbone.md) — is still open. The [C3++](c3-governor.md) governor is the LLM-side instrument of the same idea. The [applied recoverability stack](applied-stack.md) is the hub for those three Python labs.

* [p53 campaign (Labs/p53)](p53-campaign.md)
* [MECP2 Rett campaign (Labs/MECP2)](mecp2-rett.md)
* [Frozen v9 on 1UAO / 1L2Y](protein-bridge-v9.md)
* [Live protein lab](../labs.md)
* [Applied recoverability stack](applied-stack.md)
* [Deterministic auditor (this atlas)](../data/artifacts/py/wetlab_deterministic_audit.py)
* [UnifiedAuditEngine.py v5.7](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/UnifiedAuditEngine.py)
* [SCHEMA.md](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/SCHEMA.md)
* [WetLabEngine on GitHub](https://github.com/proteinfoldingengine/WetLabEngine)
* [Labs/p53](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Labs/p53)
* [Labs/MECP2](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Labs/MECP2)

## X sources

Original posts this article was compiled from. The notebook copy is editorial; the status URL is the source.

* 2026-09-19

  Protein-mechanism program CLOSED on current evidence

  [In the notebook](https://aaronspradlin.grok.me/notes#protein-closeout-2026-09-19)[Open original post](https://x.com/aaronspradlin/status/2101337128169034035)
* 2026-04-12

  Frozen v9 protein bridge on 1UAO / 1L2Y

  [In the notebook](https://aaronspradlin.grok.me/notes#bridge-v9-2026-04-12)[Open original post](https://x.com/aaronspradlin/status/2043198645147967753)
* 2026-04-14

  Villin HP35: identical snapshot, different fate

  [In the notebook](https://aaronspradlin.grok.me/notes#villin-2026-04-14)[Open original post](https://x.com/aaronspradlin/status/2044155484039705016)
* 2026-05-01

  Retained coherence in live critical path

  [In the notebook](https://aaronspradlin.grok.me/notes#critical-path-2026-05-01)[Open original post](https://x.com/aaronspradlin/status/2050029681517433047)
* 2026-03-25

  C3++ Stability Governor on Qwen3-4B

  [In the notebook](https://aaronspradlin.grok.me/notes#c3-2026-03-25)[Open original post](https://x.com/aaronspradlin/status/2036659106350792814)
* 2026-05-10

  What unifies proteins, RCLC, critical path, TSP

  [In the notebook](https://aaronspradlin.grok.me/notes#unify-domains-2026-05-10)[Open original post](https://x.com/aaronspradlin/status/2053553647712338040)

[PreviousProtein program closeout](protein-closeout.md)[NextMECP2 Rett MBD–DNA campaign](mecp2-rett.md)

Causal stack

1. [00

   Astra / global consistency](astra.md)
2. [01

   Genesis Pin](genesis-pin.md)
3. [02

   Retained pruning-order history](causal-stack.md)
4. [03

   Admissible slice](causal-stack.md)
5. [04

   L1 (closed)](causal-stack.md)
6. [05

   L2 (closed)](causal-stack.md)
7. [06

   L3 hyperedge memory T\_H + D\_L3](causal-stack.md)
8. [07

   L4 H₄ rank lift](causal-stack.md)
9. [08

   Discrete atlas / scalar accessibility](retained-atlas.md)
10. [09

    GEM-bridge / gravity](emergent-gravity.md)

On this page

* [Repository map](#repository-map)
* [The engine](#the-engine)
* [Run this first](#run-this-first)
* [Villin HP35 — the X result](#villin-hp35-the-x-result)
* [X ledger versus GitHub-only labs](#x-ledger-versus-github-only-labs)
* [Same pattern, other domains](#same-pattern-other-domains)

[X sources](#x-sources)

Related articles

* [The research program](program.md)
* [For researchers and models](for-researchers.md)
* [Recoverability geometry](recoverability.md)
* [Applied recoverability stack](applied-stack.md)
* [TSP coherence backbone](tsp-backbone.md)
* [New Critical Path](critical-path.md)
* [C3++ Stability Governor](c3-governor.md)
* [p53 mutational mechanisms](p53-campaign.md)
* [MECP2 Rett MBD–DNA campaign](mecp2-rett.md)
* [Frozen v9 protein bridge (1UAO / 1L2Y)](protein-bridge-v9.md)
* [X science notebook](x-notebook.md)
* [Open science method](open-science.md)
* [Protein program closeout](protein-closeout.md)

GitHub packages

* [WetLabEngine (root)](https://aaronspradlin.grok.me/packages/wetlab-root)
* [Labs/p53](https://aaronspradlin.grok.me/packages/labs-p53)
* [Labs/MECP2](https://aaronspradlin.grok.me/packages/labs-mecp2)
* [uqcf\_bridge\_v9\_update\_bundle](https://aaronspradlin.grok.me/packages/uqcf-bridge-v9-update-bundle)

Field notes

* [Protein-mechanism program CLOSED on current evidence](https://aaronspradlin.grok.me/notes#protein-closeout-2026-09-19)

  2026-09-19

  [On X](https://x.com/aaronspradlin/status/2101337128169034035)
* [Frozen v9 protein bridge on 1UAO / 1L2Y](https://aaronspradlin.grok.me/notes#bridge-v9-2026-04-12)

  2026-04-12

  [On X](https://x.com/aaronspradlin/status/2043198645147967753)
* [Villin HP35: identical snapshot, different fate](https://aaronspradlin.grok.me/notes#villin-2026-04-14)

  2026-04-14

  [On X](https://x.com/aaronspradlin/status/2044155484039705016)
* [Retained coherence in live critical path](https://aaronspradlin.grok.me/notes#critical-path-2026-05-01)

  2026-05-01

  [On X](https://x.com/aaronspradlin/status/2050029681517433047)
* [C3++ Stability Governor on Qwen3-4B](https://aaronspradlin.grok.me/notes#c3-2026-03-25)

  2026-03-25

  [On X](https://x.com/aaronspradlin/status/2036659106350792814)
* [What unifies proteins, RCLC, critical path, TSP](https://aaronspradlin.grok.me/notes#unify-domains-2026-05-10)

  2026-05-10

  [On X](https://x.com/aaronspradlin/status/2053553647712338040)
