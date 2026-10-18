---
title: "p53 mutational mechanisms"
route: "/wiki/p53-campaign"
source: "https://aaronspradlin.grok.me/wiki/p53-campaign"
description: "Aug 2025 Labs/p53. 16 Sep 2026 README: further testing did not support the findings; lab materials withdrawn. Do not rely on them as validation. Restricted/Corrected."
date: "2026-09-19"
claimStatus: "corrected"
tags: ["protein", "p53", "Y220C", "R248Q", "PhiKan083"]
dek: "Aug 2025 Labs/p53. 16 Sep 2026 README: further testing did not support the findings; lab materials withdrawn. Do not rely on them as validation. Restricted/Corrected."
---

[Wiki](index.md)

# p53 mutational mechanisms

Aug 2025 Labs/p53. 16 Sep 2026 README: further testing did not support the findings; lab materials withdrawn. Do not rely on them as validation. Restricted/Corrected.

Applied · Applied · Corrected · 2026-09-19 · compiled 2026-10-10 · 3 min read · 2 claims

[Package: Labs/p53](../packages/labs-p53.md) · [JSON](../data/page/p53-campaign.json) · [Cite](../cite.txt)

protein · p53 · Y220C · R248Q · PhiKan083

On this page

*   [Thesis in the contract](#thesis-in-the-contract)
*   [Twelve-run scoreboard](#twelve-run-scoreboard)
*   [Two failure modes, one globule](#two-failure-modes-one-globule)

Causal stack

1.  [00 Astra / global consistency](astra.md)
2.  [01 Genesis Pin](genesis-pin.md)
3.  [02 Retained pruning-order history](causal-stack.md)
4.  [03 Admissible slice](causal-stack.md)
5.  [04 L1 (closed)](causal-stack.md)
6.  [05 L2 (closed)](causal-stack.md)
7.  [06 L3 hyperedge memory T\_H + D\_L3](causal-stack.md)
8.  [07 L4 H₄ rank lift](causal-stack.md)
9.  [08 Discrete atlas / scalar accessibility](retained-atlas.md)
10. [09 GEM-bridge / gravity](emergent-gravity.md)

Labs/p53 is a 12-run coarse-grained campaign on the p53 DNA-binding domain, dated 22–23 Aug 2025 in the deliverable folders. The machine-readable contract is [findings.json](protein-audit.md) v2.2. The human manuscript (ReadMe.pd) is co-attributed to Gemini, ChatGPT, Grok, and [Aaron Spradlin](aaron-spradlin.md). There is no load-bearing X field note for this campaign in the current compile — it lives on GitHub. Cite the folder and the [science contract](protein-audit.md), not a tweet.

What the campaign is allowed to say

Wild-type also collapses to a compact non-native globule (best RMSD 26.6 Å). The result is mechanism differentiation among misfolded globules, not native p53 folding. Contact-anneal + PhiKan083 improved Y220C from ~25 Å to 18.9 Å inside this force field. That is not a pharmacological proof and not a crystal-structure rescue.

## Thesis in the contract {#thesis-in-the-contract}
> Across the [UQCF-GEM](uqcf-gem.md) campaign, p53-Y220C predominantly fails via a kinetic collapse trap, while p53-R248Q failure is electrostatic in nature. A protocol-level intervention—contact anneal with PhiKan083—achieves meaningful improvement (≤ 20 Å) relative to ~25 Å baselines. The campaign ultimately revealed a force-field limitation in the ligand model.

## Twelve-run scoreboard {#twelve-run-scoreboard}
| Run | Purpose | Claim type | Best RMSD (Å) | Contract verdict |
| --- | --- | --- | --- | --- |
| 1 | R248Q baseline | electrostatic\_failure | 26.6 | CONFIRMED (salt-bridge collapse; median 1 vs WT 7) |
| 2 | WT baseline | control\_informative | 26.6 | CONFIRMED (misfolded globule) |
| 3 | Y220C coil-start | kinetic\_trap | 25.4 | CONFIRMED |
| 4 | Y220C + L221F | negative\_result | 26.1 | CONFIRMED (genetic rescue fails) |
| 5 | PhiKan083 native-start artifact | control\_artifact | ~0.0 | CONFIRMED as artifact |
| 6 | PhiKan083 HERO control | ligand\_partial | 19.5 | CONFIRMED (partial) |
| 7 | PhiKan083 HERO v1 | ligand\_partial | 19.5 | CONFIRMED (partial) |
| 8 | PhiKan083 native-start validation | native\_validation\_limit | 4.0 | CONFIRMED (drift; ligand-model limit) |
| 9 | Contact anneal + PhiKan083 | rescue\_protocol | 18.9 | INDETERMINATE in this compile (ContactAnneal folder missing) |
| 10 | PhiKan083 rescue v1 pilot | ligand\_partial | 25.7 | CONFIRMED (no rescue) |
| 11 | PhiKan083 timing sweep | ligand\_thermodynamic | 18.9 | CONFIRMED (stabilizer, not kinetic guide) |
| 12 | Y220F rescue attempt | negative\_result | 26.1 | CONFIRMED (genetic rescue fails) |

Manuscript numbers from Labs/p53/ReadMe.pd Table 1. This compile’s deterministic pass (7 Sep 2026) reproduced the same order from diagnostics CSVs (R248Q/WT tail-median 26.71 Å vs 26.6; Y220C coil 25.32 vs 25.4; native-start 3.82 vs 4.0; Run 11 18.86 vs 18.9): 11 CONFIRMED, 0 DEVIATION, 1 INDETERMINATE. Run 9’s ContactAnneal folder is not in the public tree — do not treat the 18.9 Å rescue as independently re-read. Start the engine smoke test on [MECP2](mecp2-rett.md), not here.

## Two failure modes, one globule {#two-failure-modes-one-globule}
Final RMSD alone does not separate the mutants from wild-type. The mechanistic split is in the diagnostics. R248Q (DNA-contact mutant) loses the salt-bridge network (median 1.0 versus WT 7.0) while collapsing to the same 26.6 Å globule — electrostatic\_failure. Y220C (pocket mutant) is diagnosed as a kinetic trap: genetic pocket patches Y220F and L221F do not improve RMSD; a gentler contact-anneal protocol plus the pharmacological chaperone PhiKan083 does, inside this model. The timing sweep says the ligand acts as a thermodynamic stabilizer of the collapsed state, not a kinetic folding guide.

*   Model: coarse-grained, backbone-centric [UQCF-GEM](uqcf-gem.md). Terms named in the manuscript: steric, directional H-bond, Ramachandran, Debye–Hückel electrostatics, tunable contact springs.
*   Protocol: extended coil start unless marked native-start. pH 7.4, ionic strength 150 mM. k\_hbond = 16.0, k\_contact\_springs = 0.05 as the posted sweet spot.
*   Negative results are first-class: L221F and Y220F fail; the native-start ligand run drifts to 4.0 Å and is filed as a force-field limit, not hidden.
*   PNG and PDB artifacts in Labs/ are Git LFS pointers in a plain clone. Markdown reports, raw CSVs, and [findings.json](protein-audit.md) are ordinary files.

Restricted

Inside this coarse-grained campaign, R248Q and Y220C reach similar misfolded globules by different routes (electrostatic network loss vs kinetic trap), and a contact-anneal + PhiKan083 protocol improved Y220C RMSD relative to ~25 Å baselines. Not native folding, not a crystal rescue, not a cancer therapy, not a TOE result.

Not claimed

This atlas does not claim that PhiKan083 rescues p53-Y220C in cells, or that [UQCF-GEM](uqcf-gem.md) replaces all-atom MD. The native-start drift is the campaign’s own limit.

*   [Labs/p53 on GitHub](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Labs/p53)
*   [findings.json v2.2](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Labs/p53/findings.json)
*   [Run this first (MECP2 smoke)](protein-audit.md)
*   [MECP2 campaign](mecp2-rett.md)

[Previous MECP2 Rett MBD–DNA campaign](mecp2-rett.md)[Next Frozen v9 protein bridge (1UAO / 1L2Y)](protein-bridge-v9.md)

Causal stack

1.  [00 Astra / global consistency](astra.md)
2.  [01 Genesis Pin](genesis-pin.md)
3.  [02 Retained pruning-order history](causal-stack.md)
4.  [03 Admissible slice](causal-stack.md)
5.  [04 L1 (closed)](causal-stack.md)
6.  [05 L2 (closed)](causal-stack.md)
7.  [06 L3 hyperedge memory T\_H + D\_L3](causal-stack.md)
8.  [07 L4 H₄ rank lift](causal-stack.md)
9.  [08 Discrete atlas / scalar accessibility](retained-atlas.md)
10. [09 GEM-bridge / gravity](emergent-gravity.md)

On this page

*   [Thesis in the contract](#thesis-in-the-contract)
*   [Twelve-run scoreboard](#twelve-run-scoreboard)
*   [Two failure modes, one globule](#two-failure-modes-one-globule)

Related articles

*   [For researchers and models](for-researchers.md)
*   [Claim ledger](claim-ledger.md)
*   [Applied recoverability stack](applied-stack.md)
*   [WetLabEngine protein audit](protein-audit.md)
*   [MECP2 Rett MBD–DNA campaign](mecp2-rett.md)
*   [Frozen v9 protein bridge (1UAO / 1L2Y)](protein-bridge-v9.md)
*   [Open science method](open-science.md)

GitHub packages

*   [Labs/p53](../packages/labs-p53.md)
*   [WetLabEngine (root)](../packages/wetlab-root.md)
