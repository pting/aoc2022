import os
import json
from multiprocessing import Process, Queue

with open(os.environ.get("AOC_INPUT", "input03.txt"), "r") as f:
    INPUT = f.read().split("\n")


def part1(queue, input):
    res1 = 0
    for line in input:
        if line:
            size = len(line) // 2
            A = set(line[:size])
            B = set(line[size:])
            I = next(iter(A.intersection(B)))

            if I.islower():
                res1 += ord(I) - ord("a") + 1
            else:
                res1 += ord(I) - ord("A") + 27
    queue.put(("part_one", res1))


def helper(l):
    I = {}
    for line in l:
        if line:
            if I:
                I = I.intersection(set(line))
            else:
                I = set(line)
    L = next(iter(I))
    if L.islower():
        return ord(L) - ord("a") + 1
    else:
        return ord(L) - ord("A") + 27


def part2(queue, input):
    res2 = 0
    for i in range(0, len(input), 3):
        res2 += helper(input[i : i + 3])
    queue.put(("part_two", res2))


def main():
    queue = Queue()

    ret = {}
    p1 = Process(
        target=part1,
        args=(
            queue,
            INPUT,
        ),
    )
    p1.start()
    p2 = Process(
        target=part2,
        args=(
            queue,
            INPUT,
        ),
    )
    p2.start()
    p1.join()
    p2.join()

    count = 0
    while queue:
        res = queue.get()
        ret[res[0]] = res[1]
        count += 1
        if count == 2:
            break

    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
