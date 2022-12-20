import os
import sys
import json
import re

wind = None
path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    wind = f.read().strip()


def pr(arr):
    # for a in arr:
    #     print(a)
    pass


rocks = [
    [['#', '#', '#', '#']],
    [['.', '#', '.'], ['#', '#', '#'], ['.', '#', '.']],
    [['#', '#', '#'], ['.', '.', '#'], ['.', '.', '#']],
    [['#'], ['#'], ['#'], ['#']],
    [['#', '#'], ['#', '#']],
]
# pr(rocks)
# def canmove(dir, )

DIR = {
    "D": [-1, 0],
    "<": [0, -1],
    ">": [0, 1]
}

def move(dir, id, chamber):
    # print(f"move: {dir, id}")
    pieces = []
    for r, row in enumerate(chamber):
        for c, rock in enumerate(row):
            if rock == id:
                newr = r + DIR[dir][0]
                newc = c + DIR[dir][1]
                pieces.append([newr, newc])
                # print(f"row = {row}, c = {c}, newr = {newr}, newc = {newc}")
                if newc < 0 or newc > 6 or newr < 0 or (chamber[newr][newc] != 0 and chamber[newr][newc] != id):
                    return(False)
    
    # Can move so move
    for r, row in enumerate(chamber):
        for c, rock in enumerate(row):
            if rock == id:
                chamber[r][c] = 0

    for r, c in pieces:
        chamber[r][c] = id

    if dir == "D":
        chamber.pop()
    pr(chamber)
    return True


def part1():
    global wind
    floor = 0
    chamber = []
    
    rid = 0
    wid = 0
    rocknum = 0
    N = 2022
    for y in range(N):
        rocknum += 1

        chamber.append([0] * 7)
        chamber.append([0] * 7)
        chamber.append([0] * 7)
        for r in rocks[rid]:
            row = [0] * 7
            j = 2
            for i in range(len(r)):
                row[j] = rocknum if r[i] == "#" else 0
                j += 1
            chamber.append(row)

        rid += 1
        if rid == len(rocks):
            rid = 0

        pr(chamber)

        fall = True
        while(fall):
            w = wind[wid]
            wid += 1
            if wid == len(wind):
                wid = 0

            move(w, rocknum, chamber)
            fall = move("D", rocknum, chamber)
    print(f"Height = {len(chamber)}")
    pr(chamber)
    return(len(chamber))


def part2():
    return None


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()


rockstring = """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

rocks = []
for gr in rockstring.strip().split("\n\n"):
    ro = []
    for l in gr.split("\n"):
        x = [c for c in l]
        ro.append(x)
    ro.reverse()
    rocks.append(ro)