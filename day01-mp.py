
"""
Use multiprocessing - this is about 20x slower for the day 1 problem
"""
from multiprocessing import Pool
import dill as pickle


def x(numlist):
    return sum(numlist)


if __name__ == "__main__":
    with open('input01.txt', 'r') as f:
        splitlist = []
        temp = []
        for line in f:
            line = line.strip()
            if line:
                temp.append(int(line))
            else:
                splitlist.append(temp)
                temp = []

    top3 = [0, 0, 0]
    with Pool(8) as p:
        res = p.map(sum, splitlist)

    for n in res:
        top3.sort()
        top3[0] = max(top3[0], n)

    print(f"{top3}")
    print(top3[0] + top3[1] + top3[2])

