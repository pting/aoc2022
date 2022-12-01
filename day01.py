import os

N = 3
INPUTFILE=os.environ.get("AOC_INPUT", "input01.txt")

def main():
    with open(INPUTFILE, 'r') as f:
        res = 0
        top = [0] * N

        for line in f:
            line = line.rstrip()
            if not line:
                if res > top[0]:
                    top[0] = res
                    top.sort()
                res = 0
            else:
                res += int(line)

        print(sum(top))


if __name__ == "__main__":
    main()