"""Supply the pinned WetLabEngine demos directory on the command line."""
from pathlib import Path
from runpy import run_path
import sys

atom = run_path(str(Path(sys.argv[1]) / "v16.26-consistency-increment-law/engine.py"))["atomic"]
p = (-1, 0, 0, 0, 0)
start = ((0, 1, 2, 3), (0, 1), (0, 1), (0, 2), (0, 2, 4), (0, 3, 4))
C = 4

def move(rows, cmd):
    op, i, leaf = cmd
    if op == "+":
        # Bare fixed-carrier addition on this star. The parent Pin is always present.
        if leaf in rows[i]:
            return None
        return tuple(tuple(sorted((*row, leaf))) if j == i else row for j, row in enumerate(rows))
    try:
        result = atom(p, rows, i, leaf)
    except ValueError as error:
        if str(error) not in ("same union", "leaf"):
            raise
        return None
    return tuple(map(tuple, result["after"]))

def menu(rows):
    return tuple(v for v in rows[C] if v and move(rows, ("-", C, v)) is not None)

def extension(pair, cmd):
    left, right = (move(rows, cmd) for rows in pair)
    return (left, right) if left is not None and right is not None else None

def differs(pair):
    return menu(pair[0]) != menu(pair[1])

simple = tuple(move(start, ("-", 0, leaf)) for leaf in (1, 2))
eligible = []
for i in (1, 2, 3, 5):
    for leaf in simple[0][i][1:]:
        cmd = ("-", i, leaf)
        following = extension(simple, cmd)
        if following and differs(following):
            eligible.append(cmd)
assert eligible == [("-", 3, 2)]
print("One common peer withdrawal distinguishes the A cuts:", eligible)

common = simple[1]
pair = (move(common, ("-", 2, 1)), move(common, ("-", 0, 3)))
commands = [(op, i, v) for i in range(6) for v in range(1, 5) for op in ("-", "+")]
assert not differs(pair)
witnesses = []
for cmd in commands:
    first = extension(pair, cmd)
    if first is None:
        continue
    assert not differs(first)
    for next_cmd in commands:
        second = extension(first, next_cmd)
        if second is not None and differs(second):
            witnesses.append((cmd, next_cmd, menu(second[0]), menu(second[1])))
print("Shortest shared commands giving different C deletion menus:", witnesses)
assert any(a == ("+", C, 3) and b == ("-", 5, 3) for a,b,_,_ in witnesses)
