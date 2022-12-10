import os
import json
import sys

N = 3
INPUTFILE=os.environ.get("AOC_INPUT", sys.argv[1])

def calc(N, input):
    res = 0
    top = [0] * N

    for line in input:
        if not line:
            if res > top[0]:
                top[0] = res
                top.sort()
            res = 0
        else:
            res += int(line)
    return sum(top)


def main():
    with open(INPUTFILE, 'r') as f:
        input = f.read().split("\n")

    ret = {}
    ret["part_one"] = calc(1, input)
    ret["part_two"] = calc(3, input)
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()