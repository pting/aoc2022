import os

INPUTFILE = os.environ.get("AOC_INPUT", "input02.txt")

inputA = {"A", "B", "C"}
inputB = {"X", "Y", "Z"}

part1 = {
    "A": {"X": 4, "Y": 8, "Z": 3},
    "B": {"Y": 5, "Z": 9, "X": 1},
    "C": {"Z": 6, "X": 7, "Y": 2},
}

part2 = {
    "A": {"X": 3, "Y": 4, "Z": 8},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 2, "Y": 6, "Z": 7},
}


def main():
    with open(INPUTFILE, "r") as f:
        score1 = 0
        score2 = 0

        input = f.read().split("\n")
        for line in input:
            if not line:
                continue
            line = line.split(" ")
            if not (line[0] and line[0] in inputA and line[1] and line[1] in inputB):
                continue

            # print(f"{line}")

            # Part 1
            # if line[1] == 'X':
            #     round += 1
            # elif line[1] == 'Y':
            #     round += 2
            # elif line[1] == 'Z':
            #     round += 3
            # # Draw
            # if (line[0] == 'A' and line[1] == 'X') or (line[0] == 'B' and line[1] == 'Y') or (line[0] == 'C' and line[1] == 'Z'):
            #     round += 3
            #     # print("Draw")
            # # Win
            # elif (line[0] == 'A' and line[1] == 'Y') or (line[0] == 'B' and line[1] == 'Z') or (line[0] == 'C' and line[1] == 'X'):
            #     round += 6
            #     # print("Win")

            score1 += part1[line[0]][line[1]]

            # Part 2 - X:lose, Y:draw, Z:Win
            # if line[1] == 'X':
            #     if line[0] == 'A':
            #         # pick Z
            #         round += 3
            #     elif line[0] == 'B':
            #         # pick X
            #         round += 1
            #     elif line[0] == 'C':
            #         # pick Y
            #         round += 2
            # elif line[1] == 'Y':
            #     if line[0] == 'A':
            #         # pick X
            #         round += 1
            #     elif line[0] == 'B':
            #         # pick Y
            #         round += 2
            #     elif line[0] == 'C':
            #         # pick Z
            #         round += 3
            #     round += 3
            # elif line[1] == 'Z':
            #     if line[0] == 'A':
            #         # pick Y
            #         round += 2
            #     elif line[0] == 'B':
            #         # pick Z
            #         round += 3
            #     elif line[0] == 'C':
            #         # pick X
            #         round += 1
            #     round += 6

            score2 += part2[line[0]][line[1]]

        print(f"Part 1: {score1}, Part 2: {score2}")


if __name__ == "__main__":
    main()
