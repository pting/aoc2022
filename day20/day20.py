import os
import sys
import json


class Node:
    def __init__(self, n):
        self.n = n
        self.prev = None
        self.next = None


path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")


def part1():
    f = open(os.environ.get("AOC_INPUT", inputname), "r")
    x = [Node(int(x)) for x in f]

    for i in range(len(x)):
        x[i].next = x[(i + 1) % len(x)]
        x[i].prev = x[(i - 1) % len(x)]
    m = len(x) - 1

    for k in x:
        if k.n == 0:
            z = k
            continue
        p = k
        if k.n > 0:
            for _ in range(k.n % m):
                p = p.next
            if k == p:
                continue
            k.next.prev = k.prev
            k.prev.next = k.next
            p.next.prev = k
            k.next = p.next
            p.next = k
            k.prev = p
        else:
            for _ in range(-k.n % m):
                p = p.prev
            if k == p:
                continue
            k.prev.next = k.next
            k.next.prev = k.prev
            p.prev.next = k
            k.prev = p.prev
            p.prev = k
            k.next = p

    t = 0

    for _ in range(3):
        for _ in range(1000):
            z = z.next
        t += z.n

    return(t)

def part2():
    f = open(os.environ.get("AOC_INPUT", inputname), "r")
    x = [Node(int(x) * 811589153) for x in f]

    for i in range(len(x)):
        x[i].next = x[(i + 1) % len(x)]
        x[i].prev = x[(i - 1) % len(x)]
    m = len(x) - 1

    for _ in range(10):
        for k in x:
            if k.n == 0:
                z = k
                continue
            p = k
            if k.n > 0:
                for _ in range(k.n % m):
                    p = p.next
                if k == p:
                    continue
                k.next.prev = k.prev
                k.prev.next = k.next
                p.next.prev = k
                k.next = p.next
                p.next = k
                k.prev = p
            else:
                for _ in range(-k.n % m):
                    p = p.prev
                if k == p:
                    continue
                k.prev.next = k.next
                k.next.prev = k.prev
                p.prev.next = k
                k.prev = p.prev
                p.prev = k
                k.next = p

    t = 0

    for _ in range(3):
        for _ in range(1000):
            z = z.next
        t += z.n

    return(t)


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
