import os
import json
import sys

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    INPUT = f.read()


def helper(n):
    i = n
    while True:
        if len(set(INPUT[i - n : i])) == n:
            return i
        else:
            i += 1


def main():
    ret = {}
    ret["part_one"] = helper(4)
    ret["part_two"] = helper(14)
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
