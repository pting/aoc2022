import os
import json
import re

def parseline(line):
    n = 4
    return [line[i:i+n] for i in range(0, len(line), n)]


with open(os.environ.get("AOC_INPUT", "input05.txt"), "r") as f:
    INPUT = f.read().split("\n")
    PARSEDINPUT = []
    MOVEMENT = []
    for line in INPUT:
        if line:
            if "[" in line:
                PARSEDINPUT.append(parseline(line))
            elif "move" in line:
                MOVEMENT.append(line)


def getstacks():
    res = []
    for line in PARSEDINPUT:
        ns = len(line)
        while len(res) < ns:
            res.append([])
        for i, stack in enumerate(line):
            id = re.findall("\[[a-zA-Z]+\]", stack)
            if id:
                res[i].append(id)
    return res



def part1():
    stacks = getstacks()
    # print(f">>> {stacks}")
    for line in MOVEMENT:
        move = re.findall("move (\d+) from (\d+) to (\d+)", line)
        moveint = []
        for item in move[0]:
            moveint.append(int(item))
        # print(moveint)
        for i in range(moveint[0]):
            id = stacks[moveint[1]-1].pop(0)
            # print(f"moving {i}: {id} -----{stacks}")
            stacks[moveint[2]-1].insert(0, id)
            # print(stacks)
    res = ""
    for row in stacks:
        res += row[0][0][1]
    return res


def part2():
    stacks = getstacks()
    # print(f">>> {stacks}")
    for line in MOVEMENT:
        move = re.findall("move (\d+) from (\d+) to (\d+)", line)
        moveint = []
        for item in move[0]:
            moveint.append(int(item))
        # print(moveint)
        m = []
        for i in range(moveint[0]):
            id = stacks[moveint[1]-1].pop(0)
            # print(f"moving {i}: {id} -----{stacks}")
            m.append(id)
        
        for id in m[::-1]:
            stacks[moveint[2]-1].insert(0, id)
            # print(stacks)
        
    res = ""
    for row in stacks:
        res += row[0][0][1]
    return res


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
