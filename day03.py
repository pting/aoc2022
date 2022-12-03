import os
import json

INPUTFILE=os.environ.get("AOC_INPUT", "input03.txt")

def part1(input):
    res = 0
    for line in input:
        if line:
            size = len(line)//2
            A = set(line[:size])
            B = set(line[size:])
            I = next(iter(A.intersection(B)))
            
            if I.islower():
                res += ord(I) - ord('a') + 1
            else:
                res += ord(I) - ord('A') + 27
    return res


def helper(input):
    I = {}
    for line in input:
        if line:
            if I:
                I = I.intersection(set(line))
            else:
                I = set(line)
    L = next(iter(I))
    if L.islower():
        return ord(L) - ord('a') + 1
    else:
        return ord(L) - ord('A') + 27   


def part2(input):
    res = 0
    for i in range(0, len(input), 3):
        res += helper(input[i:i + 3])
    return res


def main():
    with open(INPUTFILE, 'r') as f:
        input = f.read().split("\n")

    ret = {}
    ret["part_one"] = part1(input)
    ret["part_two"] = part2(input)
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()