"""Remember-what-survived. Pedagogical reconstruction of the
posted operator — not a dump of unpublished WetLabEngine source.

Visible state G_t is never enough. Hidden retained history R_t
decides what is still coherent, what is only stressed, and what
has gone stale. Same operator in protein, fractal TSP, and live
critical path. Recurrence is not a unification proof.

Posted residuals (restricted empirical, not this file):
  TSP 11 Apr 2026  100-point 3D cloud
    NN     length 1984.6  coherence 0.2267
    GEM    length 2492.7  coherence 0.5251  best seed 4
  Villin HP35 14 Apr 2026
    AUC(G_t + R_t) ≈ 0.9569 vs G_t alone
    matched-state divergence 50.2% far-R_t vs 1.3% close-R_t
"""

from __future__ import annotations

import math
import random
from typing import Sequence


Point = tuple[float, float]


def recover(G, R, shock, tau_lo=0.25, tau_hi=0.72):
    stress = strain(G, R, shock)
    keep = [g for g, s in zip(G, stress) if s < tau_lo]
    warp = deform([g for g, s in zip(G, stress) if tau_lo <= s < tau_hi], R)
    reseed = reset([g for g, s in zip(G, stress) if s >= tau_hi])
    return splice(keep, warp, reseed)


def strain(G, R, shock):
    # Visible mismatch plus forgotten history. G_t-only undercounts.
    return [
        visible_gap(g, shock) * (1.0 - retained_coherence(r, shock))
        for g, r in zip(G, R)
    ]


def visible_gap(g, shock) -> float:
    return min(1.0, abs(hash((repr(g), repr(shock))) % 1000) / 1000)


def retained_coherence(r, shock) -> float:
    return min(1.0, max(0.0, 0.5 + 0.5 * math.cos(hash((repr(r), repr(shock))) % 628 / 100)))


def deform(parts, R):
    return parts  # teaching stub: keep identity, mark stressed upstream


def reset(parts):
    return []  # teaching stub: drop stale commitments


def splice(*groups):
    out = []
    for g in groups:
        out.extend(g)
    return out


def dist(a: Point, b: Point) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def unit(a: Point, b: Point) -> Point:
    d = dist(a, b) or 1.0
    return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)


def tour_length(pts: Sequence[Point], tour: Sequence[int]) -> float:
    n = len(tour)
    return sum(dist(pts[tour[i]], pts[tour[(i + 1) % n]]) for i in range(n))


def tour_coherence(pts: Sequence[Point], tour: Sequence[int]) -> float:
    n = len(tour)
    if n < 3:
        return 0.0
    s = 0.0
    for i in range(n):
        u = unit(pts[tour[i]], pts[tour[(i + 1) % n]])
        v = unit(pts[tour[(i + 1) % n]], pts[tour[(i + 2) % n]])
        s += u[0] * v[0] + u[1] * v[1]
    return s / n


def nearest_neighbor(pts: Sequence[Point], start: int = 0) -> list[int]:
    n = len(pts)
    used = [False] * n
    tour = [start]
    used[start] = True
    while len(tour) < n:
        cur = pts[tour[-1]]
        best, best_d = -1, float("inf")
        for i, p in enumerate(pts):
            if used[i]:
                continue
            d = dist(cur, p)
            if d < best_d:
                best, best_d = i, d
        used[best] = True
        tour.append(best)
    return tour


def coherence_backbone(pts: Sequence[Point], start: int = 0, lam: float = 0.42) -> list[int]:
    n = len(pts)
    used = [False] * n
    tour = [start]
    used[start] = True
    mean = sum(dist(pts[i], pts[j]) for i in range(n) for j in range(i + 1, n))
    mean /= max(1, n * (n - 1) / 2)
    first = nearest_neighbor(pts, start)[1]
    used[first] = True
    tour.append(first)
    while len(tour) < n:
        prev, cur = pts[tour[-2]], pts[tour[-1]]
        heading = unit(prev, cur)
        best, best_s = -1, -float("inf")
        for i, cand in enumerate(pts):
            if used[i]:
                continue
            direction = unit(cur, cand)
            coh = heading[0] * direction[0] + heading[1] * direction[1]
            score = coh - lam * (dist(cur, cand) / mean)
            if score > best_s:
                best, best_s = i, score
        used[best] = True
        tour.append(best)
    return tour


if __name__ == "__main__":
    rng = random.Random(4)
    pts = [(rng.random(), rng.random()) for _ in range(32)]
    nn = nearest_neighbor(pts)
    gem = coherence_backbone(pts)
    print("toy NN ", f"{tour_length(pts, nn):.2f}", f"{tour_coherence(pts, nn):.3f}")
    print("toy GEM", f"{tour_length(pts, gem):.2f}", f"{tour_coherence(pts, gem):.3f}")
    print("posted 100-pt NN  1984.6 / 0.2267")
    print("posted 100-pt GEM 2492.7 / 0.5251  (restricted; not this toy)")
