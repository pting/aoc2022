import os
import json
import sys


def pr(matrix):
    for r in matrix:
        print(r)


path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input08.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    INPUT = f.read().split("\n")
    m = []

    for h, line in enumerate(INPUT):
        if not line:
            continue
        row = []
        for i, n in enumerate(line):
            row.append(int(n))
        m.append(row)


def isvis(r, c):
    if r == 0 or c == 0 or r == len(m) - 1 or c == len(m[0]) - 1:
        return True

    up = -1
    for i in range(r):
        up = max(up, m[i][c])
    if m[r][c] > up:
        return True

    down = -1
    for i in range(r + 1, len(m)):
        down = max(down, m[i][c])
    if m[r][c] > down:
        return True

    left = -1
    for i in range(c):
        left = max(left, m[r][i])
    if m[r][c] > left:
        return True

    right = -1
    for i in range(c + 1, len(m[0])):
        right = max(right, m[r][i])
    if m[r][c] > right:
        return True

    return False


def dist(r, c):
    up = 0
    for i in reversed(range(r)):
        up += 1
        if m[i][c] >= m[r][c]:
            break

    down = 0
    for i in range(r + 1, len(m)):
        down += 1
        if m[i][c] >= m[r][c]:
            break

    left = 0
    for i in reversed(range(c)):
        left += 1
        if m[r][i] >= m[r][c]:
            break

    right = 0
    for i in range(c + 1, len(m[0])):
        right += 1
        if m[r][i] >= m[r][c]:
            break

    return up * down * left * right


def part1():
    tot = 0
    for r, row in enumerate(m):
        for c in range(len(row)):
            if isvis(r, c):
                tot += 1
    return tot


def part2():
    ret = 0
    # pr(m)
    for r, row in enumerate(m):
        for c in range(len(row)):
            vis = dist(r, c)
            ret = max(vis, ret)

    # pr(temp)
    return ret


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
