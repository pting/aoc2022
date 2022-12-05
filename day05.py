import os
import json
import re

def parsestack(line):
    n = 4
    return [line[i:i+n] for i in range(0, len(line), n)]


with open(os.environ.get("AOC_INPUT", "input05.txt"), "r") as f:
    INPUT = f.read().split("\n")
    STACKINPUT = []
    MOVEMENT = []
    for line in INPUT:
        if line:
            if "[" in line:
                STACKINPUT.append(parsestack(line))
            elif "move" in line:
                move = re.match("move (\d+) from (\d+) to (\d+)", line)
                moveints = []
                for item in move.groups():
                    moveints.append(int(item))
                MOVEMENT.append(moveints)
    STACK1 = []
    STACK2 = []
    # Parse in reverse order to set up queues
    for line in STACKINPUT[::-1]:
        ns = len(line)
        while len(STACK1) < ns:
            STACK1.append([])
            STACK2.append([])
        for i, stack in enumerate(line):
            id = re.match("\[[a-zA-Z]+\]", stack)
            if id:
                STACK1[i].append(id)
                STACK2[i].append(id)


def part1():
    for moveint in MOVEMENT:
        for i in range(moveint[0]):
            id = STACK1[moveint[1]-1].pop()
            STACK1[moveint[2]-1].append(id)
    return "".join([row[-1][0][1] for row in STACK1])


def part2():
    for moveint in MOVEMENT:
        m = []
        for i in range(moveint[0]):
            id = STACK2[moveint[1]-1].pop()
            m.append(id)
        for id in m[::-1]:
            STACK2[moveint[2]-1].append(id)
    return "".join([row[-1][0][1] for row in STACK2])


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
