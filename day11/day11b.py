import os
import sys
import json
import re
import copy

monkey = []
lcm = 1

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    groups = f.read().strip().split("\n\n")

    for g in groups:
        l = g.splitlines()
        mon = []
        mon.append(list(map(int, re.findall(r"\d+", l[1]))))
        mon.append(eval(f"lambda old:{l[2].split('=')[-1]}"))
        prime = int(re.findall(r"\d+", l[3])[0])
        lcm *= prime
        mon.append(prime)
        mon.append(int(re.findall(r"\d+", l[4])[0]))
        mon.append(int(re.findall(r"\d+", l[5])[0]))
        monkey.append(mon)

    # print(monkey)
    monkey2 = copy.deepcopy(monkey)


def part1():
    rounds = 20
    counts = [0] * len(monkey)

    while rounds > 0:
        # print(f"Round {rounds}")
        rounds -= 1
        for i, m in enumerate(monkey):
            # print()
            # print(m)
            for n in m[0]:
                new = m[1](n)
                # print(f"Worry level {n} to {new}")
                new = new // 3
                # print(f"Worry level is divided by 3 to {new}")
                if new % m[2] == 0:
                    # print(f"Current worry level is divisible by {m[2]}")
                    monkey[m[3]][0].append(new)
                    # print(f"Item with worry level {new} is thrown to monkey {m[3]}")
                else:
                    # print(f"Current worry level is not divisible by {m[2]}")
                    monkey[m[4]][0].append(new)
                    # print(f"Item with worry level {new} is thrown to monkey {m[4]}")
                counts[i] += 1
            m[0] = []

    counts.sort()
    return counts[-1] * counts[-2]


def part2():
    rounds = 10000
    counts = [0] * len(monkey2)
    # r = 0

    while rounds > 0:
        rounds -= 1
        # r += 1
        for i, m in enumerate(monkey2):
            for n in m[0]:
                new = m[1](n) % lcm
                if new % m[2] == 0:
                    monkey2[m[3]][0].append(new)
                else:
                    monkey2[m[4]][0].append(new)
                counts[i] += 1
            m[0] = []
        # if r == 1 or r == 20 or r % 1000 == 0:
        #     print(counts)
    counts.sort()
    return counts[-1] * counts[-2]


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
