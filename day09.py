import os
import json

def pr(matrix):
    for r in matrix:
        print(r)

m = set((0,0))

def isfar(h, t):
    return (abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1)


def movehead(T, dir, n):
    while n:
        # print(f"movehead: {T} -> {dir}, {n}")
        if dir == "L":
            T[0][0] -= 1
        elif dir == "R":
            T[0][0] += 1
        elif dir == "U":
            T[0][1] += 1
        elif dir == "D":
            T[0][1] -= 1
        n -= 1
        # print(f"--> H: {H}")
        
        movetail(T)
        

def movetail(tlist):
    # print(tlist)
    if len(tlist) == 1:
        newloc = tuple(tlist[0])
        m.add(newloc)
        # print(f"End: {m}")
        return

    h = tlist[0]
    t = tlist[1]
    moved = False
    if isfar(h, t):
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
            # print(f"--> {T}, tot: {tot1}")
    if moved:
        movetail(tlist[1:])


with open(os.environ.get("AOC_INPUT", "input09.txt"), "r") as f:
    INPUT = f.read().split("\n")


def part1():
    T = [[0, 0], [0, 0]]
    for line in INPUT:
        if not line:
            continue

        move = line.split(" ")
        movehead(T, move[0], int(move[1]))
    return len(m)


def part2():
    T = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    global m
    m = set((0,0))
    # print(f"Begin: {T}")
    for line in INPUT:
        if not line:
            continue

        move = line.split(" ")
        movehead(T, move[0], int(move[1]))
    # print(f"End: {T}")
    return len(m)

 

def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
