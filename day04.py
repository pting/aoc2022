import os
import json
import sys


def getpair(line):
    pair = line.split(",")
    p1, p2 = pair[0].split("-"), pair[1].split("-")
    return (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1]))


with open(os.environ.get("AOC_INPUT", sys.argv[1]), "r") as f:
    INPUT = f.read().split("\n")
    parsedInput = []
    for line in INPUT:
        if line:
            parsedInput.append(getpair(line))


def part1():
    res = 0
    for p1, p2 in parsedInput:
        if part1check(p1, p2):
            res += 1
    return res


def part1check(p1, p2):
    return (p1[0] <= p2[0] and p1[1] >= p2[1]) or (p2[0] <= p1[0] and p2[1] >= p1[1])


def part2check(p1, p2):
    return (
        (p1[0] >= p2[0] and p1[0] <= p2[1])
        or (p1[1] >= p2[0] and p1[1] <= p2[1])
        or (p2[0] >= p1[0] and p2[0] <= p1[1])
        or (p2[1] >= p1[0] and p2[1] <= p1[1])
    )


def part2():
    res = 0
    for p1, p2 in parsedInput:
        if part1check(p1, p2) or part2check(p1, p2):
            res += 1
    return res


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
