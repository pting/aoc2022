
def main():
    with open('input01.txt', 'r') as f:
        res = 0
        top3 = [0, 0, 0]

        for line in f:
            line = line.strip()
            if not line:
                top3.sort()
                top3[0] = max(top3[0], res)
                res = 0
            else:
                res += int(line)

        # print(f"{top3}")
        print(top3[0] + top3[1] + top3[2])


if __name__ == "__main__":
    main()