import os
import sys
import json
import re
from multiprocessing import Process, Event, Queue
import time

# list(map(int, re.findall(r"\d+", l[1])))

pattern = re.compile(r"-?\d+")

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")
    # print(len(lines))
    if len(lines) < 15:
        YY = 10
    else:
        YY = 2000000


def part1():
    ranges = []
    known = set()
    Y = YY
    for l in lines:
        if l:
            x1, y1, x2, y2 = map(int, pattern.findall(l))
            # print(f"x1 - x2 = {x1 - x2}")
            r = abs(x1 - x2) + abs(y1 - y2)
            # print(f"{x1, y1, x2, y2} r={r}")
            yhi = y1 + r
            ylo = y1 - r
            if ylo <= Y and Y <= yhi:
                off = r - abs(Y - y1)
                # print(f"{x1, y1, x2, y2}: off = {off}, Adding {x1 - off} to {x1 + off}")
                ranges.append((x1 - off, x1 + off))
            if y2 == Y:
                known.add(x2)

    ranges.sort()
    q = []
    for lo, hi in ranges:
        if not q:
            q.append([lo, hi])
            continue

        if lo > q[-1][1] + 1:
            q.append([lo, hi])
            continue

        q[-1][1] = max(q[-1][1], hi)

    blocked = set()
    for lo, hi in q:
        for x in range(lo, hi + 1):
            blocked.add(x)

    return len(blocked - known)


def task(event, queue, rng):
    # print(f"Starting range: {rng}")
    for Y in range(rng[0], rng[1]):
        # print(f"Y = {Y}")
        ranges = []
        known = set()
        for l in lines:
            if l:
                x1, y1, x2, y2 = map(int, pattern.findall(l))
                # print(f"x1 - x2 = {x1 - x2}")
                r = abs(x1 - x2) + abs(y1 - y2)
                # print(f"{x1, y1, x2, y2} r={r}")
                yhi = y1 + r
                ylo = y1 - r
                if ylo <= Y and Y <= yhi:
                    off = r - abs(Y - y1)
                    # print(f"{x1, y1, x2, y2}: off = {off}, Adding {x1 - off} to {x1 + off}")
                    ranges.append((x1 - off, x1 + off))
                if y2 == Y:
                    known.add(x2)

        ranges.sort()
        q = []
        for lo, hi in ranges:
            if not q:
                q.append([lo, hi])
                continue

            if lo > q[-1][1] + 1:
                q.append([lo, hi])
                continue

            q[-1][1] = max(q[-1][1], hi)

        x = 0
        for lo, hi in q:
            if x < lo:
                queue.get()
                queue.put(x * 4000000 + Y)
                event.set()
            x = max(x, hi + 1)
            if x > YY * 2 + 1:
                break


def part2():
    M = YY * 2 + 1
    targets = []

    i = 0
    for j in range(0, M + 1, 500000):
        if j != i:
            targets.append([i, j])
            i = j

    event = Event()
    queue = Queue()
    ret = 0
    queue.put(ret)

    if M < 500:
        task(event, queue, [0, 20])
        return queue.get()

    processes = [
        Process(
            target=task,
            args=(
                event,
                queue,
                t,
            ),
        )
        for t in targets
    ]

    jobs = []
    for process in processes:
        process.start()
        jobs.append(process)

    while True:
        if event.is_set():
            # print("Getting result...")
            ret = queue.get()
            # print("Exiting all child processess..")
            for i in jobs:
                i.terminate()

            return ret
        # time.sleep(2)


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
