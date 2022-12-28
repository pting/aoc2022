import os
import sys
import json


path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")


def part1():
    tot = 0
    chars = "=-012"

    for l in lines:
        if l:
            place = 1
            for c in l[::-1]:
                tot += (chars.index(c) - 2) * place
                place *= 5

    chars = "   =-"
    ret = ""

    while tot:
        rem = tot % 5
        tot //= 5

        if rem <= 2:
            ret = str(rem) + ret
        else:
            ret = chars[rem] + ret
            tot += 1

    return ret


def part2():
    return None


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
