import os
import json


with open(os.environ.get("AOC_INPUT", "input10.txt"), "r") as f:
    INPUT = f.read().split("\n")


def do1(c, X, points, sum):
    c += 1
    if c in points:
        sum += c * X
        # print(X)
    return c, sum


def part1():
    points = set([20, 60, 100, 140, 180, 220])
    X = 1
    c = 0
    sum = 0
    for line in INPUT:
        if line:
            if line[0] == "n":
                c, sum = do1(c, X, points, sum)
            else:
                l = line.split(" ")
                c, sum = do1(c, X, points, sum)
                c, sum = do1(c, X, points, sum)
                X += int(l[1])

    return sum


def do2(c, X, res, p2):
    if c in [X - 1, X, X + 1]:
        res.append("#")
    else:
        res.append(".")

    c += 1
    if c % 40 == 0:
        p = "".join(res)
        p2 = p2 + "\n" + p
        # print(p)
        res = []
        c = 0

    return c, X, res, p2


def part2():
    X = 1
    c = 0
    res = []
    p2 = ""

    for line in INPUT:
        if line:
            if line[0] == "n":
                c, X, res, p2 = do2(c, X, res, p2)
            else:
                l = line.split(" ")
                c, X, res, p2 = do2(c, X, res, p2)
                c, X, res, p2 = do2(c, X, res, p2)

                X += int(l[1])
    return p2


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
