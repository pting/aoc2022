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
        print(p)
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


def part1b():
    o = [0]
    x = 1
    for line in INPUT:
        if line:
            if line[0] == "n":
                o.append(x)
            else:
                o.append(x)
                o.append(x)
                x += int(line.split()[1])
    o.append(x)

    return sum([x * y for x, y in list(enumerate(o))[20::40]])


def part2b():
    o = []
    x = 1
    res = []
    for line in INPUT:
        if line:
            if line[0] == "n":
                o.append(x)
            else:
                o.append(x)
                o.append(x)
                x += int(line.split()[1])

    def mod40(t):
        return (t[0] % 40, t[1])

    for t in map(mod40, list(enumerate(o))):
        if t[0] == 0:
            res.append("\n")
        if t[0] == t[1] or t[0] == t[1] - 1 or t[0] == t[1] + 1:
            res.append("#")
        else:
            res.append(".")
    ret = "".join(res)
    # print(ret)
    return ret


def main():
    ret = {}
    ret["part_one"] = part1b()
    ret["part_two"] = part2b()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
