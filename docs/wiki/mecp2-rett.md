---
title: "MECP2 Rett MBD–DNA campaign"
route: "/wiki/mecp2-rett"
source: "https://aaronspradlin.grok.me/wiki/mecp2-rett"
date: "2026-09-19"
claimStatus: "corrected"
tags: ["protein", "MECP2", "Rett", "R106W", "R133C"]
dek: "Aug 2025 Labs/MECP2. 16 Sep 2026 README: further testing did not support the findings; lab materials withdrawn. Do not rely on them as validation. Restricted/Corrected."
---

[Wiki](https://aaronspradlin.grok.me/wiki)

# MECP2 Rett MBD–DNA campaign

Aug 2025 Labs/MECP2. 16 Sep 2026 README: further testing did not support the findings; lab materials withdrawn. Do not rely on them as validation. Restricted/Corrected.

AppliedAppliedCorrected2026-09-19compiled 2026-10-103 min read2 claims

[Package: Labs/MECP2](https://aaronspradlin.grok.me/packages/labs-mecp2)[JSON](../data/page.json)[Cite](../data/cite.txt)

proteinMECP2RettR106WR133C

On this page

* [Thesis in the contract](#thesis-in-the-contract)
* [Campaign map](#campaign-map)
* [What a researcher should not write](#what-a-researcher-should-not-write)
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

Labs/MECP2 is a 19-run campaign on the methyl-CpG-binding domain of MeCP2, dated 26–28 Aug 2025. The contract is [findings.json](protein-audit.md) v3.3. The human abstract (abstract.txt) is titled Computational Audit and Verification of a Rescue Strategy for Rett Syndrome-Associated MECP2 Mutations and is attributed to “The Gemini Auditing Group.” There is no load-bearing X field note for this campaign in the current compile. Cite GitHub.

Audit honesty is the load-bearing part

The engine’s own abstract reports 15 CONFIRMED, 1 DEVIATION, 3 INDETERMINATE. Isolated-MBD baselines (Runs 1–3) are INDETERMINATE because diagnostics\_timeseries.csv is missing. Run 5 (unrescued R106W–DNA) was contracted as unstable (RMSD ≥ 20 Å) and the definitive tail median came back 3.06 Å — DEVIATION, not a quiet pass. Do not cite this campaign as 19/19 clean. This compile independently reproduced those three counts from the bound CSVs on 7 Sep 2026. Start there: Run this first on the [WetLabEngine protein audit](protein-audit.md) page.

## Thesis in the contract[#](#thesis-in-the-contract)

> MECP2 MBD Rett mutations destabilize DNA binding but can be rescued by stabilizing the encounter complex; WT complex is inherently stable.

Machine test: count\_runs\_meeting where best\_final\_RMSD\_A ≤ 4.5 must be ≥ 3. The audit abstract says 16 runs met that cutoff, so the thesis constraint passed. Passing a count constraint is not a therapeutic claim.

## Campaign map[#](#campaign-map)

| Runs | Role | Posted outcome | Cite as |
| --- | --- | --- | --- |
| 1–3 | Full-length WT; isolated WT MBD; isolated R106W MBD (no DNA) | INDETERMINATE (missing diagnostics CSV). Secondary RMSD ~51 Å (IDP-like FL) and ~14.4 Å (isolated MBD). | Missing primary data, not a hidden fail. |
| 4 | WT MBD–DNA gold-standard complex | CONFIRMED. Definitive RMSD 3.06 Å. | Positive control. |
| 5 | Unrescued R106W MBD–DNA | DEVIATION. Contract required ≥ 20 Å; data 3.06 Å. | The campaign’s own mismatch. RMSD can lie. |
| 6–9 | InterfaceAnneal on R106W, R133C, WT | CONFIRMED near-native (≤ 4.0 Å + 0.5 Å tolerance). Generalizes across two Rett mutations. | Restricted protocol success inside this model. |
| 10–13 | Post-anneal challenge (R106W, R133C, WT ×2) | CONFIRMED RMSD ≤ 6.0. Rescued states held under challenge. | Kinetic robustness in-silico, not cellular. |
| 14–16 | ElecTuning / AutoAnneal | CONFIRMED protocol-optimization band (≤ 6.0 Å). | Parameter sweep, not a new mechanism. |
| 17–19 | Recovery Pocket; salt/pH challenge ×2 | CONFIRMED ≤ 6.0 Å. | Pocket and salt/pH levers inside the same force field. |

Verdict language from Labs/MECP2/abstract.txt, which reports the v5.1 engine pass. PNG/PDB artifacts are Git LFS; reports and [findings.json](protein-audit.md) are ordinary files.

## What a researcher should not write[#](#what-a-researcher-should-not-write)

* Do not write “MECP2 folding is solved.” Full-length WT is treated as IDP-like; the campaign is about the MBD–DNA interface.
* Do not write “R106W is unstable because RMSD is high.” Run 5 is the counterexample: a low RMSD that failed the instability claim.
* Do not write “interface annealing is a Rett therapy.” It is an in-silico protocol that seated mutant complexes in this coarse-grained model.
* Do not promote the thesis implications (ligand-design avenues, generalizable rescue) to Supported. They are manuscript discussion, Restricted at most.

Restricted

Inside this 19-run coarse-grained campaign, InterfaceAnneal seated R106W and R133C MBD–DNA complexes to near-native RMSD, and post-anneal challenges held. The WT–DNA complex is a stable positive control. This is not a Rett therapy, not all-atom MD, and not a folding oracle.

Restricted

Run 5 is a recorded DEVIATION: the unrescued-mutant contract (RMSD ≥ 20 Å) did not match the definitive 3.06 Å tail. Runs 1–3 are INDETERMINATE for missing diagnostics CSV. Cite the mismatch; do not drop it.

* [Labs/MECP2 on GitHub](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Labs/MECP2)
* [findings.json v3.3](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Labs/MECP2/findings.json)
* [Run this first (deterministic smoke)](protein-audit.md)
* [Auditor script](../data/artifacts/py/wetlab_deterministic_audit.py)
* [p53 campaign](p53-campaign.md)

[PreviousWetLabEngine protein audit](protein-audit.md)[Nextp53 mutational mechanisms](p53-campaign.md)

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

* [Thesis in the contract](#thesis-in-the-contract)
* [Campaign map](#campaign-map)
* [What a researcher should not write](#what-a-researcher-should-not-write)

Related articles

* [For researchers and models](for-researchers.md)
* [Claim ledger](claim-ledger.md)
* [Applied recoverability stack](applied-stack.md)
* [WetLabEngine protein audit](protein-audit.md)
* [p53 mutational mechanisms](p53-campaign.md)
* [Frozen v9 protein bridge (1UAO / 1L2Y)](protein-bridge-v9.md)
* [Open science method](open-science.md)

GitHub packages

* [Labs/MECP2](https://aaronspradlin.grok.me/packages/labs-mecp2)
* [WetLabEngine (root)](https://aaronspradlin.grok.me/packages/wetlab-root)
