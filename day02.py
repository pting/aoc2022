import os

INPUTFILE=os.environ.get("AOC_INPUT", "input02.txt")

myselect = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

part1 = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "Y": 3,
        "Z": 6,
        "X": 0
    },
    "C": {
        "Z": 3,
        "X": 6,
        "Y": 0
    }
}

part2 = {
    "A": {
        "X": (0, "Z"),
        "Y": (3, "X"),
        "Z": (6, "Y")
    },
    "B": {
        "X": (0, "X"),
        "Y": (3, "Y"),
        "Z": (6, "Z")
    },
    "C": {
        "X": (0, "Y"),
        "Y": (3, "Z"),
        "Z": (6, "X")
    }
}

def main():
    with open(INPUTFILE, 'r') as f:
        score1 = 0
        score2 = 0
        round = 0

        for line in f:
            line = line.strip()
            line = line.split(" ")
            # print(f"{line}")
            round = 0

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

            round = myselect[line[1]]
            round += part1[line[0]][line[1]]
            score1 += round

            round = 0
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

            res = part2[line[0]][line[1]]
            score2 += (res[0] + myselect[res[1]])

        print(f"Part 1: {score1}, Part 2: {score2}")


if __name__ == "__main__":
    main()