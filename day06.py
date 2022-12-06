import os
import json
import re


def parsestack(line):
    n = 4
    return [line[i : i + n] for i in range(0, len(line), n)]


with open(os.environ.get("AOC_INPUT", "input06.txt"), "r") as f:
    INPUT = f.read()


def helper(n):
    last4 = []
    i = 0
    for c in INPUT:
        if len(last4) < n:
            last4.append(c)
            i += 1
        else:
            if len(last4) == n:
                set4 = set(last4)
                # print(f"last4 = {last4}, set4 = {set4}")
                if len(set4) == n:
                    return i
                else:
                    last4.pop(0)
                    last4.append(c)
                    i += 1
    return i


def helper2(n):
    i = n
    while True:
        if len(set(INPUT[i - n: i])) == n:
            return i
        else:
            i += 1


def part1():
    return helper2(4)

def part2():
    return helper2(14)

def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
