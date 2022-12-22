import os
import sys
import json
import re
import copy


def pr(arr):
    for a in arr:
        print("".join(a))


M = []
path = []
maxc = 0

# list(map(int, re.findall(r"\d+", l[1])))
pattern = re.compile(r"-?\d+")

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")
    for l in lines:
        if l:
            if "." in l or " " in l or "#" in l:
                row = []
                for c in l:
                    row.append(c)
                maxc = max(maxc, len(row))
                M.append(row)
            else:
                path = re.split("(\d+)", l.strip())[1:-1]


def padlist(some_list, target_len):
    return some_list[:target_len] + [" "] * (target_len - len(some_list))


for i in range(len(M)):
    M[i] = padlist(M[i], maxc)

# pr(map)
# print(path)

DIR = {
    "N": (-1, 0, 3, "^"),
    "S": (1, 0, 1, "v"),
    "E": (0, 1, 0, ">"),
    "W": (0, -1, 2, "<"),
}

TURN = {
    "L": {
        "N": "W",
        "S": "E",
        "E": "N",
        "W": "S",
    },
    "R": {
        "N": "E",
        "S": "W",
        "E": "S",
        "W": "N",
    },
}


def move(loc):
    # print("go", loc)
    dir = loc[2]
    newr = loc[0] + DIR[dir][0]
    newc = loc[1] + DIR[dir][1]
    m = loc[3]

    if dir == "S" and (newr >= len(m) or m[newr][newc] == " "):
        for i in range(len(m)):
            if m[i][loc[1]] != " ":
                newr = i
                break
    if dir == "N" and (newr < 0 or m[newr][newc] == " "):
        for i in reversed(range(len(m))):
            if m[i][loc[1]] != " ":
                newr = i
                break
    if dir == "E" and (newc >= len(m[loc[0]]) or m[newr][newc] == " "):
        for i in range(len(m[loc[0]])):
            if m[loc[0]][i] != " ":
                newc = i
                break
    if dir == "W" and (newc < 0 or m[newr][newc] == " "):
        for i in reversed(range(len(m[loc[0]]))):
            if m[loc[0]][i] != " ":
                newc = i
                break

    if loc[3][newr][newc] == "#":
        return loc

    # print([newr, newc, loc[2]])
    loc[3][newr][newc] = DIR[dir][3]
    return [newr, newc, loc[2], loc[3]]


def turn(loc, d):
    # print("turn", loc, d)
    newd = TURN[d][loc[2]]
    loc[2] = newd
    return loc


def part1():
    m = copy.deepcopy(M)
    loc = [0, m[0].index("."), "E", m]
    # print(loc)
    p = copy.deepcopy(path)
    while p:
        x = p.pop(0)
        if x.isnumeric():
            n = int(x)
            for _ in range(n):
                newloc = move(loc)
                if not newloc:
                    break
                loc = newloc
        else:
            loc = turn(loc, x)
        # print(loc)

    # pr(loc[3])
    # print(loc[0], loc[1], loc[2])
    ret = [(loc[0] + 1) * 1000, (loc[1] + 1) * 4, DIR[loc[2]][2]]
    return sum(ret)


DIR = {
    "N": (-1, 0, 3, "^"),
    "S": (1, 0, 1, "v"),
    "E": (0, 1, 0, ">"),
    "W": (0, -1, 2, "<"),
}


BOX1 = {
    "E": lambda r, c: [r, 100, "E"],  # BOX2
    "S": lambda r, c: [50, c, "S"],  # BOX3
    "N": lambda r, c: [100 + c, 0, "E"],  # BOX6
    "W": lambda r, c: [149 - r, 0, "E"],  # BOX5
}
TUP1 = list(BOX1.items())

BOX2 = {
    "E": lambda r, c: [149 - r, 99, "W"],  # BOX4
    "S": lambda r, c: [c - 50, 99, "W"],  # BOX3
    "N": lambda r, c: [199, c - 100, "N"],  # BOX6
    "W": lambda r, c: [r, 99, "W"],  # BOX5
}
TUP2 = list(BOX2.items())

BOX3 = {
    "E": lambda r, c: [49, r + 50, "N"],  # BOX4
    "S": lambda r, c: [r + 1, c, "S"],  # BOX3
    "N": lambda r, c: [r - 1, c, "N"],  # BOX6
    "W": lambda r, c: [100, r - 50, "S"],  # BOX5
}
TUP3 = list(BOX3.items())

BOX4 = {
    "E": lambda r, c: [149 - r, 149, "W"],  # BOX2
    "S": lambda r, c: [c + 100, 49, "W"],  # BOX6
    "N": lambda r, c: [r - 1, c, "N"],  # BOX3
    "W": lambda r, c: [r, c - 1, "W"],  # BOX5
}
TUP4 = list(BOX4.items())

BOX5 = {
    "E": lambda r, c: [r, c + 1, "E"],  # BOX4
    "S": lambda r, c: [r + 1, c, "S"],  # BOX6
    "N": lambda r, c: [50 + c, 50, "E"],  # BOX3
    "W": lambda r, c: [149 - r, 50, "E"],  # BOX5
}
TUP5 = list(BOX5.items())

BOX6 = {
    "E": lambda r, c: [149, r - 100, "N"],  # BOX4
    "S": lambda r, c: [0, c + 100, "S"],  # BOX2
    "N": lambda r, c: [r - 1, c, "N"],  # BOX5
    "W": lambda r, c: [0, r - 100, "S"],  # BOX1
}
TUP6 = list(BOX6.items())

RBOUND = [
    [0, 50, {tuple(TUP1), tuple(TUP2)}],
    [50, 100, {tuple(TUP3)}],
    [100, 150, {tuple(TUP5), tuple(TUP4)}],
    [150, 200, {tuple(TUP6)}],
]
CBOUND = [
    [0, 50, {tuple(TUP5), tuple(TUP6)}],
    [50, 100, {tuple(TUP1), tuple(TUP3), tuple(TUP4)}],
    [100, 150, {tuple(TUP2)}],
]


def getbox(r, c):
    # print("getbox:", r, c)
    box = {}
    for rb in RBOUND:
        if rb[0] <= r and r < rb[1]:
            tup = rb[2]
            # print("1", tup)
            break
    for cb in CBOUND:
        if cb[0] <= c and c < cb[1]:
            tup2 = cb[2]
            # print("2", tup2)
            tup = tup.intersection(cb[2])
            # print("3", tup)
            break

    for t in tup:
        for (k, v) in t:
            box[k] = v
    # print("got box:", box)
    return box


def move2(loc):
    global M
    m = M
    # print("go", loc)

    dir = loc[2]
    if (
        (dir == "N" and loc[0] in [0, 50, 100, 150])
        or (dir == "S" and loc[0] in [49, 99, 149, 199])
        or (dir == "E" and loc[1] in [49, 99, 149, 199])
        or (dir == "W" and loc[1] in [0, 50, 100, 150])
    ):
        # print("Old location:", loc)
        oldbox = getbox(loc[0], loc[1])
        newr, newc, newdir = oldbox[loc[2]](loc[0], loc[1])
        # print("New location:", newr, newc, newdir)
    else:
        newr = loc[0] + DIR[dir][0]
        newc = loc[1] + DIR[dir][1]
        newdir = dir

    if m[newr][newc] == "#":
        return None
    return [newr, newc, newdir]


def part2():
    global M
    loc = [0, M[0].index("."), "E"]
    # print(loc)
    p = copy.deepcopy(path)
    while p:
        x = p.pop(0)
        if x.isnumeric():
            n = int(x)
            for _ in range(n):
                newloc = move2(loc)
                if not newloc:
                    break
                loc = newloc
        else:
            loc = turn(loc, x)
        # print(loc)

    # pr(loc[3])
    # print(loc[0], loc[1], loc[2])
    ret = [(loc[0] + 1) * 1000, (loc[1] + 1) * 4, DIR[loc[2]][2]]
    return sum(ret)


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
