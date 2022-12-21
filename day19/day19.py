import os
import sys
import json
import re
from collections import deque
import copy
from multiprocessing import Process, Array
import time

# list(map(int, re.findall(r"\d+", l[1])))
pattern = re.compile(r"-?\d+")

BP = []


def pr(arr):
    for a in arr:
        print(a)


path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")
    for l in lines:
        if l:
            nums = list(map(int, pattern.findall(l)))
            BP.append(nums)


def state(t):
    return {
        "ore": 0,
        "clay": 0,
        "obs": 0,
        "geo": 0,
        "orebot": 1,
        "claybot": 0,
        "obsbot": 0,
        "geobot": 0,
        "timeleft": t,
    }


def dfs(st, bp, cache):
    if st["timeleft"] == 0:  # or (st["timeleft"] < 4 and st["geobot"] < 1):
        # print(st)
        return st["geo"]

    key = tuple(st.items())
    if key in cache:
        # print(cache[key], key)
        return cache[key]

    res = 0
    n = copy.deepcopy(st)
    n["timeleft"] -= 1
    n["ore"] += st["orebot"]
    n["clay"] += st["claybot"]
    n["obs"] += st["obsbot"]
    n["geo"] += st["geobot"]

    # build geobot
    if st["ore"] >= bp[-2] and st["obs"] >= bp[-1]:
        n["ore"] -= bp[-2]
        n["obs"] -= bp[-1]
        n["geobot"] += 1
        newgeo = dfs(n, bp, cache)
        res = max(res, dfs(n, bp, cache))
    # build obsbot
    elif st["ore"] >= bp[-4] and st["clay"] >= bp[-3]:
        n["ore"] -= bp[-4]
        n["clay"] -= bp[-3]
        n["obsbot"] += 1
        res = max(res, dfs(n, bp, cache))
    else:
        # Do nothing
        res = max(res, dfs(n, bp, cache))
        # build orebot if worth it
        if st["ore"] >= bp[1] and st["timeleft"] > bp[1] and st["orebot"] < bp[1] + bp[2] + bp[-2] + bp[-4]:
            n["ore"] -= bp[1]
            n["orebot"] += 1
            res = max(res, dfs(n, bp, cache))
            n["ore"] += bp[1]
            n["orebot"] -= 1
        # build claybot
        if st["ore"] >= bp[2] and st["claybot"] < bp[-3]:
            n["ore"] -= bp[2]
            n["claybot"] += 1
            res = max(res, dfs(n, bp, cache))
            n["ore"] += bp[2]
            n["claybot"] -= 1

    cache[key] = res
    return res


def part1():
    res = []
    cache = []

    for p in BP:
        cache = {}
        res.append([dfs(state(24), p, cache), p[0]])

    ret = 0
    for n in res:
        ret += n[0] * n[1]

    return ret


def part2old():
    res = 1
    cache = []

    for p in BP[:3]:
        cache = {}
        res *= dfs(state(32), p, cache)

    return res


def task(a, p, i):
    cache = {}
    a[i] = dfs(state(32), p, cache)


def part2():
    a = Array("i", 3)

    processes = [
        Process(
            target=task,
            args=(a, p, i),
        )
        for i, p in enumerate(BP[:3])
    ]

    for pr in processes:
        pr.start()

    time.sleep(5)

    for pr in processes:
        pr.join()

    return a[0] * a[1] * a[2]


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
