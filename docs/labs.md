---
title: "Applied labs"
route: "/labs"
source: "https://aaronspradlin.grok.me/labs"
description: "Protein folding, fractal TSP, and live critical path — three Python labs on Aaron Spradlin’s recoverability operator. Restricted empirical. Unification still open."
date: "2026-09-07"
claimStatus: "restricted"
tags: ["labs", "protein", "TSP", "critical-path", "python"]
dek: "Three simulations on Aaron Spradlin’s recoverability operator. Restricted empirical. Unification still open."
---

@aaronspradlin · applied stack

# Protein · TSP · critical path

Three simulations, one operator, uniquely built on the retained-information physics — not a TSP heuristic, not a folding oracle, not a Gantt product. Runnable here as teaching toys. The posted residuals live on X and GitHub.

Restricted · Open · [Applied recoverability stack](wiki/applied-stack.md) · [Proofs & simulations](wiki/proofs-and-simulations.md)

One operator

## Remember what survived

1.  01 Preserve what remains coherent.
2.  02 Deform what is stressed.
3.  03 Reset only what became stale.

Visible state G\_t is the snapshot. Hidden retained history R\_t is why two identical snapshots can still diverge. Restricted empirical. Unification still open.

Restricted · Open

applied\_recoverability\_operator.py

```
"""Remember-what-survived. Pedagogical reconstruction of the
posted operator — not a dump of unpublished WetLabEngine source.

Visible state G_t is never enough. Hidden retained history R_t
decides what is still coherent, what is only stressed, and what
has gone stale. Same operator in protein, fractal TSP, and live
critical path. Recurrence is not a unification proof.
"""

def recover(G, R, shock, tau_lo=0.25, tau_hi=0.72):
    stress = strain(G, R, shock)          # how much the shock hits each part
    keep   = G[stress < tau_lo]           # preserve coherent commitments
    warp   = deform(G[(stress >= tau_lo) & (stress < tau_hi)], R)
    reseed = reset(G[stress >= tau_hi])   # only the stale
    return splice(keep, warp, reseed)

def strain(G, R, shock):
    # Visible mismatch plus forgotten history. G_t-only undercounts.
    return visible_gap(G, shock) * (1.0 - retained_coherence(R, shock))
```

Run the stack

## Three labs, same physics

Each canvas is a reconstruction of the posted remember-what-survived pattern. It is not the Villin HP35 harness, not the 100-point 3D residual, and not a product optimizer. Posted numbers stay boxed with their X source.

Frame 18

Restricted · 2026-04-14

### Same conformation, different fate

Two chains meet at one visible snapshot. Close-R\_t stays folded. Far-R\_t walks away. A G\_t-only read cannot tell them apart. This canvas is a teaching toy — the posted Villin HP35 numbers sit below.

Toy AUC G\_t

0.468

matched pairs, chance-ish

Toy AUC G\_t+R\_t

1.000

retained history lifts

Close drift

0.009

after snapshot

Far drift

0.274

after snapshot

Posted · Villin HP35

AUC G\_t+R\_t ≈ 0.9569 vs G\_t alone

Matched-state divergence 50.2% far-R\_t vs 1.3% close-R\_t. Restricted controlled cases. Not a folding oracle.

[Source on X](https://x.com/aaronspradlin/status/2044155484039705016)

[WetLabEngine protein audit](wiki/protein-audit.md)

What they unify under

On 10 May 2026 Aaron asked what equation sits under the protein, RCLC, critical-path, and TSP simulations, and what the work is for on top of the physics. Recurrence across posted Python labs is not a closed unification law. χ ≈ 0.2667 is not a universal applied-lab constant on this atlas.

[The 10 May question](https://x.com/aaronspradlin/status/2053553647712338040)

[Falsification sheet](wiki/falsification.md)
