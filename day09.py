import os
import json

m = set([(0, 0)])


def helper(T):
    for line in INPUT:
        if not line:
            continue

        move = line.split(" ")
        movefunc = make_move(move[0])
        n = int(move[1])
        while n:
            movefunc(T[0])
            n -= 1
            movenext(T)

    return len(m)


def movenext(tlist):
    if len(tlist) == 1:
        m.add(tuple(tlist[0]))
        return

    h = tlist[0]
    t = tlist[1]
    moved = False
    if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
        if h[0] - t[0] > 0:
            t[0] += 1
            moved = True
        elif h[0] - t[0] < 0:
            t[0] -= 1
            moved = True
        if h[1] - t[1] > 0:
            t[1] += 1
            moved = True
        elif h[1] - t[1] < 0:
            t[1] -= 1
            moved = True
    if moved:
        movenext(tlist[1:])


def moveL(node):
    node[0] -= 1


def moveR(node):
    node[0] += 1


def moveU(node):
    node[1] += 1


def moveD(node):
    node[1] -= 1


movement = {
    "L": moveL,
    "R": moveR,
    "U": moveU,
    "D": moveD,
}


def make_move(dir):
    return movement[dir]


with open(os.environ.get("AOC_INPUT", "input09.txt"), "r") as f:
    INPUT = f.read().split("\n")


def part1():
    T = [[0, 0], [0, 0]]
    return helper(T)


def part2():
    T = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    global m
    m = set([(0, 0)])
    return helper(T)


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
