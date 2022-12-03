import os
import json

with open(os.environ.get("AOC_INPUT", "input03.txt"), "r") as f:
    INPUT = f.read().split("\n")


def part1():
    res = 0
    for line in INPUT:
        if line:
            size = len(line) // 2
            A = set(line[:size])
            B = set(line[size:])
            I = list(A.intersection(B))

            if I[0].islower():
                res += ord(I[0]) - ord("a") + 1
            else:
                res += ord(I[0]) - ord("A") + 27
    return res


def helper(input):
    I = {}
    for line in input:
        if I:
            I = I.intersection(set(line))
        else:
            I = set(line)

    # Guard against empty lines
    if not I:
        return 0

    L = list(I)
    if L[0].islower():
        return ord(L[0]) - ord("a") + 1
    else:
        return ord(L[0]) - ord("A") + 27


def part2():
    res = 0
    for i in range(0, len(INPUT), 3):
        res += helper(INPUT[i : i + 3])
    return res


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
