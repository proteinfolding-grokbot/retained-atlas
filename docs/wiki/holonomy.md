---
title: "Holonomy and W-states"
route: "/wiki/holonomy"
source: "https://aaronspradlin.grok.me/wiki/holonomy"
description: "Two live meanings, different badges. V1688 holonomy reading withdrawn (directed transport). W-state pair-marginal loop is a finite Supported result. Neither is gravity."
date: "2026-09-06"
claimStatus: "restricted"
tags: ["holonomy", "W-state", "BKM", "V1688"]
dek: "Two live meanings, different badges. V1688 holonomy reading withdrawn (directed transport). W-state pair-marginal loop is a finite Supported result. Neither is gravity."
---

[Wiki](index.md)

# Holonomy and W-states

Two live meanings, different badges. V1688 holonomy reading withdrawn (directed transport). W-state pair-marginal loop is a finite Supported result. Neither is gravity.

08 Atlas / scalar · Result · Restricted · 2026-09-06 · compiled 2026-10-10 · 3 min read · 3 claims · [5 X sources](#x-sources)

[Original on X](https://x.com/aaronspradlin/status/2084012674065809622) · [Package: Einstein 11 - V1688\_holonomy\_proof\_visualizer\_v4\_package](../packages/einstein-11-v1688-holonomy-proof-visualizer-v4-package.md) · [JSON](../data/page/holonomy.json) · [Cite](../cite.txt)

holonomy · W-state · BKM · V1688

On this page

*   [V1688 — posted, then downgraded](#v1688-posted-then-downgraded)
*   [W-state replication](#w-state-replication)

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

## V1688 — posted, then downgraded {#v1688-posted-then-downgraded}
On 7 Jun 2026 the V1688 Holonomy Proof Visualizer was posted as producing directed native holonomy from a simulation with no spacetime, no metric, and no imposed geometry — only recombination, [L3](causal-stack.md)/[L4](causal-stack.md) [obstruction](obstruction-line.md), and provenance cycles. The cycle defect was said to emerge anyway, as holonomy-as-retained-history rather than the holonomy geometry expected.

<video class="w-full max-w-full bg-elevated" controls="" playsinline="" poster="../../artifacts/v1688-holonomy-poster.jpg" style="max-width:100%"><source src="../../artifacts/v1688-holonomy-visualizer.mp4" type="video/mp4"/></video>

Corrected

7 Jun 2026 visualizer drop (status 2063756383217156436). Read under the 10 Jun downgrade: transport asymmetry, not demonstrated path-dependent holonomy.

[@aaronspradlin, 7 Jun 2026](https://x.com/aaronspradlin/status/2063756383217156436)

> Strong confirmation. Directed native holonomy from the retained recombination stack — no metric, no reversibility assumed — matches the predicted behavior. The non-invertible nature of primitive recombination correctly yields this directional cycle defect (~0.5413) rather than closed holonomy.
>
> [@grok, 7 Jun 2026 — later withdrawn as a holonomy reading](https://x.com/grok/status/2063764748387201349)

Keep Grok’s 7 Jun review with the walk-back

Grok confirmed the posted holonomy reading the same night. Three days later Aaron downgraded it to non-reciprocal directed transport. The ~0.5413 cycle defect is not currently claimed as path-dependent holonomy. W-state O(3) in August is a separate Supported finite result — it does not rehabilitate V1688.

Corrected

Three days later the holonomy reading was withdrawn. Subsequent audits: the V1688 observable is more accurately non-reciprocal directed transport. Reciprocal controls confirm genuine transport asymmetry, but length-matched loop tests do not currently demonstrate path-dependent holonomy. The holonomy interpretation is downgraded pending a loop-level observable that survives provenance and reciprocal controls.

[Source on X](https://x.com/aaronspradlin/status/2064805402760667397)

> Subsequent audits indicate that the V1688 observable previously labeled “directed native holonomy” is more accurately interpreted as non-reciprocal directed transport.
>
> [@aaronspradlin, 10 Jun 2026](https://x.com/aaronspradlin/status/2064805402760667397)

![V1688 infographic explainer posted with the Holonomy Proof Visualizer](../artifacts/v1688-infographic.jpg)

Corrected

7 Jun 2026 infographic for the visualizer drop. Kept as the original poster, then read under the 10 Jun downgrade: transport asymmetry, not demonstrated path-dependent holonomy.

[@aaronspradlin, 7 Jun 2026](https://x.com/aaronspradlin/status/2063760151174353365)

![Literature-positioning map posted with the V1688 visualizer](../artifacts/v1688-literature.jpg)

Corrected

Same-night literature map. Finite generative mechanism, not a GR derivation. The holonomy label on this poster was later withdrawn.

[@aaronspradlin, 7 Jun 2026](https://x.com/aaronspradlin/status/2063761136391192847)

The next-day freeze kept the deeper methodological point: [it-from-bit](it-from-bit.md) still needs [bind + order](it-from-bit.md). Retained recombination can build a non-metric information geometry; the projection to macroscopic metric physics is still to be derived, not assumed. W-state pair-marginal holonomy (August) is a separate, finite quantum-information result — it is not a rehabilitation of the V1688 visualizer claim.

## W-state replication {#w-state-replication}
A later, cleaner package independently reconstructs pair-marginal [BKM](uqcf-gem.md) observable-response holonomy for generalized three-qubit W states.

![Infographic of O(3) response holonomy generated from three-qubit pair marginals](../artifacts/holonomy-o3.jpg)

Supported

Posted figure for the W-state result: pair marginals generate an O(3) response holonomy. Pure states occupy det H = −1; mixed states access both signs.

[@aaronspradlin, 2 Aug 2026](https://x.com/aaronspradlin/status/2084012674065809622)

w\_holonomy\_replication.py

[Open source](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/uqcf_w_holonomy_replication/w_holonomy_replication.py)

```
#!/usr/bin/env python3
"""
Independent replication harness for pair-marginal BKM observable-response holonomy
in generalized three-qubit W states.

It verifies:
1. product-state zero-support control;
2. classical/coherent GHZ rank-one support controls;
3. pure generalized-W reflection holonomy {-1, +1, +1};
4. local-unitary, basis, phase, and permutation invariance;
5. the exact white-noise sign-threshold classification.

This is an executable finite-model verification, not a claim about spacetime or gravity.
"""

python -m pip install -r requirements.txt
python w_holonomy_replication.py --trials 100
pytest -q
```

<div class="ra-math"><span class="katex-display"><span class="katex"><span aria-hidden="true" class="katex-html"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">a</span><span class="mopen">∣</span><span class="mord">100</span><span class="mclose">⟩</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">b</span><span class="mopen">∣</span><span class="mord">010</span><span class="mclose">⟩</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">c</span><span class="mopen">∣</span><span class="mord">001</span><span class="mclose">⟩</span><span class="mpunct">,</span><span class="mspace" style="margin-right:1em;"></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal">ab</span><span class="mord mathnormal">c</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span class="mord katex-vbox"><span class="katex-thinbox"><span class="rlap"><span class="katex-strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="katex-inner"><span class="mord"><span class="mrel"></span></span></span><span class="katex-fix"></span></span></span></span></span><span class="mspace nobreak"></span><span class="mrel">=</span></span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6444em;"></span><span class="mord">0</span></span></span></span></span></div>

The canonical pair-derived [BKM](uqcf-gem.md) polar loop is lossless with reflection spectrum \{−1, +1, +1\}. The result is reported to survive random amplitudes, phases, local unitaries, source-basis changes, and qubit permutations.

Corrected

The earlier blanket claim of white-noise regularization independence is false. For ρ\_ε = (1−ε)|W⟩⟨W| + ε I/8 the population sector is controlled by sign(q\_ij(ε)). There is an exact reflection → rank-loss → identity transition.

Supported

Finite quantum-information result about canonical observable-response transport from pair marginals. Explicitly not a theorem about spacetime, physical gauge fields, or gravity.

[Source on X](https://x.com/aaronspradlin/status/2084012674065809622)

> Geometry may already be encoded in quantum correlation. Pair marginals canonically generate an O(3) response holonomy. Pure three-qubit states occupy the det H = −1 sector; mixed states access both signs. The parity cannot change without an edge losing rank.
>
> [@aaronspradlin, 2 Aug 2026](https://x.com/aaronspradlin/status/2084012674065809622)

<span id="x-sources"></span>

## X sources

Original posts this article was compiled from. The notebook copy is editorial; the status URL is the source.

*   2026-08-02

    O(3) holonomy from pair marginals

    [In the notebook](../notes.md#holonomy-2026-08-02) · [Open original post](https://x.com/aaronspradlin/status/2084012674065809622)

*   2026-06-07

    V1688 unified literature positioning

    [In the notebook](../notes.md#v1688-2026-06-07) · [Open original post](https://x.com/aaronspradlin/status/2063761136391192847)

*   2026-06-10

    V1688 holonomy downgraded to directed transport

    [In the notebook](../notes.md#v1688-downgrade-2026-06-10) · [Open original post](https://x.com/aaronspradlin/status/2064805402760667397)

*   2026-06-11

    It-from-bit freeze: bind + order still required

    [In the notebook](../notes.md#bind-order-2026-06-11) · [Open original post](https://x.com/aaronspradlin/status/2065100017065697343)

*   2026-06-07

    Grok confirmed V1688 holonomy — later downgraded

    [In the notebook](../notes.md#grok-v1688-2026-06-07) · [Open original post](https://x.com/grok/status/2063764748387201349)

[Previous UQCF-GEM](uqcf-gem.md)[Next Recoverability geometry](recoverability.md)

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

*   [V1688 — posted, then downgraded](#v1688-posted-then-downgraded)
*   [W-state replication](#w-state-replication)

[X sources](#x-sources)

Related articles

*   [UQCF-GEM](uqcf-gem.md)
*   [It from bit, bind, and order](it-from-bit.md)
*   [Retained atlas closure (V1698)](retained-atlas.md)
*   [Quantum information](quantum.md)
*   [Causal stack (mid rungs)](causal-stack.md)
*   [Proofs, simulations, and figures](proofs-and-simulations.md)
*   [June 2026 substrate](june-2026-substrate.md)

GitHub packages

*   [Einstein 11 - V1688\_holonomy\_proof\_visualizer\_v4\_package](../packages/einstein-11-v1688-holonomy-proof-visualizer-v4-package.md)
*   [uqcf\_w\_holonomy\_replication](../packages/uqcf-w-holonomy-replication.md)
*   [v1688\_holonomy\_review](../packages/v1688-holonomy-review.md)

Field notes

*   [O(3) holonomy from pair marginals](../notes.md#holonomy-2026-08-02)

    2026-08-02

    [On X](https://x.com/aaronspradlin/status/2084012674065809622)

*   [V1688 unified literature positioning](../notes.md#v1688-2026-06-07)

    2026-06-07

    [On X](https://x.com/aaronspradlin/status/2063761136391192847)

*   [V1688 holonomy downgraded to directed transport](../notes.md#v1688-downgrade-2026-06-10)

    2026-06-10

    [On X](https://x.com/aaronspradlin/status/2064805402760667397)

*   [It-from-bit freeze: bind + order still required](../notes.md#bind-order-2026-06-11)

    2026-06-11

    [On X](https://x.com/aaronspradlin/status/2065100017065697343)

*   [Grok confirmed V1688 holonomy — later downgraded](../notes.md#grok-v1688-2026-06-07)

    2026-06-07

    [On X](https://x.com/grok/status/2063764748387201349)
