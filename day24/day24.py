import os
import sys
import json
from collections import deque
import copy


def pr(arr):
    for a in arr:
        print(a)


M = []
path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")
    for l in lines:
        if l:
            row = []
            for c in range(len(l)):
                v = [l[c]] if l[c] != "." else []
                row.append(v)
            M.append(row)

DIR = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}


def pr1(arr, r, c):
    for i, a in enumerate(arr):
        s = []
        for j, b in enumerate(a):
            s.append("*" if i == r and j == c else b[0] if b else ".")
        print("".join(s))


def go(el, end, m, minute):
    q = deque()
    q.append(el)

    while True:
        minute += 1
        nm = []
        for r in range(len(m)):
            row = []
            for c in range(len(m[r])):
                if m[r][c] == ["#"]:
                    row.append(["#"])
                else:
                    row.append([])
            nm.append(row)

        for r in range(len(m)):
            for c in range(len(m[r])):
                for v in m[r][c]:
                    match v:
                        case "#" | " ":
                            pass
                        case "^" | "v" | ">" | "<":
                            nr = r + DIR[v][0]
                            nc = c + DIR[v][1]
                            if nr == 0:
                                nr = len(nm) - 2
                            elif nr == len(nm) - 1:
                                nr = 1
                            if nc == 0:
                                nc = len(nm[r]) - 2
                            elif nc == len(nm[r]) - 1:
                                nc = 1
                            nm[nr][nc].append(v)

        visited = set()
        newq = deque()
        while q:
            e = q.popleft()
            elf = (e[0], e[1], minute)
            if elf in visited:
                continue
            visited.add(elf)

            for d in ["^", "v", ">", "<"]:
                newloc = (r := elf[0] + DIR[d][0], c := elf[1] + DIR[d][1], minute)
                if r == end[0] and c == end[1]:
                    return minute, nm
                if r >= 1 and r <= len(nm) - 2 and c >= 1 and c <= len(nm[r]) - 2:
                    if not nm[r][c]:
                        newq.append(newloc)

            if (
                not nm[elf[0]][elf[1]]
                and elf[0] >= 0
                and elf[0] <= len(nm) - 1
                and elf[1] >= 0
                and elf[1] <= len(nm[r]) - 1
            ):
                oldloc = (elf[0], elf[1], minute)
                newq.append(oldloc)

        q = newq
        m = nm


def part1():
    m = copy.deepcopy(M)
    destination = (len(M) - 1, len(M[0]) - 2)
    count, m = go((0, 1), destination, m, 0)
    return count


def part2():
    minute = 0
    destination = (len(M) - 1, len(M[0]) - 2)
    c1, m = go((0, 1), destination, M, 0)
    c2, m = go(destination, (0,1), m, c1)
    c3, _ = go((0, 1), destination, m, c2)
    
    # [(len(M) - 1, len(M[0]) - 2), (0, 1), (len(M) - 1, len(M[0]) - 2)]
    return c3

def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
