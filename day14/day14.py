import os
import sys
import json
import copy

# list(map(int, re.findall(r"\d+", l[1])))

def pr(gr):
    for r in gr:
        line = ""
        for c in r:
            line += str(c)
        print(line[490:510])


HEIGHT = 200
WIDTH = 1000
grid = []
for i in range(HEIGHT):
    line = []
    for w in range(WIDTH):
        line.append(0)
    grid.append(line)

# pr(grid)
path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().strip().split("\n")

    floor = 0
    for l in lines:
        start = None
        points = l.split(" -> ")
        # print(points)
        for s in points:
            pt = s.split(',')
            p = list(map(int, pt))
            if start:
                end = p
                # print(start, end)
                floor = max(floor, start[1], end[1])
                if start[1] == end[1]:
                    if end[0] - start[0] > 0:
                        i = start[0]
                        j = end[0]
                    if end[0] - start[0] < 0:
                        i = end[0]
                        j = start[0]
                    for x in range(i, j + 1):
                        # print(x, start[1])
                        grid[start[1]][x] = 1
                else:
                    if end[1] - start[1] > 0:
                        i = start[1]
                        j = end[1]
                    if end[1] - start[1] < 0:
                        i = end[1]
                        j = start[1]
                    for y in range(i, j + 1):
                        # print(start[0], y)
                        grid[y][start[0]] = 1

            start = p
    floor += 2
    grid2 = copy.deepcopy(grid)

    for x in range(len(grid2[floor])):
        grid2[floor][x] = 1

# pr(grid2)

def fall(w, d, gr):
    global HEIGHT
    global DONE
    global count
    # print(w, d, HEIGHT)
    if gr[d][w] == 1:
        return False
    if d == HEIGHT - 1:
        DONE = True
        return False
    # print(grid[d + 1][w - 1], grid[d + 1][w], grid[d + 1][w + 1])
    if gr[d + 1][w] == 0:
        # print("down")
        return fall(w, d + 1, gr)
    elif gr[d + 1][w - 1] == 0:
        # print("left")
        return fall(w - 1, d + 1, gr)
    elif gr[d + 1][w + 1] == 0:
        # print("right")
        return fall(w + 1, d + 1, gr)
    else:
        count += 1
        # print(f"STOP - {count}")
        gr[d][w] = 1
        return True


def part1():
    global DONE
    global count
    DONE = False
    count = 0
    # fall(500,0)
    # return
    while not DONE:
        fall(500, 0, grid)
    return(count)


def part2():
    global DONE
    global count
    DONE = False
    count = 0

    while fall(500, 0, grid2):
        pass

    return(count)


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
