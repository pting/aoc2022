import os
import sys
import json
import re
from collections import deque

sys.setrecursionlimit(1000000)

# list(map(int, re.findall(r"\d+", l[1])))
pattern = re.compile(r"-?\d+")


def pr(arr):
    for a in arr:
        print(a)


def prd(d):
    for k, v in d.items():
        print(f"{k}: {v}")


M = set()
bound = [0, 0, 0]
path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")
    for l in lines:
        if l:
            cube = tuple(map(int, l.split(",")))
            bound[0] = max(bound[0], cube[0])
            bound[1] = max(bound[1], cube[1])
            bound[2] = max(bound[2], cube[2])
            M.add(cube)


alldirs = [
    [-1, 0, 0],
    [1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, -1],
    [0, 0, 1],
]


def getallnextair(k):
    ret = []
    for dir in alldirs:
        loc = tuple((k[0] + dir[0], k[1] + dir[1], k[2] + dir[2]))
        if loc not in M:
            ret.append(loc)
    return ret


def getallnextlava(k):
    ret = []
    for dir in alldirs:
        loc = tuple((k[0] + dir[0], k[1] + dir[1], k[2] + dir[2]))
        if loc in M:
            ret.append(loc)
    return ret


outside = set()


def bfs(s):
    # print(s)
    q = deque([s])
    while q:
        p = q.popleft()
        if p in outside or p in M:
            continue
        outside.add(p)
        for n in getallnextair(p):
            if (
                n[0] <= bound[0] + 1
                and n[1] <= bound[1] + 1
                and n[2] <= bound[2] + 1
                and n[0] >= -1
                and n[1] >= -1
                and n[2] >= -1
                and n not in outside
            ):
                q.append(n)


# outside = set()
bfs(tuple(bound))
# print("Done with outside.")
# print(len(outside))


def part1():
    total = 0
    for x in M:
        total += 6 - len(getallnextlava(x))

    return total


def part2():
    total = 0
    for x in M:
        total += 6 - len(getallnextlava(x))

    for k in M:
        for a in getallnextair(k):
            if a not in outside and a not in M:
                total -= 1
    return total


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
