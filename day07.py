import os
import json
import re

with open(os.environ.get("AOC_INPUT", "input07.txt"), "r") as f:
    INPUT = f.read().split("\n")

    fs = {}
    currdir = fs
    currdir["_size_"] = 0

    dirs = {}
    curr = "/"

    for line in INPUT:
        if line.startswith("$"):
            if line.startswith("$ cd "):
                dirname = line.split("$ cd ")[1]
                if dirname == "/":
                    curr = "/"
                elif dirname == "..":
                    currlist = curr.split("/")
                    curr = "/".join(currlist[:-1])
                else:
                    curr = f"{curr}/{dirname}"

                if curr not in dirs:
                    dirs[curr] = {"_size": 0}
        else:
            if line.startswith("dir"):
                dirname = line.split("dir ")[1]
                if "_subdirs" not in dirs[curr]:
                    dirs[curr]["_subdirs"] = []
                dirs[curr]["_subdirs"].append(f"{curr}/{dirname}")
            else:
                f = line.split(" ")
                fname = f[1]
                fsize = int(f[0])
                if "_size" not in dirs[curr]:
                    dirs[curr]["_size"] = 0
                dirs[curr]["_size"] += fsize


def treesize(dir):
    if "_rsize" in dirs[dir]:
        return dirs[dir]["_rsize"]

    tot = 0
    if "_size" in dirs[dir]:
        tot += dirs[dir]["_size"]
    if "_subdirs" in dirs[dir]:
        for d in dirs[dir]["_subdirs"]:
            tot += treesize(d)
    dirs[dir]["_rsize"] = tot
    return tot


def part1():
    tot = 0
    for dir, _ in dirs.items():
        if dir == "/":
            continue
        sz = treesize(dir)
        if sz <= 100000:
            tot += sz
    return tot


def part2():
    target = treesize("/") - 40000000
    mindif = float("inf")
    mindir = ""

    for d in dirs:
        dif = treesize(d) - target
        if dif >= 0 and dif < mindif:
            mindif = dif
            mindir = d
    return treesize(mindir)


def main():
    ret = {}
    ret["part_one"] = part1()
    ret["part_two"] = part2()
    print(f"{json.dumps(ret)}")


if __name__ == "__main__":
    main()
