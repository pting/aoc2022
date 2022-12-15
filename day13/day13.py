import os
import sys
import json
import functools
import copy

# list(map(int, re.findall(r"\d+", l[1])))
pairs = []
p2 = []
path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    groups = f.read().split("\n\n")
    for gr in groups:
        g = gr.split()
        node = []
        for l in g:
            node.append(eval(l))
            p2.append(eval(l))

        pairs.append(node)


def checkp(L, R):
    while R and L:
        l = L.pop(0)
        r = R.pop(0)
        # print(f"Compare {l} vs {r}")

        if type(r) is int and type(l) is int:
            if r != l:
                if r > l:
                    return True
                if r < l:
                    return False
                continue
        if type(l) is list and type(r) is int:
            r = [r]
        elif type(r) is list and type(l) is int:
            l = [l]
        if type(l) is list and type(r) is list:
            if l or r:
                ret = checkp(l, r)
                if ret is not None:
                    return ret
    if R:
        return True
    if L:
        return False


def part1():
    res = [False]
    for p in pairs:

        # print(f"Compare {p[0]} vs {p[1]}")
        res.append(checkp(p[0], p[1]))
        # print(res[-1])

    ret = 0
    for i, v in enumerate(res):
        if v:
            ret += i
    # print(res)
    return ret


def part2():
    smaller = 1
    larger = len(p2) + 2

    for p in p2:
        pp = copy.deepcopy(p)
        if checkp(p, [[2]]):
            smaller += 1
        elif checkp([[6]], pp):
            larger -= 1
    # print(smaller)
    # print(larger)
    return smaller * larger


def part2sort():
    p2.append([[2]])
    p2.append([[6]])

    def mycmp(x, y):
        l = copy.deepcopy(x)
        r = copy.deepcopy(y)
        ret = checkp(l, r)
        if ret is None:
            return 0
        return -1 if ret else 1

    sp2 = sorted(p2, key=functools.cmp_to_key(mycmp))
    ret = 1
    for i, v in enumerate(sp2):
        if v in [[[2]], [[6]]]:
            # print(i + 1)
            ret *= i + 1
    return ret


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2sort()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
