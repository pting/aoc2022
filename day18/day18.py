import os
import sys
import json
import re
import sys
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
path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")
    for l in lines:
        if l:
            cube = tuple(map(int, l.split(",")))
            M.add(cube)

# pr(M)

def isnext(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2]) == 1


GR = {}

for t in M:
    GR[t] = []
    for c in M:
        if t != c:
            if isnext(t, c):
                GR[t].append(c)

# pr(M)
# prd(GR)

visited = set()
connected = []

def traverse(k, conn):
    if k in visited:
        return None
    visited.add(k)
    conn.add(k)
    for t in GR[k]:
        traverse(t, conn)
    


for k in GR:
    conn = set()
    traverse(k, conn)
    if conn:
        connected.append(conn)

# pr(connected)

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
            if n[0] < 101 and n[1] < 101 and n[2] < 101 and n[0] >= 0 and n[1] >= 0 and n[2] >= 0 and n not in outside:
                q.append(n)

bfs(tuple((0,0,0)))
# print("Done with outside.")
# print(len(outside))

# outside = set()
# bfs(tuple((0, 100, 100)))
# print("Done with outside.")
# print(len(outside))

# outside = set()
# bfs(tuple((0, 0, 100)))
# print("Done with outside.")
# print(len(outside))

# outside = set()
# bfs(tuple((0, 100, 0)))
# print("Done with outside.")
# print(len(outside))

# outside = set()
# bfs(tuple((100, 100, 100)))
# print("Done with outside.")
# print(len(outside))

def part1():
    total = 0
    for group in connected:
        gtot = 6 * len(group)
        for t in group:
            gtot -= len(GR[t])
        total += gtot

    return(total)


def part2():
    total = 0
    for group in connected:
        gtot = 6 * len(group)
        for t in group:
            gtot -= len(GR[t])
        total += gtot

    for k in M:
        for a in getallnextair(k):
            if a not in outside and a not in M:
                total -= 1
    return(total)


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
