N = 3

def main():
    with open('input01.txt', 'r') as f:
        res = 0
        top = [0] * N

        for line in f:
            line = line.rstrip()
            if not line:
                top.sort()
                top[0] = max(top[0], res)
                res = 0
            else:
                res += int(line)

        print(sum(top))


if __name__ == "__main__":
    main()