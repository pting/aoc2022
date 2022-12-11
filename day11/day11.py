import os
import sys
import json


path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input11.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    INPUT = f.read().split("\n")


def part2():

    for line in INPUT:
        if line:
            pass

def part1():

    for line in INPUT:
        if line:
            pass


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
