import os
import sys
import json
import re
import copy

monkeys = {}
lcm = 1

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    INPUT = f.read().split("\n")

    id = None
    for line in INPUT:
        if line:
            if line.startswith("M"):
                id = re.findall(r"\d+", line)[-1]
                if id not in monkeys:
                    monkeys[id] = {}
                    monkeys[id]["count"] = 0
                    continue
            if line.startswith("  S"):
                items = re.findall(r"\d+", line)
                monkeys[id]["items"] = [int(x) for x in items]
                continue
            if line.startswith("  O"):
                o = line.split("=")[1]
                op = o.split()
                operation = op[-2]
                num = op[-1]
                if num == "old":
                    if operation == "+":
                        monkeys[id]["opdesc"] = "+o"
                    elif operation == "*":
                        monkeys[id]["opdesc"] = "*o"
                else:
                    if operation == "+":
                        monkeys[id]["opdesc"] = f"+ {num}"
                    elif operation == "*":
                        monkeys[id]["opdesc"] = f"* {num}"
                continue
            if line.startswith("  T"):
                num = int(re.findall(r"\d+", line)[-1])
                lcm = lcm * num
                monkeys[id]["divby"] = num
                continue
            if line.startswith("    If true"):
                target = re.findall(r"\d+", line)[-1]
                monkeys[id]["T"] = target
            if line.startswith("    If false"):
                target = re.findall(r"\d+", line)[-1]
                monkeys[id]["F"] = target

    monkeys2 = copy.deepcopy(monkeys)


def runop(i, op):
    if op == "*o":
        return i * i
    if op == "+o":
        return i + i
    if op.startswith("*"):
        num = int(re.findall(r"\d+", op)[-1])
        return i * num
    if op.startswith("+"):
        num = int(re.findall(r"\d+", op)[-1])
        return i + num


def part1():
    rounds = 20

    while rounds > 0:
        # print(f"Round {rounds}")
        rounds -= 1
        for id, m in monkeys.items():
            # print()
            # print(m)
            items = m["items"][:]
            # print(items)
            m["items"] = []
            for i in items:
                new = runop(i, m["opdesc"])
                # print(f"Worry level {i} to {new} opdesc: {m['opdesc']}")
                new = new // 3
                # print(f"Worry level is divided by 3 to {new}")
                if new % m["divby"] == 0:
                    # print(f"Current worry level is divisible by {m['divby']}")
                    monkeys[m["T"]]["items"].append(new)
                    # print(f"Item with worry level {n} is thrown to monkey {m['T']}")
                else:
                    # print(f"Current worry level is not divisible by {m['divby']}")
                    monkeys[m["F"]]["items"].append(new)
                    # print(f"Item with worry level {n} is thrown to monkey {m['F']}")
                m["count"] += 1
                # print(f"monkey {id} count = {m['count']}")
    counts = []
    for _, m in monkeys.items():
        counts.append(m["count"])
    counts.sort()
    return counts[-1] * counts[-2]


def part2():
    rounds = 10000
    r = 0
    while rounds > 0:
        r += 1
        # print(f"Round {r}")
        rounds -= 1
        for id, m in monkeys2.items():
            # print()
            # print(m)
            items = m["items"]
            # print(items)
            m["items"] = []
            for i in items:
                new = runop(i, m["opdesc"])
                # print(f"Worry level {i} to {new} opdesc: {m['opdesc']}")
                # new = new // 3
                # print(f"Worry level is divided by 3 to {new}")
                if new % m["divby"] == 0:
                    # print(f"Current worry level is divisible by {m['divby']}")
                    monkeys2[m["T"]]["items"].append(new % lcm)
                    # print(f"Item with worry level {n} is thrown to monkey {m['T']}")
                else:
                    # print(f"Current worry level is not divisible by {m['divby']}")
                    monkeys2[m["F"]]["items"].append(new % lcm)
                    # print(f"Item with worry level {n} is thrown to monkey {m['F']}")
                m["count"] += 1
                # print(f"monkey {id} count = {m['count']}")
    counts = []
    for _, m in monkeys2.items():
        counts.append(m["count"])
    counts.sort()
    return counts[-1] * counts[-2]


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
