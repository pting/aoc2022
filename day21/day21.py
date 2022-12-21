import os
import sys
import json
import re
import copy
from sympy.solvers import solve
from sympy import Symbol

GR = {}

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    lines = f.read().split("\n")
    for l in lines:
        if l:
            a = l.split(": ")
            k = a[0]
            v = a[1].split(" ")
            GR[k] = v


def helper(x):
    s = []
    for term in GR[x]:
        if re.match("^[a-z]{4}$", term):
            s += str(helper(term))
        else:
            s.append(term)
    e = "".join(s)
    n = int(eval(e))
    return n


def part1():
    final = helper("root")
    return final


def helper2(x, gr):
    s = []
    for term in gr[x]:
        if re.match("^[a-z]{4}$", term):
            s += str(helper2(term, gr))
        else:
            s.append(term)
    return "(" + "".join(s) + ")"


def part2():
    gr = copy.deepcopy(GR)
    gr["humn"] = "(humn)"

    a, b = gr["root"][0], gr["root"][2]
    expra = helper2(a, gr)
    exprb = helper2(b, gr)

    expr = f"{expra} - {exprb}"
    humn = Symbol("humn")
    res = solve(expr, humn, rational=True)
    return int(res[0])


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
