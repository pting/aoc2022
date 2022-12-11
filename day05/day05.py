import os
import json
import re
import sys


def parsestack(line):
    n = 4
    return [line[i : i + n] for i in range(0, len(line), n)]


path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input05.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    INPUT = f.read().split("\n")
    STACKINPUT = []
    MOVEMENT = []
    for line in INPUT:
        if line:
            if line.startswith("m"):
                MOVEMENT.append(
                    [
                        int(x)
                        for x in re.match(
                            "move (\d+) from (\d+) to (\d+)", line
                        ).groups()
                    ]
                )
            elif "[" in line:
                STACKINPUT.append(parsestack(line))
    # One for each part
    STACK1 = []
    STACK2 = []
    # Parse in reverse order to set up queues
    for line in STACKINPUT[::-1]:
        while len(STACK1) < len(line):
            STACK1.append([])
            STACK2.append([])
        for i, stack in enumerate(line):
            id = re.match("\[[a-zA-Z]+\]", stack)
            if id:
                STACK1[i].append(id)
                STACK2[i].append(id)


def part1():
    for moveint in MOVEMENT:
        for _ in range(moveint[0]):
            STACK1[moveint[2] - 1].append(STACK1[moveint[1] - 1].pop())
    return "".join([row[-1][0][1] for row in STACK1])


def part2():
    for moveint in MOVEMENT:
        m = []
        for _ in range(moveint[0]):
            m.append(STACK2[moveint[1] - 1].pop())
        for id in m[::-1]:
            STACK2[moveint[2] - 1].append(id)
    return "".join([row[-1][0][1] for row in STACK2])


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
