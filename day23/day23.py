import os
import sys
import json
from collections import deque
import copy


def pr(arr):
    for k, v in arr.items():
        print(k, v)
    print("length", len(arr))


EL = set()

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")


with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")
    for r, l in enumerate(lines):
        if l:
            for c in range(len(l)):
                if l[c] == "#":
                    EL.add((r, c))


def isalone(r, c, elves):
    around = [
        (r - 1, c - 1),
        (r - 1, c),
        (r - 1, c + 1),
        (r, c + 1),
        (r, c - 1),
        (r + 1, c - 1),
        (r + 1, c),
        (r + 1, c + 1),
    ]
    for target in around:
        if target in elves:
            return False
    return True


def move(elves, dirs):
    def canmove(locs):
        ret = True
        for l in locs:
            if l in elves:
                return False
        return True

    moves = []
    conflicts = {}

    for elf in elves:
        r = elf[0]
        c = elf[1]
        if isalone(r, c, elves):
            continue

        target = None
        for dir in dirs:
            if dir == "N" and canmove([(r - 1, c - 1), (r - 1, c), (r - 1, c + 1)]):
                target = (r - 1, c)
            elif dir == "S" and canmove([(r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]):
                target = (r + 1, c)
            elif dir == "W" and canmove([(r + 1, c - 1), (r, c - 1), (r - 1, c - 1)]):
                target = (r, c - 1)
            elif dir == "E" and canmove([(r + 1, c + 1), (r, c + 1), (r - 1, c + 1)]):
                target = (r, c + 1)
            if target:
                break

        if target:
            if target not in conflicts:
                conflicts[target] = 0
            conflicts[target] += 1
            moves.append((elf, target))

    if not moves:
        return False

    for (elf, target) in moves:
        if conflicts[target] == 1:
            elves.remove(elf)
            elves.add(target)
    return True


def part1():
    elves = copy.deepcopy(EL)
    dirs = ["N", "S", "W", "E"]
    for _ in range(10):
        move(elves, dirs)
        d = dirs.pop(0)
        dirs.append(d)

    br = [float("inf"), -float("inf")]
    bc = [float("inf"), -float("inf")]

    for elf in elves:
        br[0] = min(br[0], elf[0])
        br[1] = max(br[1], elf[0])
        bc[0] = min(bc[0], elf[1])
        bc[1] = max(bc[1], elf[1])

    count = 0
    for r in range(br[0], br[1] + 1):
        for c in range(bc[0], bc[1] + 1):
            if (r, c) not in elves:
                count += 1

    return count


def part2():
    elves = copy.deepcopy(EL)
    dirs = ["N", "S", "W", "E"]
    i = 0
    while True:
        i += 1
        if not move(elves, dirs):
            return i
        d = dirs.pop(0)
        dirs.append(d)


def prmap(elves, br, bc):
    for r in range(br[0], br[1] + 1):
        line = ""
        for c in range(bc[0], bc[1] + 1):
            if (r, c) in elves:
                line += "#"
            else:
                line += "."
        print(line)
    print("count", len(elves))


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
