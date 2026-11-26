from itertools import combinations
from pathlib import Path
from runpy import run_path
import sys

demos = Path(sys.argv[1])
engine = run_path(str(demos / "v16.27-increment-attribution-closure/engine.py"))
parents = (-1, 0, 0, 0, 0)
start = ((0,1,2,3), (0,1), (0,1), (0,2), (0,2,4), (0,3,4))
names = "AXYZCB"
events = [(i, leaf) for i, row in enumerate(start) for leaf in row if leaf]
totals = [0, 0, 0]
for first, second in combinations(events, 2):
    target = tuple(tuple(v for v in row if (i,v) not in (first, second))
                   for i,row in enumerate(start))
    paths = engine["paths"](parents, start, target)
    if not paths:
        totals[0] += 1
        continue
    assert len(paths) == 2
    totals[1] += 1
    left, right = paths
    if engine["event_map"](left) != engine["event_map"](right):
        totals[2] += 1
        traces = [[p[0]["h_before"], *(d["h_after"] for d in p)] for p in paths]
        print([(names[i],v) for i,v in (first, second)], traces)
print("unavailable, both orders legal, attribution changes", totals)
