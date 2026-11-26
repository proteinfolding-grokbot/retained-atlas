"""Run with the pinned WetLabEngine demos directory as the only argument."""
from pathlib import Path
from runpy import run_path
import sys

atom = run_path(str(Path(sys.argv[1]) / "v16.26-consistency-increment-law/engine.py"))["atomic"]
parents = (-1, 0, 0, 0, 0)
start = ((0, 1, 2, 3), (0, 1), (0, 1), (0, 2), (0, 2, 4), (0, 3, 4))
C = 4

def neighborhood(rows):
    return tuple((i, tuple(row)) for i, row in enumerate(rows)
                 if i == C or (set(row) & set(rows[C])) - {0})

def outside_coverage(rows):
    return set().union(*(row for i, row in enumerate(rows) if i != C)) - {0}

def local_test(rows):
    peers = [set(row) - {0} for i, row in enumerate(rows) if i != C and 2 in row]
    return set(rows[C]) == {0, 2, 4} and peers == [{2}]

states = [start] + [atom(parents, start, i, v)["after"]
                    for i, row in enumerate(start) for v in row if v]
tested = positives = 0
for rows in states:
    for v in (2, 4):
        try:
            receipt = atom(parents, rows, C, v)
        except ValueError as error:
            if str(error) not in ("same union", "leaf"):
                raise
            continue
        assert local_test(rows) == receipt["trigger"]
        tested += 1
        positives += receipt["trigger"]
assert (tested, positives) == (19, 2)

common = atom(parents, start, 0, 2)["after"]
left = atom(parents, common, 2, 1)["after"]   # Y withdraws 1
right = atom(parents, common, 0, 3)["after"]  # A withdraws 3
assert neighborhood(left) == neighborhood(right)
assert outside_coverage(left) == outside_coverage(right) == {1, 2, 3, 4}
for v in (2, 4):
    a, b = (atom(parents, rows, C, v) for rows in (left, right))
    assert neighborhood(a["after"]) == neighborhood(b["after"])
    assert (a["tau_before"], a["tau_after"], a["trigger"]) == (2, 3, True)
    assert (b["tau_before"], b["tau_after"], b["trigger"]) == (3, 3, False)
    print("C withdraws", v, "same neighborhood; cover sizes 2->3 versus 3->3")
print(tested, "one-withdrawal-or-control certificates checked;", positives, "true")
