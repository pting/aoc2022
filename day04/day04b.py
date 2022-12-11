import re
import os
import sys
import json

path = os.path.dirname(os.path.abspath(__file__))
inputname = sys.argv[1] if len(sys.argv) > 1 else os.path.join(path, "input.txt")
with open(os.environ.get("AOC_INPUT", inputname), "r") as f:
    data = re.findall("(\d+)-(\d+),(\d+)-(\d+)", f.read())
    data = [[int(e) for e in row] for row in data]

contained = [(a <= c <= d <= b or c <= a <= b <= d) for a, b, c, d in data]
overlap = [max(a, c) <= min(b, d) for a, b, c, d in data]

ret = {}
ret["part_one"] = sum(contained)
ret["part_two"] = sum(overlap)
print(f"{json.dumps(ret)}")
