---
title: "v12.41 moment-map closure"
route: "/wiki/v1241-closure"
source: "https://aaronspradlin.grok.me/wiki/v1241-closure"
description: "Qubit Kirillov–Kostant–Souriau identity: quantum relations → symplectic generators → closed constraint algebra. 121-step public simulation. Restricted finite calc. Gravity’s constraints not identified."
date: "2026-09-10"
claimStatus: "restricted"
tags: ["Astra", "v12.41", "constraint algebra", "symplectic", "moment map"]
dek: "Qubit Kirillov–Kostant–Souriau identity: quantum relations → symplectic generators → closed constraint algebra. 121-step public simulation. Restricted finite calc. Gravity’s constraints not identified."
---

[Wiki](index.md)

# v12.41 moment-map closure

Qubit Kirillov–Kostant–Souriau identity: quantum relations → symplectic generators → closed constraint algebra. 121-step public simulation. Restricted finite calc. Gravity’s constraints not identified.

00 Astra · Result · Restricted · 2026-09-10 · compiled 2026-10-10 · 3 min read · 2 claims · [5 X sources](#x-sources)

[Original on X](https://x.com/aaronspradlin/status/2098145800949776410) · [Package: UQCF\_GEM\_v12\_41\_PUBLIC\_SIMULATION\_COMPLETE](../packages/uqcf-gem-v12-41-public-simulation-complete.md) · [JSON](../data/page/v1241-closure.json) · [Cite](../cite.txt)

Astra · v12.41 · constraint algebra · symplectic · moment map

On this page

*   [The posted chain](#the-posted-chain)
*   [What the 121-step run actually shows](#what-the-121-step-run-actually-shows)
*   [Run this first](#run-this-first)
*   [The week that led here (7–9 Sep)](#the-week-that-led-here-7-9-sep)

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

Posted 10 Sep 2026 20:25 UTC with a five-second film. GitHub packet Tmp/TOE/UQCF\_GEM\_v12\_41\_PUBLIC\_SIMULATION\_COMPLETE landed eight minutes earlier (commit v12\_41). ChatGPT-5.6 [Astra](astra.md) derived the chain; the public simulation is a qubit density matrix swept through 121 ordered unitary relational transforms. This compile independently reconstructed the core: max exact residual 0, max broken residual 0.297. Not Einstein constraints. Not ADM. λ is an index, not physical time.

> This is not a claim that [Astra](astra.md) derived gravity. Gravity’s constraints have not been identified yet. But we no longer have to assume that a constraint algebra must begin with spacetime.
>
> [@aaronspradlin, 10 Sep 2026](https://x.com/aaronspradlin/status/2098145800949776410)

## The posted chain {#the-posted-chain}

<div class="ra-math"><span class="katex-display"><span class="katex"><span aria-hidden="true" class="katex-html"><span class="katex-base"><span class="katex-strut" style="height:1.0361em;vertical-align:-0.2861em;"></span><span class="mord"><span class="mord">Ω</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1514em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">ρ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathnormal">A</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal" style="margin-right:0.0502em;">B</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">−</span><span class="mord mathnormal">i</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathrm">Tr</span></span><span class="mopen">(</span><span class="mord mathnormal">ρ</span><span class="mopen">[</span><span class="mord mathnormal">A</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal" style="margin-right:0.0502em;">B</span><span class="mclose">])</span></span></span></span></span></div>

<div class="ra-math"><span class="katex-display"><span class="katex"><span aria-hidden="true" class="katex-html"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0715em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:-0.0715em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">A</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathnormal">ρ</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord mathrm">Tr</span></span><span class="mopen">(</span><span class="mord mathnormal">ρ</span><span class="mord mathnormal">A</span><span class="mclose">)</span></span></span></span></span></div>

<div class="ra-math"><span class="katex-display"><span class="katex"><span aria-hidden="true" class="katex-html"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0715em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:-0.0715em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">A</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0715em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:-0.0715em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0502em;">B</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">}</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1.0385em;vertical-align:-0.3552em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0715em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3448em;"><span style="top:-2.5198em;margin-left:-0.0715em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathnormal mtight">i</span><span class="mopen mtight">[</span><span class="mord mathnormal mtight">A</span><span class="mpunct mtight">,</span><span class="mord mathnormal mtight" style="margin-right:0.0502em;">B</span><span class="mclose mtight">]</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.3552em;"><span></span></span></span></span></span></span></span></span></span></span></div>

On Pauli generators the last line is the su(2) moment-map identity \{C\_x, C\_y\} = 2 C\_z, because −i[σ\_x, σ\_y] = 2 σ\_z. The public script checks that identity on a mixed qubit seed conjugated by U\_z(0.55λ) U\_y(0.35λ) U\_x(0.20λ) at 121 values of λ ∈ [0, 2π].

<video class="w-full max-w-full bg-elevated" controls="" playsinline="" poster="../../artifacts/v1241-verification.png" style="max-width:100%"><source src="../../artifacts/v1241-simulation.mp4" type="video/mp4"/></video>

Restricted

Posted public simulation: Bloch / moment-map coordinates, C\_A traces, exact residual vs deliberately broken generator law. Ordered relational sweep — not a gravitational orbit.

[v1241\_public\_simulation.mp4 · GitHub packet](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/UQCF_GEM_v12_41_PUBLIC_SIMULATION_COMPLETE/outputs/v1241_public_simulation.mp4)

## What the 121-step run actually shows {#what-the-121-step-run-actually-shows}
| Quantity | Posted log | This compile |
| --- | --- | --- |
| steps | 121 | 121 |
| max exact Δ\_closure | 0 | 0 |
| max broken Δ\_closure | 0.297 | 0.297 |
| min density eigenvalue | 0.2508 | 0.2508 |
| purity (constant) | 0.6242 | 0.6242 |

Broken control is 1.25 C\_z + 0.15 C\_x in place of 2 C\_z. Exact residual stays at machine zero; the broken law does not. Independent reconstruction used the posted seed, not the author’s Python import.

Live reconstruction on this page

The canvas below the article is a browser rebuild of the same Pauli core. It is a teaching toy. The posted MP4, PNG, and CSV remain the artifacts. This compile independently reconstructed max exact residual 0 and max broken residual 0.297.

![Exact quantum closure residual sitting on zero versus a broken-control residual that stays O(0.1)](../artifacts/v1241-verification.png)

Restricted

Posted verification plot. Vertical axis is closure residual on a symlog scale. Exact branch is the quantum generator law; broken branch contaminates the structure coefficients.

[v1241\_public\_simulation\_verification.png · GitHub packet](https://github.com/proteinfoldingengine/WetLabEngine/blob/main/Tmp/TOE/UQCF_GEM_v12_41_PUBLIC_SIMULATION_COMPLETE/outputs/v1241_public_simulation_verification.png)

Restricted

On the posted 121-step qubit sweep, the KKS / Pauli moment-map identity closes with Δ\_closure = 0. Deliberately breaking the generator law yields Δ\_closure > 0 (max 0.297). Finite quantum construction. Not a derivation of gravity, ADM, or Einstein constraints.

[Source on X](https://x.com/aaronspradlin/status/2098145800949776410)

## Run this first {#run-this-first}
Clone the public packet

[Open source](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/UQCF_GEM_v12_41_PUBLIC_SIMULATION_COMPLETE)

```
git clone --depth 1 https://github.com/proteinfoldingengine/WetLabEngine.git
cd WetLabEngine/Tmp/TOE/UQCF_GEM_v12_41_PUBLIC_SIMULATION_COMPLETE
python test_uqcf_v1241_public_sim.py
python uqcf_v1241_public_sim.py
```

uqcf\_v1241\_public\_sim.py — exact vs broken residual

[Open source](../artifacts/py/uqcf_v1241_public_sim.py)

```
def exact_closure_residual(rho):
    sx, sy, sz = paulis()
    lhs = kks_bracket(rho, sx, sy)          # -i Tr(ρ [σx, σy])
    rhs = 2.0 * moment_map(rho, sz)         # C_{-i[σx,σy]} = 2 C_z
    return abs(lhs - rhs)

def broken_closure_residual(rho):
    sx, sy, sz = paulis()
    lhs = kks_bracket(rho, sx, sy)
    rhs = 1.25 * moment_map(rho, sz) + 0.15 * moment_map(rho, sx)
    return abs(lhs - rhs)
```

What a successful run does not show

It does not identify the gravitational constraint algebra. It does not introduce ADM, Einstein equations, or fundamental time. The sweep parameter λ is an ordered family of relational transformations. The broken control is an internal null, not a physical perturbation.

## The week that led here (7–9 Sep) {#the-week-that-led-here-7-9-sep}
v12.41 is the simulation. The three [Astra](astra.md) posts immediately before it stay on X (no matching GitHub packet in this compile). They are the questions the simulation does not close.

*   7 Sep — [UQCF](uqcf-gem.md)–GEM [v9.190](quantum-compatibility-lab.md): exact reconstruction of the affine map γ(x) = u + Lx from eleven source settings (110 real coefficients) on a nonsingular domain. Distinguishes γ(x) = g x from offsets, unequal gains, and cross-coupling. Exact model numerics. Physical source law open.
*   8 Sep — conditional principle: each matter sector already has K\_α = g\_α n J\_α(t\_α). Quantum consistency does not force g\_1 = g\_2 = ⋯. One signed source coefficient before sector specialization, K\_α^U = [g\_★](astra.md) n J\_α(t\_α) ∀α, is the unique [protected-source response](uqcf-gem-reader.md) that survives erasure of matter-sector labels. Author: not yet a derivation of gravity.
*   9 Sep — [N-cycle](astra.md) difference operator: σ\_min^+([D\_N](astra.md)) = 2 sin(π/N). Bare inverse ~ N/(2π); after geometry supplies h = 1/N the inverse converges to 1/(2π). No fitted force law. Gravity connection still open.

Open

The gravitational constraint algebra has not been identified. v12.41 shows a constraint algebra can start from quantum relations on a qubit. Mapping that algebra onto [g\_★](astra.md), the [D\_N](astra.md) continuum seed, or Einstein/ADM remains open.

[Source on X](https://x.com/aaronspradlin/status/2098145800949776410)

*   [X post (10 Sep, video)](https://x.com/aaronspradlin/status/2098145800949776410)
*   [GitHub public simulation packet](https://github.com/proteinfoldingengine/WetLabEngine/tree/main/Tmp/TOE/UQCF_GEM_v12_41_PUBLIC_SIMULATION_COMPLETE)
*   [Vendored Python](../artifacts/py/uqcf_v1241_public_sim.py)
*   [Diagnostics CSV](../artifacts/v1241-diagnostics.csv)
*   [Astra identities (F, t\*, d(t))](astra.md)
*   [Quantum compatibility lab (v9.167 / v9.190)](quantum-compatibility-lab.md)
*   [Emergent gravity (still a candidate)](emergent-gravity.md)

Live reconstruction

Restricted

### 121-step moment-map closure

Same qubit seed and generator law as the posted GitHub script. Exact residual must stay at 0; the broken control must not. This canvas is a teaching toy — the posted MP4 and CSV remain the artifacts.

step 120/120 · Δ\_exact 0.0e+0 · Δ\_broken 0.203 · this compile max exact 0.0e+0 · max broken 0.297

<span id="x-sources"></span>

## X sources

Original posts this article was compiled from. The notebook copy is editorial; the status URL is the source.

*   2026-09-10

    v12.41 moment-map closure — constraint algebra without spacetime

    [In the notebook](../notes.md#v1241-2026-09-10) · [Open original post](https://x.com/aaronspradlin/status/2098145800949776410)

*   2026-09-09

    N-cycle inverse converges after geometry-supplied scale

    [In the notebook](../notes.md#dn-scale-2026-09-09) · [Open original post](https://x.com/aaronspradlin/status/2097526717262762012)

*   2026-09-08

    Universal source coefficient g\_★ before sector specialization

    [In the notebook](../notes.md#gstar-2026-09-08) · [Open original post](https://x.com/aaronspradlin/status/2097384034037105091)

*   2026-09-07

    UQCF–GEM v9.190 affine source reconstruction

    [In the notebook](../notes.md#v9190-2026-09-07) · [Open original post](https://x.com/aaronspradlin/status/2097030907198906776)

*   2026-09-06

    Same response ≠ same quantum reality

    [In the notebook](../notes.md#qclab-clarify-2026-09-06) · [Open original post](https://x.com/aaronspradlin/status/2096696936506315013)

[Previous Astra (pre–Genesis Pin)](astra.md)[Next Compatibility lab](compatibility-lab.md)

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

*   [The posted chain](#the-posted-chain)
*   [What the 121-step run actually shows](#what-the-121-step-run-actually-shows)
*   [Run this first](#run-this-first)
*   [The week that led here (7–9 Sep)](#the-week-that-led-here-7-9-sep)

[X sources](#x-sources)

Related articles

*   [Claim ledger](claim-ledger.md)
*   [Quantum information](quantum.md)
*   [Astra (pre–Genesis Pin)](astra.md)
*   [Quantum compatibility lab (v9.167)](quantum-compatibility-lab.md)
*   [Emergent gravity (candidate)](emergent-gravity.md)
*   [Package 17 — derivation program](package-17.md)
*   [Proofs, simulations, and figures](proofs-and-simulations.md)

GitHub packages

*   [UQCF\_GEM\_v12\_41\_PUBLIC\_SIMULATION\_COMPLETE](../packages/uqcf-gem-v12-41-public-simulation-complete.md)

Field notes

*   [v12.41 moment-map closure — constraint algebra without spacetime](../notes.md#v1241-2026-09-10)

    2026-09-10

    [On X](https://x.com/aaronspradlin/status/2098145800949776410)

*   [N-cycle inverse converges after geometry-supplied scale](../notes.md#dn-scale-2026-09-09)

    2026-09-09

    [On X](https://x.com/aaronspradlin/status/2097526717262762012)

*   [Universal source coefficient g\_★ before sector specialization](../notes.md#gstar-2026-09-08)

    2026-09-08

    [On X](https://x.com/aaronspradlin/status/2097384034037105091)

*   [UQCF–GEM v9.190 affine source reconstruction](../notes.md#v9190-2026-09-07)

    2026-09-07

    [On X](https://x.com/aaronspradlin/status/2097030907198906776)

*   [Same response ≠ same quantum reality](../notes.md#qclab-clarify-2026-09-06)

    2026-09-06

    [On X](https://x.com/aaronspradlin/status/2096696936506315013)
