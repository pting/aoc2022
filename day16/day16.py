import os
import sys
import json
import re
from collections import deque

# list(map(int, re.findall(r"\d+", l[1])))
pattern = re.compile(r"-?\d+")

rates = {}
tunnels = {}
dist = {}

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")
    for l in lines:
        if l:
            s = l.split(";")
            k = s[0].split()[1]
            r = int(s[0].split("=")[1])
            if r:
                rates[k] = r
            p = s[1].replace("valves", "valve")
            p = p.split("valve ")[1]
            p = p.split(", ")
            tunnels[k] = p


# Calculate distances from start to all other nodes
def bfs(tunnels, start, targets):
    d = {start: 0}
    seen = {start}
    q = deque([start])
    while q and any(t not in d for t in targets):
        p = q.popleft()
        for x in tunnels[p]:
            if x not in seen:
                seen.add(x)
                d[x] = d[p] + 1
                q.append(x)
    return d


def find_paths(dist, rates, t):
    res = []
    paths = []
    stack = [(t, 0, ["AA"])]
    while stack:
        t, r, path = stack.pop()
        curr = path[-1]
        new = []
        for n, d in dist[curr].items():
            if d > t - 2 or n in path:
                continue
            newt = t - d - 1
            newr = r + rates[n] * newt
            item = newt, newr, path + [n]
            new.append(item)
        if new:
            stack.extend(new)
        else:
            res.append(r)
            paths.append(path[1:0])
    return res, paths


def part1():
    for start in ("AA", *rates):
        dist[start] = {}
        d = bfs(tunnels, start, rates)
        # print(f"d = {d}")
        for r in rates:
            if r != start and r in d:
                dist[start][r] = d[r]
    # print(dist)
    p, _ = find_paths(dist, rates, 30)
    return max(p)


def part2():
    x = list(zip(*find_paths(dist, rates, 26)))
    p, paths = zip(*sorted(x, reverse=True))
    i, j = 0, 1
    while any(x in paths[j] for x in paths[i]):
        j += 1
    ans = p[i] + p[j]  # lower bound
    j_max = j  # since p[i] can only decrease, j cannot exceed this
    for i in range(1, j_max):
        for j in range(i + 1, j_max + 1):
            if any(x in paths[j] for x in paths[i]):
                continue
            ans = max(ans, p[i] + p[j])
    return ans


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
