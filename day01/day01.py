import os
import json
import sys

N = 3
path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input01.txt")
INPUTFILE = os.environ.get("AOC_INPUT", inputname)


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
    with open(INPUTFILE, "r") as f:
        input = f.read().split("\n")

    ret = {}
    ret["part_one"] = calc(1, input)
    ret["part_two"] = calc(3, input)
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
