import os
import sys
import json

map = []
maxcount = float("inf")
S = ord("S")
E = ord("E")
target = None
curr = None

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")

    for line in lines:
        if line:
            map.append([int(ord(l)) for l in line])

    for r, row in enumerate(map):
        for c, col in enumerate(row):
            if col == E:
                target = [r, c]
                map[r][c] = ord("z")
            if col == S:
                curr = [r, c]
                map[r][c] = ord("a")
            if curr and target:
                break

    size = [len(map), len(map[0])]


def part1():
    """BFS from start and end, meet in the middle. This saves roughly 1/3 runtime."""
    queue = [(curr[0], curr[1], 0)]
    q2 = [(target[0], target[1], 0)]
    visited = {}  # (r, c) = num steps to target

    while queue or q2:
        if q2:
            (r, c, d2) = q2.pop(0)
            if [r, c] == curr:
                return d2
            if (r, c) not in visited:
                visited[(r, c)] = d2
                # right
                if c + 1 < size[1]:
                    if map[r][c + 1] >= map[r][c] - 1:
                        q2.append((r, c + 1, d2 + 1))
                # left
                if c - 1 >= 0:
                    if map[r][c - 1] >= map[r][c] - 1:
                        q2.append((r, c - 1, d2 + 1))
                # up
                if r - 1 >= 0:
                    if map[r - 1][c] >= map[r][c] - 1:
                        q2.append((r - 1, c, d2 + 1))
                # down
                if r + 1 < size[0]:
                    if map[r + 1][c] >= map[r][c] - 1:
                        q2.append((r + 1, c, d2 + 1))

        if queue:
            (r, c, depth) = queue.pop(0)
            if [r, c] == target:
                return depth
            if (r, c) in visited:
                if visited[(r, c)]:
                    return depth + visited[(r, c)]
            else:
                visited[(r, c)] = None
                # right
                if c + 1 < size[1]:
                    if map[r][c + 1] <= map[r][c] + 1:
                        queue.append((r, c + 1, depth + 1))
                # left
                if c - 1 >= 0:
                    if map[r][c - 1] <= map[r][c] + 1:
                        queue.append((r, c - 1, depth + 1))
                # up
                if r - 1 >= 0:
                    if map[r - 1][c] <= map[r][c] + 1:
                        queue.append((r - 1, c, depth + 1))
                # down
                if r + 1 < size[0]:
                    if map[r + 1][c] <= map[r][c] + 1:
                        queue.append((r + 1, c, depth + 1))


def part1b():
    queue = [(curr[0], curr[1], 0)]
    visited = set()

    while queue:
        (r, c, depth) = queue.pop(0)
        if [r, c] == target:
            return depth
        if (r, c) not in visited:
            visited.add((r, c))
            # right
            if c + 1 < size[1]:
                if map[r][c + 1] <= map[r][c] + 1:
                    queue.append((r, c + 1, depth + 1))
            # left
            if c - 1 >= 0:
                if map[r][c - 1] <= map[r][c] + 1:
                    queue.append((r, c - 1, depth + 1))
            # up
            if r - 1 >= 0:
                if map[r - 1][c] <= map[r][c] + 1:
                    queue.append((r - 1, c, depth + 1))
            # down
            if r + 1 < size[0]:
                if map[r + 1][c] <= map[r][c] + 1:
                    queue.append((r + 1, c, depth + 1))


def part2():
    q2 = [(target[0], target[1], 0)]
    visited2 = {}
    maxqlen = 0

    while q2:
        maxqlen = max(maxqlen, len(q2))
        (r, c, d2) = q2.pop(0)
        if map[r][c] == ord("a"):
            print(f"Part2 remaining queue length: {len(q2)}, max {maxqlen}")
            return d2
        if (r, c) not in visited2:
            visited2[(r, c)] = d2
            # right
            if c + 1 < size[1]:
                if map[r][c + 1] >= map[r][c] - 1:
                    q2.append((r, c + 1, d2 + 1))
            # left
            if c - 1 >= 0:
                if map[r][c - 1] >= map[r][c] - 1:
                    q2.append((r, c - 1, d2 + 1))
            # up
            if r - 1 >= 0:
                if map[r - 1][c] >= map[r][c] - 1:
                    q2.append((r - 1, c, d2 + 1))
            # down
            if r + 1 < size[0]:
                if map[r + 1][c] >= map[r][c] - 1:
                    q2.append((r + 1, c, d2 + 1))


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
