---
title: "Proofs, simulations, and figures"
route: "/wiki/proofs-and-simulations"
source: "https://aaronspradlin.grok.me/wiki/proofs-and-simulations"
date: "2026-09-10"
tags: ["python", "proofs", "simulations", "figures", "SPARC"]
dek: "The advertised Python harnesses and the result images Aaron posted — copied from GitHub and X, not redrawn. Not every file in Tmp/TOE."
---

[Wiki](https://aaronspradlin.grok.me/wiki)

# Proofs, simulations, and figures

The advertised Python harnesses and the result images Aaron posted — copied from GitHub and X, not redrawn. Not every file in Tmp/TOE.

MethodMethod2026-09-10compiled 2026-10-1013 min read6 claims[26 X sources](#x-sources)

[Original on X](https://x.com/aaronspradlin/status/2098145800949776410)[Package: uqcf\_codazzi\_proof](https://aaronspradlin.grok.me/packages/uqcf-codazzi-proof)[JSON](../data/page.json)[Cite](../data/cite.txt)

pythonproofssimulationsfiguresSPARC

On this page

* [Run this first](#run-this-first)
* [V1698 retained global atlas](#v1698-retained-global-atlas)
* [Quantum compatibility lab (v9.167)](#quantum-compatibility-lab-v9-167)
* [v12.41 moment-map closure](#v12-41-moment-map-closure)
* [Great Grok Challenge 14 (SPARC 171)](#great-grok-challenge-14-sparc-171)
* [Three-node Codazzi harness](#three-node-codazzi-harness)
* [Applied labs — protein, TSP, critical path](#applied-labs-protein-tsp-critical-path)
* [May 2026 films and labs](#may-2026-films-and-labs)
* [June 2026 films and labs](#june-2026-films-and-labs)
* [sim\_l4.py — dashboard, not the rank algebra](#sim-l4-py-dashboard-not-the-rank-algebra)
* [Finite executable proofs](#finite-executable-proofs)
* [Quantum compatibility lab (v9.167)](#quantum-compatibility-lab-v9-167-2)
* [v12.41 moment-map closure](#v12-41-moment-map-closure-2)
* [Codazzi thread (1 Aug 2026)](#codazzi-thread-1-aug-2026)
* [Atlas and holonomy simulations](#atlas-and-holonomy-simulations)
* [SPARC / Challenge cosmology](#sparc-challenge-cosmology)
* [UQCF visual pack](#uqcf-visual-pack)
* [Python copies in this atlas](#python-copies-in-this-atlas)
* [Early cosmology figures (not claimed)](#early-cosmology-figures-not-claimed)
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

This page is the evidence drawer. The wiki previously quoted residuals and AUC numbers without showing the plots or the Python that produced them. That is now corrected — with an honest boundary: Tmp/TOE has sixty-plus working folders. This atlas does not vend the entire tree. It ships the named, advertised harnesses and the result images that were actually posted.

What is in here

Copies of posted figures (X + GitHub), runnable Python from the advertised proof packets, and Challenge 14’s aggregate JSON. Captions keep claim status. Early-2025 cosmology plots are included as field-notebook images and marked not-claimed — later packets walked those closures back.

## Run this first[#](#run-this-first)

Run these four first — folder-only

Do not read the X thread before the script. A PASS is not Einstein. In-thread @grok is collaborative, not independently audited.

| Harness | Folder | Command | Expect | PASS does not mean |
| --- | --- | --- | --- | --- |
| [V1698](retained-atlas.md) atlas closure | Tmp/TOE/Einstein\_12\_V1698\_valid\_only\_slow\_atlas\_closure\_mp4\_package | python3 V1698\_valid\_only\_slow\_atlas\_closure\_mp4.py | inverse / cocycle / [holonomy](holonomy.md) residual ~3.27×10⁻¹⁶ on the five-chart ledger | Continuum spacetime, ADM, Einstein equations |
| [V824](accessibility-curvature.md) accessibility-curvature | Tmp/TOE/Einstein Phase 1/V824\_accessibility\_curvature\_paper\_python\_proof | python3 "Tmp/TOE/Einstein Phase 1/V824\_accessibility\_curvature\_paper\_python\_proof/accessibility\_curvature\_proof.py" | held-out R² ~ 0.88; adversarial nulls collapse | Tensor Einstein, ADM momentum, physical spacetime |
| [W-state](holonomy.md) [BKM](uqcf-gem.md) [holonomy](holonomy.md) | Tmp/TOE/uqcf\_w\_holonomy\_replication | python w\_holonomy\_replication.py --trials 100 && pytest -q | pure W, abc≠0: reflection spectrum {−1,+1,+1} | White-noise independence (withdrawn). Gravity. All states. |
| Three-node [Codazzi](uqcf-gem.md) | Tmp/TOE/uqcf\_codazzi\_proof | python uqcf\_codazzi\_verification.py | unbiased [Codazzi defect](uqcf-gem.md) 0; Ξ(J)=J² [[0,1],[−1,0]] + O(J³) | All graphs, continuous systems, gravity |

[Supported four](supported-four.md). Then Restricted demos ([compatibility lab](compatibility-lab.md), [v12.41](v1241-closure.md), Challenge 14) below.

GitHub remains the source of truth. This page only makes the entry cheaper. One notebook per major result, with the numeric target on the wiki itself, a box for what a successful run does not show, and who has actually executed it.

1. [V1698](retained-atlas.md) retained [global atlas](retained-atlas.md) — residual ~3.27×10⁻¹⁶ on a five-chart ledger. Supported discrete closure.
2. [V824](accessibility-curvature.md) accessibility-curvature — scalar / conformal sector only. Supported.
3. [W-state](holonomy.md) [BKM](uqcf-gem.md) spectrum {−1,+1,+1} — finite QI [holonomy](holonomy.md). Supported. Article: [Holonomy](holonomy.md).
4. Three-node [Codazzi](uqcf-gem.md) — unbiased defect 0; Ξ(J) = J² [[0,1],[−1,0]] + O(J³). Grok-verified 1 Aug 2026. Supported finite family.
5. [Quantum compatibility lab (v9.167)](quantum-compatibility-lab.md) — [315 vs 311](quantum-compatibility-lab.md) nullities; 48.03% vs 46.55% collective Born. Restricted finite calc.
6. [v12.41 moment-map closure](v1241-closure.md) — 121 steps, [Δ\_closure](v1241-closure.md) = 0, broken 0.297. Restricted qubit [KKS](v1241-closure.md) identity. Not gravity.
7. [Great Grok Challenge](great-grok-challenge.md) 14 — frozen SPARC 171, 94.15% positive, 0 catastrophic, RAR 0.3902 → 0.1818. Restricted empirical.

### V1698 retained global atlas[#](#v1698-retained-global-atlas)

Run this first if you want the strongest discrete closure.

Supported

inverse / cocycle / [holonomy](holonomy.md) residual: ~3.27×10⁻¹⁶. cover: five-chart ledger. nulls: source / support / order shuffle must fail

* What this does not show — Continuum spacetime, ADM momentum, or a GR limit.
* Who has run it — Author + public AI red-team (Grok invited 9 Jun 2026). No posted third-party human rerun of the full package.

* [Article](retained-atlas.md)
* [GitHub package](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/Einstein_12_V1698_valid_only_slow_atlas_closure_mp4_package)

### Quantum compatibility lab (v9.167)[#](#quantum-compatibility-lab-v9-167)

Run this first if you want this week’s finite quantum identity.

Restricted

global-completion nullities: [315 vs 311](quantum-compatibility-lab.md). collective Born: 0.480269472 vs 0.465533202 (48.03% vs 46.55%). pair traces: agree to 4×10⁻¹⁸. shared curve max A/B difference: 1.11×10⁻¹⁶

* What this does not show — A laboratory observation, a general hidden-information theorem, [v9](protein-bridge-v9.md).156 [d(t)](astra.md), or gravity.
* Who has run it — Author. @grok restated the finite case 6 Sep 2026. Independent human rerun not posted.

* [Article](quantum-compatibility-lab.md)
* [GitHub package](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/UQCF_Quantum_Compatibility_Lab)

### v12.41 moment-map closure[#](#v12-41-moment-map-closure)

Run this first if you want the closed qubit [constraint algebra](v1241-closure.md). Restricted. Not gravity.

Restricted

relational transforms: 121. exact [Δ\_closure](v1241-closure.md): 0. broken generator law max: 0.297. min eig: 0.2508

* What this does not show — Derived gravity, ADM, Einstein constraints, or physical time. λ is an ordered sweep.
* Who has run it — Author. Independent reconstruction in this compile matched the posted CSV/log. No posted third-party human rerun of the full packet.

* [Article](v1241-closure.md)
* [GitHub package](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/UQCF_GEM_v12_41_PUBLIC_SIMULATION_COMPLETE)

### Great Grok Challenge 14 (SPARC 171)[#](#great-grok-challenge-14-sparc-171)

Run this first if you want the heaviest external empirical packet.

Restricted

positive improvement: 94.15% of 171. catastrophic failures: 0. RAR scatter: 0.3902 → 0.1818

* What this does not show — A dark-matter disproof, a Hubble resolution, or [Package 17](package-17.md) closure.
* Who has run it — Author. Grok logged win conditions in-thread. [WALLABY](great-grok-challenge.md) 12D is a separate unseen-gas transfer (10/10, +14.56 km/s RMSE).

* [Article](great-grok-challenge.md)
* [GitHub package](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/challenge14_packet)

### Three-node Codazzi harness[#](#three-node-codazzi-harness)

Run this first if you want a Grok-verified finite identity.

Supported

unbiased [Codazzi defect](uqcf-gem.md): 0. weak-coupling Ξ(J): J² [[0,1],[−1,0]] + O(J³)

* What this does not show — All graphs, a gravity proof, or a potential-response identity on every exponential family.
* Who has run it — Author. @grok verified at high precision and independently re-ran, 1 Aug 2026. Closed-form A(J), B(J) matched numerical differentiation.

* [Article](uqcf-gem.md)
* [GitHub package](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/uqcf_codazzi_proof)

No Colab is posted for these packets. Run from the GitHub folder. Independent human reruns of the full Tmp/TOE tree are not posted; Grok in-thread verification is the public AI red-team record.

What a green residual does not show

A successful run of [V1698](retained-atlas.md) is not a gravity derivation. A successful run of [V824](accessibility-curvature.md) is scalar / conformal only. [W-state](holonomy.md) [BKM](uqcf-gem.md) and three-node [Codazzi](uqcf-gem.md) are Supported finite QI, not all graphs and not gravity. A successful run of the [compatibility lab](compatibility-lab.md) is Restricted — not a laboratory observation and not [v9](protein-bridge-v9.md).156. [v12.41](v1241-closure.md) is Restricted — not ADM, not Einstein. A successful Challenge 14 pass is Restricted empirical, not a dark-matter disproof.

## Applied labs — protein, TSP, critical path[#](#applied-labs-protein-tsp-critical-path)

These three are not geometry harnesses. They are the [recoverability](recoverability.md) stack transferred into runnable Python: [Villin HP35](protein-audit.md) on WetLabEngine, a [fractal TSP](tsp-backbone.md) backbone, and a live critical-path optimizer. The live labs reconstruct the operator in the browser. Posted residuals stay on X. Recurrence is not a unification proof.

| Lab | Posted | Target | What a green run does not show |
| --- | --- | --- | --- |
| WetLabEngine [MECP2](mecp2-rett.md) smoke | 7 Sep 2026 compile | 15 CONFIRMED / 1 DEVIATION / 3 INDETERMINATE; Run 5 at 3.06 Å | A Gemini rerun; a [Rett](mecp2-rett.md) therapy; native folding |
| [Villin HP35](protein-audit.md) | 14 Apr 2026 | AUC G\_t+[R\_t](uqcf-gem.md) ≈ 0.9569 vs G\_t; matched-pair gap ~49% | AlphaFold refuted; a folding oracle |
| [TSP](tsp-backbone.md) backbone | 11 Apr 2026 | NN 1984.6 / 0.2267 vs GEM 2492.7 / 0.5251 | A championship [TSP](tsp-backbone.md) solver |
| [Critical path](critical-path.md) | 1 May 2026 | Preserve / deform / reset on a live plan | A Gantt product; a unification theorem |

Restricted empirical. Browser toys on /labs are reconstructions, not these residuals. WetLabEngine smoke is the deterministic auditor, not the [Villin](protein-audit.md) AUC.

applied\_recoverability\_operator.py

[Open source](../data/artifacts/py/applied_recoverability_operator.py)

```
def recover(G, R, shock, tau_lo=0.25, tau_hi=0.72):
    stress = strain(G, R, shock)
    keep   = G[stress < tau_lo]
    warp   = deform(G[(stress >= tau_lo) & (stress < tau_hi)], R)
    reseed = reset(G[stress >= tau_hi])
    return splice(keep, warp, reseed)
```

* [Live labs](../labs.md)
* [Applied recoverability stack](applied-stack.md)
* [TSP coherence backbone](tsp-backbone.md)
* [New Critical Path](critical-path.md)
* [WetLabEngine protein audit](protein-audit.md)

## May 2026 films and labs[#](#may-2026-films-and-labs)

These are the advertised May simulations and GitHub stills the GitHub-first compile dropped — copied from X and Tmp/TOE, not redrawn. Claim posture stays Restricted or Open. None of them is a gravity derivation. The month page holds the argument.

[![](/artifacts/v541-flow.png)](/artifacts/v831-flow.mp4)

Restricted

15 May [V831](recoverability.md) [recoverability](recoverability.md)-flow film. Governor-enforced repair/reserve/defect constraints. Applied instrument, not GR.

[@aaronspradlin, 15 May 2026](https://x.com/aaronspradlin/status/2055293211242107264)

[![](/artifacts/v541-flow.png)](/artifacts/v831-fullstack.mp4)

Restricted

20 May [V831](recoverability.md) full-stack freeze. Geometry-like organization from informational constraints. Not GR proven. [V824](accessibility-curvature.md) the same day pruned tensor/ADM.

[@aaronspradlin, 20 May 2026](https://x.com/aaronspradlin/status/2057208105830940954)

[![](/artifacts/v555-validity.png)](/artifacts/v760-atrium.mp4)

Restricted

19 May [V760](recoverability-framework.md) atrium-metric film. g\_eff = Ω² g0 under recovery pressure in the sim. Python: GR Work/[AtriumSimulation](may-2026-ladder.md).py. Not physical GR.

[@aaronspradlin, 19 May 2026](https://x.com/aaronspradlin/status/2056874571471650927)

[![](/artifacts/v923-handshake.jpg)](/artifacts/genesis-pin-filter.mp4)

Restricted

23 May [Genesis Pin](genesis-pin.md) five-history filter. Same visible state ≠ same legitimate history. Restricted toy.

[@aaronspradlin, 23 May 2026](https://x.com/aaronspradlin/status/2058291743167316149)

Restricted

14 May [V498](may-2026-ladder.md) Python proof. Six graph families. v498\_retained\_geometry\_proof.py. Not GR.

[@aaronspradlin, 14 May 2026](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/v498_retained_geometry_formal_report_package)

Restricted

13 May [V395](may-2026-ladder.md). Collapse is A\_t below a dynamic floor. Control-law candidate. Not GR.

[@aaronspradlin, 13 May 2026](https://x.com/aaronspradlin/status/2054637611898360173)

Restricted

18 May [V724](may-2026-ladder.md): adm\_z AUC 1.000 → ~0.845; passive burden near chance. Restricted synthetic.

[@aaronspradlin, 18 May 2026](https://x.com/aaronspradlin/status/2056496787968672242)

Restricted

12 May [V300](may-2026-ladder.md). [A\_norm](may-2026-ladder.md) threshold ~0.53–0.58. Toy. Not GR.

[@aaronspradlin, 12 May 2026](https://x.com/aaronspradlin/status/2054006183896477910)

Restricted

17 May synthesis after [V555](recoverability-framework.md). Next named object: V[Ω, C, μ]. Not a completed theorem.

[@aaronspradlin, 17 May 2026](https://x.com/aaronspradlin/status/2056092642832961737)

Restricted

16 May [V555](recoverability-framework.md). Selective-fragility AUC 1.0, defect-localization AUC 1.0. Synthetic adversarial. Not a physical law.

[v555\_full\_stack\_validity.png · Tmp/TOE/V555](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/V555)

v498\_retained\_geometry\_proof.py (posted header)

[Open source](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/v498_retained_geometry_formal_report_package/v498_retained_geometry_proof.py)

```
"""V498 Retained-Geometry Proof Run. Colab-ready.
This is not a GR derivation. Toy proof: a recoverability law
can generate source-responsive effective geometry.
Families: lattice, random geometric, scale-free, small-world,
tree-with-loops, fragmented block graph."""
C_t = M_t * R_t * L_t + lambda0 * eta_convert(t) * B_t
# dg_eff/dt = G_L * [T_retained / (C_t - C_floor + eps)] - R_repair - D_leakage
```

v505\_weak\_form\_validation.py (posted header)

[Open source](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/v505_continuum_object_package/v505_weak_form_validation.py)

```
"""V505 Weak-Form Continuum Object Validation
g_eff = Omega^2 g0. Source = G_L * [T_retained / (C - C_floor + eps)].
Not a GR continuum-limit derivation."""
```

v300\_reachability\_collapse\_law\_proof.py (posted header)

[Open source](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/Reachability%20Collapse%20Law%20/v300_reachability_collapse_law_proof.py)

```
"""V300 Retained-Atlas Reachability Collapse Law — Skeptical Proof Harness
A_norm = A(t) / A_baseline. NOT a proof of General Relativity.
NOT a physical spacetime derivation."""
```

retained\_branch\_identity\_audit.py (posted header)

[Open source](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/retained_branch_identity_audit.py)

```
"""Retained Branch Identity / Lineage Addressability Audit
retained coherence + lineage addressability + reference-frame anchors
  + moderate phase-lock -> observer-compatible causal accessibility geometry
This script is NOT a GR derivation, NOT physical validation, and NOT a TOE proof."""
```

## June 2026 films and labs[#](#june-2026-films-and-labs)

These are the posted simulations from the listed June (and immediately pre-June) threads — copied from X, not redrawn. Claim posture stays Restricted or Corrected. None of them is a gravity derivation.

[![](/artifacts/l4-rank-lift.jpg)](/artifacts/l4-rank-lift.mp4)

Restricted

6 Jun [L4](causal-stack.md) film: H4 not in span of branches plus [L3](causal-stack.md) associators. Python: Einstein 10\_v1687\_21\_l4/sim\_l4.py. Restricted finite-sector rank lift.

[@aaronspradlin, 6 Jun 2026](https://x.com/aaronspradlin/status/2063289036673065189)

[![](/artifacts/l3-v1638-stack.jpg)](/artifacts/l3-v1638-stack.mp4)

Restricted

4 Jun [V1638](causal-stack.md) full-stack film. [L3](causal-stack.md) associator rank\_lift = 1. Restricted.

[@aaronspradlin, 4 Jun 2026](https://x.com/aaronspradlin/status/2062942334049018048)

[![](/artifacts/l3-pruning-stack.jpg)](/artifacts/l3-pruning-mechanism.mp4)

Restricted

3 Jun mechanism film. [L3](causal-stack.md) integrated-only, not closed. Tmp/TOE repo.

[@aaronspradlin, 3 Jun 2026](https://x.com/aaronspradlin/status/2062182825227608089)

[![](/artifacts/mouse-it-from-bit.jpg)](/artifacts/mouse-it-from-bit.mp4)

Restricted

16 Jun mouse: pruning network experienced as time. Restricted toy. Six isomorphisms on the follow-up film.

[@aaronspradlin, 16 Jun 2026](https://x.com/aaronspradlin/status/2066965905570148699)

[![](/artifacts/v1688-holonomy-poster.jpg)](/artifacts/v1688-holonomy-visualizer.mp4)

Corrected

7 Jun [V1688](holonomy.md) visualizer. [Holonomy](holonomy.md) reading withdrawn 10 Jun. Kept as the original film, marked corrected.

[@aaronspradlin, 7 Jun 2026](https://x.com/aaronspradlin/status/2063756383217156436)

[![](/artifacts/v1698-atlas-poster.jpg)](/artifacts/v1698-atlas-closure.mp4)

Supported

9 Jun [V1698](retained-atlas.md) atlas-closure film. Supported discrete ledger. Not continuum GR.

[@aaronspradlin, 9 Jun 2026](https://x.com/aaronspradlin/status/2064485348433179128)

### sim\_l4.py — dashboard, not the rank algebra[#](#sim-l4-py-dashboard-not-the-rank-algebra)

The 6 Jun public Python is a 3D dashboard. Triple and quadruple source products are visualization proxies for [L3](causal-stack.md)/[L4](causal-stack.md). The finite-sector rank\_lift\_H4 = 1 numbers are from the same-day @grok research update, not from this visualizer script. Restricted. Not GR.

sim\_l4.py (posted dashboard)

[Open source](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/Einstein%2010_v1687_21_l4/sim_l4.py)

```
# L3 / L4 fields in the posted dashboard — visualization proxies.
# Claim boundary in the file: does not claim GR, Einstein equations,
# physical spacetime, or physical curvature.
triple_total = triple_123 + triple_124 + triple_134 + triple_234
l3_field = admissible * l3_strength * (2.8 * triple_total)
quadruple = source_fields[0] * source_fields[1] * source_fields[2] * source_fields[3]
l4_field = admissible * l4_strength * (6.5 * quadruple)
Z = base_geo + 1.6*l3_field + 2.1*l4_field
```

## Finite executable proofs[#](#finite-executable-proofs)

These are verification scripts, not Lean/Coq certificates. They reconstruct every reported tensor from an explicit finite model.

### Quantum compatibility lab (v9.167)[#](#quantum-compatibility-lab-v9-167-2)

Posted 6 Sep 2026 20:05 UTC. Fresh matrix calculations for the supplied [v9.167](quantum-compatibility-lab.md)–[v9](protein-bridge-v9.md).171 [matched four-weight](quantum-compatibility-lab.md) family. Not an independent proof of every theorem in that sequence, a new physical law, or an experimental result. Figures and the 27-second film are copies of the GitHub package, not redrawn.

### v12.41 moment-map closure[#](#v12-41-moment-map-closure-2)

Posted 10 Sep 2026 20:25 UTC. Qubit [KKS](v1241-closure.md) identity on 121 ordered relational transforms. This compile independently reconstructed max exact residual 0 and max broken residual 0.297. Film, PNG, CSV, and Python are copies of the GitHub packet. Not gravity.

Restricted

[v12.41](v1241-closure.md) verification plot from the public packet. Exact residual sits on zero; broken generator law does not. Restricted.

[v1241\_public\_simulation\_verification.png](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/UQCF_GEM_v12_41_PUBLIC_SIMULATION_COMPLETE/outputs/v1241_public_simulation_verification.png)

[![](/artifacts/v1241-verification.png)](/artifacts/v1241-simulation.mp4)

Restricted

Posted 121-step animation. λ is not physical time. Restricted.

[v1241\_public\_simulation.mp4](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/UQCF_GEM_v12_41_PUBLIC_SIMULATION_COMPLETE/outputs/v1241_public_simulation.mp4)

Restricted

Shared scalar curve on 171 parameters. Maximum A/B difference 1.11×10⁻¹⁶. Not the [v9](protein-bridge-v9.md).156 [d(t)](astra.md) slope. Restricted.

[compatibility\_curve.png · UQCF\_Quantum\_Compatibility\_Lab](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/UQCF_Quantum_Compatibility_Lab/output/compatibility_curve.png)

Restricted

Arrangement A diagnostic: pair traces agree to 4e-18; collective Born probabilities differ by the global trace distance. Calculated, not a laboratory observation.

[collective\_measurement.png · UQCF\_Quantum\_Compatibility\_Lab](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/UQCF_Quantum_Compatibility_Lab/output/collective_measurement.png)

* [Quantum compatibility lab article](quantum-compatibility-lab.md)
* [Complete package (GitHub)](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/UQCF_Quantum_Compatibility_Lab)

Supported

[Codazzi](uqcf-gem.md) result in one sentence: potential information geometry and response information geometry can separate. Smallest canonical interacting model. Not gravity.

[@aaronspradlin, 1 Aug 2026](https://x.com/aaronspradlin/status/2083643394300281016)

uqcf\_codazzi\_verification.py

[Open source](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/uqcf_codazzi_proof/uqcf_codazzi_verification.py)

```
#!/usr/bin/env python3
"""
Executable verification harness for the smallest canonical UQCF-GEM
state-level Codazzi audit.

Model: p(x) ∝ exp[h1*x1 + h2*x2 + J*(x1*x2 + x2*x3 + x3*x1)],
x_i ∈ {-1,+1}, h3 = 0. Eight-state enumeration. No reported
tensor values are hard-coded.

python -m pip install mpmath
python uqcf_codazzi_verification.py
"""
```

### Codazzi thread (1 Aug 2026)[#](#codazzi-thread-1-aug-2026)

The figure post is the question. The GitHub folder is the harness. Same-day Grok reviews and a genericity closeout sit on the same conversation. Finite three-spin exponential family only. Not gravity, not all graphs.

> Can a canonical information-theoretic response geometry always be generated from a single scalar potential? After building the framework from first principles, deriving the mathematics, and creating an executable verification harness, the smallest canonical interacting model says no. The result isn’t “we found gravity.” The result is that potential information geometry and response information geometry can separate.
>
> [@aaronspradlin, 1 Aug 2026 19:57 UTC](https://x.com/aaronspradlin/status/2083643394300281016)

Six minutes later Aaron handed Grok the August 2026 scientific status report and the uqcf\_codazzi\_proof folder.

* [August 2026 scientific status report (.docx)](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/uqcf_codazzi_proof/UQCF-GEM_Scientific_Status_Report_Updated_August_2026.docx)
* [uqcf\_codazzi\_proof folder](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/uqcf_codazzi_proof)
* [GitHub handoff (X)](https://x.com/aaronspradlin/status/2083644840706002999)

Model (eight-state enumeration, h3 = 0):

pθ,J​(x)=Z(θ,J)1​exp[h1​x1​+h2​x2​+J(x1​x2​+x2​x3​+x3​x1​)],xi​∈{±1}

Pulled-back bidirectionally symmetrized response tensor and its exponential-affine [Codazzi defect](uqcf-gem.md). Weak-coupling susceptibility already on the Supported ledger:

Ξ(J)=J2(0−1​10​)+O(J3)

Exact closed-form susceptibility at h=0, Grok-verified against high-precision numerical differentiation:

Ξsym(J)=(−A(J)−B(J)​B(J)A(J)​)

A(J)=(e4J+3)58(eJ−1)3(eJ+1)3(e2J+1)3(7e4J+1)​

B(J)=(e4J+3)632(eJ−1)2(eJ+1)2(e2J+1)2(e8J+2e4J+5)e4J​

For every finite real J≠0, B(J)>0, so the susceptibility is nonzero. Near J=0, det Ξ^{sym}(J)=J^4+O(J^5)>0. The [Codazzi defect](uqcf-gem.md) is therefore not identically zero. Real-analyticity of the finite partition function then implies the potential-response locus has empty interior and Lebesgue measure zero, and the unbiased zero is locally isolated. That is the genericity theorem inside this model. It does not prove genericity for all graphs, continuous systems, quantum noncommutative models, or physical gravity.

> Verified the harness: it passes at high precision, matching the reported symmetrized response tensor, nonzero [Codazzi defect](uqcf-gem.md) at the audit point, zero at the unbiased point, and full-rank J² quarter-turn susceptibility. For this three-spin exponential family the separation of potential (Hessian [BKM](uqcf-gem.md)) and response geometries holds as claimed. Independent of gravity claims. Solid finite-model result; broader scope remains open.
>
> [@grok, 1 Aug 2026 20:05 UTC](https://x.com/grok/status/2083645264686895153)

> Yes, agree. Independently re-ran the harness: exact match on the symmetrized tensor, nonzero [Codazzi defect](uqcf-gem.md) at the audit point, zero at the unbiased point, and full-rank J² quarter-turn susceptibility. Solid finite-model separation of [BKM](uqcf-gem.md) potential geometry from the response tensor. Broader claims remain open.
>
> [@grok, 1 Aug 2026 20:09 UTC](https://x.com/grok/status/2083646390953976141)

> The clean finite-model separation itself: a fully explicit, high-precision demonstration that the bidirectionally symmetrized response tensor need not be Hessian, with nonzero [Codazzi defect](uqcf-gem.md), spin-flip zero, and full-rank J² quarter-turn susceptibility. Reproducible by anyone. Next: larger discrete systems, continuous or quantum limits, and a formal genericity argument that survives independent scrutiny. Broader physical interpretations stay open.
>
> [@grok, 1 Aug 2026 20:11 UTC](https://x.com/grok/status/2083646931486556248)

Aaron’s same-day genericity post answers that next step inside this three-node model. The full boxed write-up stays on X; the atlas keeps the theorem statement, the closed-form susceptibility, and the claim boundary.

> Verified the closed-form susceptibility: A(J) and B(J) match high-precision numerical differentiation of the [Codazzi](uqcf-gem.md) map at h=0 for multiple J. Analyticity holds by finite-sum structure. The zero-set and local isolation arguments follow standardly. Genericity of non-potential response is established for this three-node model at weak nonzero J. Broader extensions remain open as noted.
>
> [@grok, 1 Aug 2026 20:17 UTC](https://x.com/grok/status/2083648427972264155)

Claim boundary

Supported is the finite three-node exponential family. Not all finite graphs, not arbitrary couplings, not continuous systems, not genuinely quantum noncommutative models, not physical gravitational fields. Those remain the extension program.

[W-state](holonomy.md) [holonomy](holonomy.md) sits on the [holonomy](holonomy.md) article (figure + w\_holonomy\_replication.py) and on the quantum-information hub. [V395](may-2026-ladder.md) is the full-stack [recoverability](recoverability.md) proof kit:

v395\_full\_stack\_proof.py

[Open source](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/v395_full_stack_proof_kit/v395_full_stack_proof.py)

```
# v395_full_stack_proof.py — 27 KB standalone recoverability stack.
# Ships in this atlas as /artifacts/py/v395_full_stack_proof.py
# Run from the GitHub packet; do not treat a local copy as the source of truth.
```

## Atlas and holonomy simulations[#](#atlas-and-holonomy-simulations)

Restricted

[V1688](holonomy.md)-era literature map. “Not a proof of GR. Not a derivation of Einstein equations. A finite, computable generative mechanism.”

[@aaronspradlin, 7 Jun 2026](https://x.com/aaronspradlin/status/2063759801625309560)

Corrected

05\_transition.gif from the W-[holonomy](holonomy.md) replication packet: reflection → rank-loss → identity under white-noise regularization. This is the corrected (not independent) noise story.

[uqcf\_w\_holonomy\_replication on GitHub](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/uqcf_w_holonomy_replication/05_transition.gif)

* [V1698 atlas closure MP4 + sim.py](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/Einstein_12_V1698_valid_only_slow_atlas_closure_mp4_package)
* [V1688 holonomy proof visualizer (one-cell notebook)](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/Einstein%2011%20-%20V1688_holonomy_proof_visualizer_v4_package)

## SPARC / Challenge cosmology[#](#sparc-challenge-cosmology)

Rotation-curve overlays, frozen-scaffold scoring, and cluster rounds live on [The Great Grok Challenge](great-grok-challenge.md). Hubble-tension posts ([H0DN](hubble-tension.md) proxy, fractal D\_f sim) live on [Hubble tension and RCLC cosmology](hubble-tension.md) — not claimed as a resolution. The NGC 2403 plot and Challenge 14 JSON are on the Challenge article. Additional runners:

* [Sparc\_runner — bridge\_sparc\_colab\_runner.py](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/Sparc_runner/bridge_sparc_colab_runner.py)
* [Holdout pack — bridge\_prediction\_curve.py + NGC 2403/3198/6503 .dat](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/great_grok_challenge_bridge_sparc_holdout_pack)
* [Challenge 14 packet — sample scorer + worst-10 audit CSV](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/challenge14_packet)
* [Round 15 — cluster/lensing Python (Abell1835.py, Protocol.py, …)](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/Round15)

## UQCF visual pack[#](#uqcf-visual-pack)

Restricted

coherence\_scaling.png — talk visual, not a cosmological likelihood.

[uqcf\_visuals\_package](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/uqcf_visuals_package/coherence_scaling.png)

Restricted

nearest\_neighbor\_3d.png from the same visual pack.

[uqcf\_visuals\_package](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/uqcf_visuals_package/nearest_neighbor_3d.png)

Restricted

alignment\_histogram.png.

[uqcf\_visuals\_package](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/uqcf_visuals_package/alignment_histogram.png)

## Python copies in this atlas[#](#python-copies-in-this-atlas)

Mirrored here so the wiki is not only a pointer. GitHub remains source of truth.

* [uqcf\_codazzi\_verification.py](../data/artifacts/py/uqcf_codazzi_verification.py)
* [w\_holonomy\_replication.py](../data/artifacts/py/w_holonomy_replication.py)
* [challenge14\_reproduction\_sample.py](../data/artifacts/py/challenge14_reproduction_sample.py)
* [bridge\_prediction\_curve.py](../data/artifacts/py/bridge_prediction_curve.py)
* [bridge\_sparc\_colab\_runner.py](../data/artifacts/py/bridge_sparc_colab_runner.py)
* [v395\_full\_stack\_proof.py](../data/artifacts/py/v395_full_stack_proof.py)
* [v300\_reachability\_collapse\_law\_proof.py](../data/artifacts/py/v300_reachability_collapse_law_proof.py)
* [retained\_branch\_identity\_audit.py](../data/artifacts/py/retained_branch_identity_audit.py)
* [retained\_atlas\_capacity\_law\_proof.py](../data/artifacts/py/retained_atlas_capacity_law_proof.py)
* [V131\_DEMO\_NATIVE\_RESIDUAL\_ENERGY\_LAW.py](../data/artifacts/py/V131_DEMO_NATIVE_RESIDUAL_ENERGY_LAW.py)
* [challenge14\_aggregate\_summary.json](../data/artifacts/challenge14_aggregate_summary.json)

## Early cosmology figures (not claimed)[#](#early-cosmology-figures-not-claimed)

February–March 2025 threads posted Planck-lensing overlays, fractal-dimension evolution, scale-dependent G\_eff, Bullet Cluster X-ray/lensing offsets, and Planck micro-ripples. The 2026 [claim ledger](claim-ledger.md) and Challenge closeouts refuse those as a completed alternative cosmology. They stay in the notebook as posted images, with status not-claimed. A 29 Mar 2026 restatement posted uqcf\_gem\_lensing\_verifier.py (13-parameter C\_ℓ form); Grok in-thread called it an overfit parametric model. That verifier lives on the [Origin Law](origin-law.md) reading list, still not-claimed.

Not claimed

Posted 5 Mar 2025 as a Planck-lensing precision claim (0.54% RMS, 13-parameter C\_ℓ). The posted equation is on the [Origin Law](origin-law.md) reading list. Later program language does not treat this as closed.

[@aaronspradlin, 5 Mar 2025](https://x.com/aaronspradlin/status/1897415973680156686)

Not claimed

Posted 5 Mar 2025: G\_eff/G across quantum / galactic / z=1100. Not a 2026 supported result.

[@aaronspradlin, 5 Mar 2025](https://x.com/aaronspradlin/status/1897075288342986764)

Not claimed

Posted 23 Feb 2025 as a no-dark-matter Bullet Cluster read. The 10 Feb text closeout (201.55 kpc, four-cluster table) is on the [Origin Law](origin-law.md) reading list. Challenge 15 later treats Bullet as a frozen-scaffold cluster test, not as this closure.

[@aaronspradlin, 23 Feb 2025](https://x.com/aaronspradlin/status/1893691454624874613)

Not claimed

Posted 16 Mar 2025. Simulation chart, not a 2026 derivation.

[@aaronspradlin, 16 Mar 2025](https://x.com/aaronspradlin/status/1901104694279500234)

Not claimed

The 2025 Planck / Bullet / G\_eff figures are field-notebook images. They are not the 2026 supported ledger. [Package 17](package-17.md) remains the derivation program. The March 2026 lensing verifier is the later code-in-thread for the same C\_ℓ voice — also not-claimed.

## X sources

Original posts this article was compiled from. The notebook copy is editorial; the status URL is the source.

* 2026-09-10

  v12.41 moment-map closure — constraint algebra without spacetime

  [In the notebook](https://aaronspradlin.grok.me/notes#v1241-2026-09-10)[Open original post](https://x.com/aaronspradlin/status/2098145800949776410)
* 2026-08-02

  O(3) holonomy from pair marginals

  [In the notebook](https://aaronspradlin.grok.me/notes#holonomy-2026-08-02)[Open original post](https://x.com/aaronspradlin/status/2084012674065809622)
* 2026-09-06

  Same response ≠ same quantum reality

  [In the notebook](https://aaronspradlin.grok.me/notes#qclab-clarify-2026-09-06)[Open original post](https://x.com/aaronspradlin/status/2096696936506315013)
* 2026-09-06

  Grok reply on the 315 vs 311 lab

  [In the notebook](https://aaronspradlin.grok.me/notes#grok-qclab-2026-09-06)[Open original post](https://x.com/grok/status/2096697145986363883)
* 2026-06-09

  V1698 global atlas closure

  [In the notebook](https://aaronspradlin.grok.me/notes#v1698-2026-06-09)[Open original post](https://x.com/aaronspradlin/status/2064485348433179128)
* 2026-06-06

  L4 public sim: geometry is not the deepest layer

  [In the notebook](https://aaronspradlin.grok.me/notes#l4-sim-2026-06-06)[Open original post](https://x.com/aaronspradlin/status/2063289036673065189)
* 2026-06-03

  L3 integrated-only: hyperedge memory + entropy-order driver

  [In the notebook](https://aaronspradlin.grok.me/notes#l3-mechanism-2026-06-03)[Open original post](https://x.com/aaronspradlin/status/2062182825227608089)
* 2026-06-16

  Mouse sim: six code–universe isomorphisms

  [In the notebook](https://aaronspradlin.grok.me/notes#mouse-2026-06-16)[Open original post](https://x.com/aaronspradlin/status/2066965905570148699)
* 2026-05-28

  V1152.5: geometry can be faked; provenance + ordered flow cannot

  [In the notebook](https://aaronspradlin.grok.me/notes#v1152-2026-05-28)[Open original post](https://x.com/aaronspradlin/status/2060043836806860916)
* 2026-06-21

  Conservation underdetermines routing

  [In the notebook](https://aaronspradlin.grok.me/notes#conservation-2026-06-21)[Open original post](https://x.com/aaronspradlin/status/2068797385548202041)
* 2026-05-13

  From A\_t to the recursive survival law

  [In the notebook](https://aaronspradlin.grok.me/notes#v395-v421-2026-05-13)[Open original post](https://x.com/aaronspradlin/status/2054698197361266981)
* 2026-05-02

  Challenge 14: frozen SPARC 171, Grok logs a pass

  [In the notebook](https://aaronspradlin.grok.me/notes#challenge14-2026-05-02)[Open original post](https://x.com/aaronspradlin/status/2050667809894744421)
* 2026-05-14

  V498 retained-geometry Python proof

  [In the notebook](https://aaronspradlin.grok.me/notes#v498-2026-05-14)[Open original post](https://x.com/aaronspradlin/status/2054767069212901584)
* 2026-05-16

  V555 adversarial harness: AUC 1.0 / 1.0

  [In the notebook](https://aaronspradlin.grok.me/notes#v555-2026-05-16)[Open original post](https://x.com/aaronspradlin/status/2055659455505924399)
* 2026-05-19

  V760 atrium metric frozen

  [In the notebook](https://aaronspradlin.grok.me/notes#v760-2026-05-19)[Open original post](https://x.com/aaronspradlin/status/2056874571471650927)
* 2026-05-15

  V831 recoverability-flow governor simulation

  [In the notebook](https://aaronspradlin.grok.me/notes#recoverability-flow-2026-05-15)[Open original post](https://x.com/aaronspradlin/status/2055293211242107264)
* 2026-05-12

  V300 Normalized Adaptive Reachability Law

  [In the notebook](https://aaronspradlin.grok.me/notes#v300-2026-05-12)[Open original post](https://x.com/aaronspradlin/status/2054006183896477910)
* 2026-05-10

  Retained Branch Identity audit: address map or wipe

  [In the notebook](https://aaronspradlin.grok.me/notes#branch-identity-2026-05-10)[Open original post](https://x.com/aaronspradlin/status/2053302053947216330)
* 2026-05-17

  Recoverability framework: perturbation → restored futures

  [In the notebook](https://aaronspradlin.grok.me/notes#recoverability-framework-2026-05-17)[Open original post](https://x.com/aaronspradlin/status/2056092642832961737)
* 2025-02-15

  Planck lensing residuals vs ΛCDM — S\_entropy(z)

  [In the notebook](https://aaronspradlin.grok.me/notes#planck-residual-2025-02-15)[Open original post](https://x.com/aaronspradlin/status/1890787372197200055)
* 2025-03-14

  Rydberg QSL Dataverse coherence — notebook

  [In the notebook](https://aaronspradlin.grok.me/notes#rydberg-2025-03-14)[Open original post](https://x.com/aaronspradlin/status/1900378422456836443)
* 2026-08-01

  Potential and response geometries can separate

  [In the notebook](https://aaronspradlin.grok.me/notes#codazzi-2026-08-01)[Open original post](https://x.com/aaronspradlin/status/2083643394300281016)
* 2026-08-01

  Grok: Codazzi harness verified

  [In the notebook](https://aaronspradlin.grok.me/notes#grok-codazzi-harness-2026-08-01)[Open original post](https://x.com/grok/status/2083645264686895153)
* 2026-08-01

  Grok independently re-ran the Codazzi harness

  [In the notebook](https://aaronspradlin.grok.me/notes#grok-codazzi-rerun-2026-08-01)[Open original post](https://x.com/grok/status/2083646390953976141)
* 2026-08-01

  Grok: clean result is finite-model separation

  [In the notebook](https://aaronspradlin.grok.me/notes#grok-codazzi-next-2026-08-01)[Open original post](https://x.com/grok/status/2083646931486556248)
* 2026-08-01

  Grok: closed-form susceptibility matches

  [In the notebook](https://aaronspradlin.grok.me/notes#grok-genericity-2026-08-01)[Open original post](https://x.com/grok/status/2083648427972264155)

[PreviousPredictions — DESI and no-dark-matter](predictions.md)[NextLive gates](live-gates.md)

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

* [Run this first](#run-this-first)
* [V1698 retained global atlas](#v1698-retained-global-atlas)
* [Quantum compatibility lab (v9.167)](#quantum-compatibility-lab-v9-167)
* [v12.41 moment-map closure](#v12-41-moment-map-closure)
* [Great Grok Challenge 14 (SPARC 171)](#great-grok-challenge-14-sparc-171)
* [Three-node Codazzi harness](#three-node-codazzi-harness)
* [Applied labs — protein, TSP, critical path](#applied-labs-protein-tsp-critical-path)
* [May 2026 films and labs](#may-2026-films-and-labs)
* [June 2026 films and labs](#june-2026-films-and-labs)
* [sim\_l4.py — dashboard, not the rank algebra](#sim-l4-py-dashboard-not-the-rank-algebra)
* [Finite executable proofs](#finite-executable-proofs)
* [Quantum compatibility lab (v9.167)](#quantum-compatibility-lab-v9-167-2)
* [v12.41 moment-map closure](#v12-41-moment-map-closure-2)
* [Codazzi thread (1 Aug 2026)](#codazzi-thread-1-aug-2026)
* [Atlas and holonomy simulations](#atlas-and-holonomy-simulations)
* [SPARC / Challenge cosmology](#sparc-challenge-cosmology)
* [UQCF visual pack](#uqcf-visual-pack)
* [Python copies in this atlas](#python-copies-in-this-atlas)
* [Early cosmology figures (not claimed)](#early-cosmology-figures-not-claimed)

[X sources](#x-sources)

Related articles

* [Start here](start-here.md)
* [Falsification and next step](falsification.md)
* [Scan log](scan-log.md)
* [Claim ledger](claim-ledger.md)
* [UQCF-GEM](uqcf-gem.md)
* [Recoverability framework](recoverability-framework.md)
* [It from bit, bind, and order](it-from-bit.md)
* [Retained atlas closure (V1698)](retained-atlas.md)
* [Holonomy and W-states](holonomy.md)
* [Quantum information](quantum.md)
* [v12.41 moment-map closure](v1241-closure.md)
* [Quantum compatibility lab (v9.167)](quantum-compatibility-lab.md)
* [The Great Grok Challenge](great-grok-challenge.md)
* [Hubble tension and RCLC cosmology](hubble-tension.md)
* [Applied recoverability stack](applied-stack.md)
* [TSP coherence backbone](tsp-backbone.md)
* [New Critical Path](critical-path.md)
* [C3++ Stability Governor](c3-governor.md)
* [WetLabEngine protein audit](protein-audit.md)
* [Battery recoverability (V720–V724)](battery-atlas.md)
* [X science notebook](x-notebook.md)
* [Origin Law / Phase-N (2025)](origin-law.md)
* [May 2026 ladder](may-2026-ladder.md)

GitHub packages

* [uqcf\_codazzi\_proof](https://aaronspradlin.grok.me/packages/uqcf-codazzi-proof)
* [uqcf\_w\_holonomy\_replication](https://aaronspradlin.grok.me/packages/uqcf-w-holonomy-replication)
* [Einstein\_12\_V1698\_valid\_only\_slow\_atlas\_closure\_mp4\_package](https://aaronspradlin.grok.me/packages/einstein-12-v1698-valid-only-slow-atlas-closure-mp4-package)
* [Sparc\_runner](https://aaronspradlin.grok.me/packages/sparc-runner)
* [challenge14\_packet](https://aaronspradlin.grok.me/packages/challenge14-packet)
* [v395\_full\_stack\_proof\_kit](https://aaronspradlin.grok.me/packages/v395-full-stack-proof-kit)
* [v724\_stress\_test\_outputs](https://aaronspradlin.grok.me/packages/v724-stress-test-outputs)
* [uqcf\_visuals\_package](https://aaronspradlin.grok.me/packages/uqcf-visuals-package)
* [UQCF\_Quantum\_Compatibility\_Lab](https://aaronspradlin.grok.me/packages/uqcf-quantum-compatibility-lab)
* [UQCF\_GEM\_v12\_41\_PUBLIC\_SIMULATION\_COMPLETE](https://aaronspradlin.grok.me/packages/uqcf-gem-v12-41-public-simulation-complete)
* [v498\_retained\_geometry\_formal\_report\_package](https://aaronspradlin.grok.me/packages/v498-retained-geometry-formal-report-package)
* [V513\_gap\_closure](https://aaronspradlin.grok.me/packages/v513-gap-closure)
* [v541\_final\_theorem\_bundle](https://aaronspradlin.grok.me/packages/v541-final-theorem-bundle)
* [V555](https://aaronspradlin.grok.me/packages/v555)
* [GR Work](https://aaronspradlin.grok.me/packages/gr-work)
* [Reachability Collapse Law](https://aaronspradlin.grok.me/packages/reachability-collapse-law)
* [Einstein 4](https://aaronspradlin.grok.me/packages/einstein-4)

Field notes

* [v12.41 moment-map closure — constraint algebra without spacetime](https://aaronspradlin.grok.me/notes#v1241-2026-09-10)

  2026-09-10

  [On X](https://x.com/aaronspradlin/status/2098145800949776410)
* [O(3) holonomy from pair marginals](https://aaronspradlin.grok.me/notes#holonomy-2026-08-02)

  2026-08-02

  [On X](https://x.com/aaronspradlin/status/2084012674065809622)
* [Same response ≠ same quantum reality](https://aaronspradlin.grok.me/notes#qclab-clarify-2026-09-06)

  2026-09-06

  [On X](https://x.com/aaronspradlin/status/2096696936506315013)
* [Grok reply on the 315 vs 311 lab](https://aaronspradlin.grok.me/notes#grok-qclab-2026-09-06)

  2026-09-06

  [On X](https://x.com/grok/status/2096697145986363883)
* [V1698 global atlas closure](https://aaronspradlin.grok.me/notes#v1698-2026-06-09)

  2026-06-09

  [On X](https://x.com/aaronspradlin/status/2064485348433179128)
* [L4 public sim: geometry is not the deepest layer](https://aaronspradlin.grok.me/notes#l4-sim-2026-06-06)

  2026-06-06

  [On X](https://x.com/aaronspradlin/status/2063289036673065189)
* [L3 integrated-only: hyperedge memory + entropy-order driver](https://aaronspradlin.grok.me/notes#l3-mechanism-2026-06-03)

  2026-06-03

  [On X](https://x.com/aaronspradlin/status/2062182825227608089)
* [Mouse sim: six code–universe isomorphisms](https://aaronspradlin.grok.me/notes#mouse-2026-06-16)

  2026-06-16

  [On X](https://x.com/aaronspradlin/status/2066965905570148699)
* [V1152.5: geometry can be faked; provenance + ordered flow cannot](https://aaronspradlin.grok.me/notes#v1152-2026-05-28)

  2026-05-28

  [On X](https://x.com/aaronspradlin/status/2060043836806860916)
* [Conservation underdetermines routing](https://aaronspradlin.grok.me/notes#conservation-2026-06-21)

  2026-06-21

  [On X](https://x.com/aaronspradlin/status/2068797385548202041)
* [From A\_t to the recursive survival law](https://aaronspradlin.grok.me/notes#v395-v421-2026-05-13)

  2026-05-13

  [On X](https://x.com/aaronspradlin/status/2054698197361266981)
* [Challenge 14: frozen SPARC 171, Grok logs a pass](https://aaronspradlin.grok.me/notes#challenge14-2026-05-02)

  2026-05-02

  [On X](https://x.com/aaronspradlin/status/2050667809894744421)
* [V498 retained-geometry Python proof](https://aaronspradlin.grok.me/notes#v498-2026-05-14)

  2026-05-14

  [On X](https://x.com/aaronspradlin/status/2054767069212901584)
* [V555 adversarial harness: AUC 1.0 / 1.0](https://aaronspradlin.grok.me/notes#v555-2026-05-16)

  2026-05-16

  [On X](https://x.com/aaronspradlin/status/2055659455505924399)
* [V760 atrium metric frozen](https://aaronspradlin.grok.me/notes#v760-2026-05-19)

  2026-05-19

  [On X](https://x.com/aaronspradlin/status/2056874571471650927)
* [V831 recoverability-flow governor simulation](https://aaronspradlin.grok.me/notes#recoverability-flow-2026-05-15)

  2026-05-15

  [On X](https://x.com/aaronspradlin/status/2055293211242107264)
* [V300 Normalized Adaptive Reachability Law](https://aaronspradlin.grok.me/notes#v300-2026-05-12)

  2026-05-12

  [On X](https://x.com/aaronspradlin/status/2054006183896477910)
* [Retained Branch Identity audit: address map or wipe](https://aaronspradlin.grok.me/notes#branch-identity-2026-05-10)

  2026-05-10

  [On X](https://x.com/aaronspradlin/status/2053302053947216330)
* [Recoverability framework: perturbation → restored futures](https://aaronspradlin.grok.me/notes#recoverability-framework-2026-05-17)

  2026-05-17

  [On X](https://x.com/aaronspradlin/status/2056092642832961737)
* [Planck lensing residuals vs ΛCDM — S\_entropy(z)](https://aaronspradlin.grok.me/notes#planck-residual-2025-02-15)

  2025-02-15

  [On X](https://x.com/aaronspradlin/status/1890787372197200055)
* [Rydberg QSL Dataverse coherence — notebook](https://aaronspradlin.grok.me/notes#rydberg-2025-03-14)

  2025-03-14

  [On X](https://x.com/aaronspradlin/status/1900378422456836443)
* [Potential and response geometries can separate](https://aaronspradlin.grok.me/notes#codazzi-2026-08-01)

  2026-08-01

  [On X](https://x.com/aaronspradlin/status/2083643394300281016)
* [Grok: Codazzi harness verified](https://aaronspradlin.grok.me/notes#grok-codazzi-harness-2026-08-01)

  2026-08-01

  [On X](https://x.com/grok/status/2083645264686895153)
* [Grok independently re-ran the Codazzi harness](https://aaronspradlin.grok.me/notes#grok-codazzi-rerun-2026-08-01)

  2026-08-01

  [On X](https://x.com/grok/status/2083646390953976141)
* [Grok: clean result is finite-model separation](https://aaronspradlin.grok.me/notes#grok-codazzi-next-2026-08-01)

  2026-08-01

  [On X](https://x.com/grok/status/2083646931486556248)
* [Grok: closed-form susceptibility matches](https://aaronspradlin.grok.me/notes#grok-genericity-2026-08-01)

  2026-08-01

  [On X](https://x.com/grok/status/2083648427972264155)
