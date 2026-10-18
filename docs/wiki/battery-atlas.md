---
title: "Battery recoverability (V720–V724)"
route: "/wiki/battery-atlas"
source: "https://aaronspradlin.grok.me/wiki/battery-atlas"
date: "2026-05-19"
claimStatus: "restricted"
tags: ["battery", "NASA", "V720", "applied"]
dek: "NASA PCoE LCO relaxation trajectories: active restoration-deficit beats passive snap distance — an applied recoverability assay."
---

[Wiki](https://aaronspradlin.grok.me/wiki)

# Battery recoverability (V720–V724)

NASA PCoE LCO relaxation trajectories: active restoration-deficit beats passive snap distance — an applied recoverability assay.

AppliedAppliedRestricted2026-05-19compiled 2026-10-101 min read1 claim[1 X source](#x-sources)

[Original on X](https://x.com/aaronspradlin/status/2056532353804370341)[Package: battery](https://aaronspradlin.grok.me/packages/battery)[JSON](../data/page.json)[Cite](../data/cite.txt)

batteryNASAV720applied

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

The retained-atlas framework was pressure-tested on the NASA PCoE LCO battery dataset (V720) and on synthetic assays V723/[V724](may-2026-ladder.md). Passive “snap distance” (instantaneous voltage drop) delivers AUC 0.6366 and is already collapsing toward chance. Integrated restoration-deficit metrics — early\_auc, tail\_auc, full\_auc — reach AUC 0.9326 and Spearman 0.8715 to capacity loss. Residualizing out the initial snap still leaves AUC 0.8655.

V723 holds passive burden metrics at chance (~0.500) while active adm\_z separates perfectly (AUC 1.000) in the synthetic. [V724](may-2026-ladder.md) adds overlapping k, nonlinear saturation, reserve fatigue, stochastic stalls, and shortened windows; signal holds at ≈0.845. Geometry-like structures (curvature concentration, geodesic relaxation, stress localization) are reported as emergent in the assay, not imposed.

Supported

[V724](may-2026-ladder.md) stress-test ROC: active restoration-deficit (adm\_z) versus passive snap. Signal holds under overlapping k, saturation, fatigue, and shortened windows. Applied [recoverability](recoverability.md), not a field equation.

[v724\_stress\_test\_outputs on GitHub](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/v724_stress_test_outputs)

Supported

Paired Δ(adm\_z) versus passive on the same synthetic trajectories. The passive metric collapses toward chance.

[v724\_stress\_test\_outputs on GitHub](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/v724_stress_test_outputs/paired_delta_adm_z_vs_passive.png)

Supported

On this public NASA dataset and the published synthetics, active restoration-deficit scoring outperforms passive snap. This is an applied [recoverability](recoverability.md) result. It does not solve battery aging and does not derive field equations.

[Source on X](https://x.com/aaronspradlin/status/2056532353804370341)

A 18 May 2026 open letter (posted from the account, attributed as a Grok draft) argued Tesla already collects the relevant rest-window voltages in BMS health checks. That is advocacy built on the assay, not a Tesla collaboration claim. The original V723/[V724](may-2026-ladder.md) assay video is 18 May: passive burden held equivalent, active perturbation-response still showing restorative structure — observation only, synthetic, falsifiable.

* [V723/V724 assay video (X)](https://x.com/aaronspradlin/status/2056494244622369095)
* [Tesla letter thread (X)](https://x.com/aaronspradlin/status/2056532353804370341)

## X sources

Original posts this article was compiled from. The notebook copy is editorial; the status URL is the source.

* 2026-05-19

  NASA battery assay and Tesla letter

  [In the notebook](https://aaronspradlin.grok.me/notes#tesla-letter-2026-05-19)[Open original post](https://x.com/aaronspradlin/status/2056532353804370341)

[PreviousC3++ Stability Governor](c3-governor.md)[NextMay 2026 ladder](may-2026-ladder.md)

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

Related articles

* [Recoverability geometry](recoverability.md)
* [Restricted bridge theorems](restricted-bridge.md)
* [Applied recoverability stack](applied-stack.md)
* [C3++ Stability Governor](c3-governor.md)
* [Proofs, simulations, and figures](proofs-and-simulations.md)

GitHub packages

* [battery](https://aaronspradlin.grok.me/packages/battery)
* [v724\_stress\_test\_outputs](https://aaronspradlin.grok.me/packages/v724-stress-test-outputs)

Field notes

* [NASA battery assay and Tesla letter](https://aaronspradlin.grok.me/notes#tesla-letter-2026-05-19)

  2026-05-19

  [On X](https://x.com/aaronspradlin/status/2056532353804370341)
