
"""
Use multiprocessing - this is about 20x slower for the day 1 problem
"""
from multiprocessing import Pool
import dill as pickle
import os

N = 3
INPUTFILE=os.environ.get("AOC_INPUT", "input01.txt")

def x(numlist):
    return sum(numlist)


if __name__ == "__main__":
    with open(INPUTFILE, 'r') as f:
        splitlist = []
        temp = []
        for line in f:
            line = line.strip()
            if line:
                temp.append(int(line))
            else:
                splitlist.append(temp)
                temp = []

    top = [0] * N
    with Pool(8) as p:
        res = p.map(sum, splitlist)

    for n in res:
        if n > top[0]:
            top[0] = n
            top.sort()

    print(f"{top}")
    print(sum(top))

