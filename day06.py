import os
import json
import sys

with open(os.environ.get("AOC_INPUT", sys.argv[1]), "r") as f:
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
