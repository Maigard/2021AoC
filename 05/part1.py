import math
import collections

def parse_input(filename):
    directions = []
    with open(filename, "r") as file:
        for line in file:
            (start, _, end) = line.rstrip().split()
            start = [int(i) for i in start.split(",")]
            end = [int(i) for i in end.split(",")]
            directions.append((start, end))
    return directions

def main():
    floor = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
    dirs = parse_input("05/inputs.txt")
    (maxx, maxy) = (0, 0)
    for dir in dirs:
        if dir[0][0] == dir[1][0] or dir[0][1] == dir[1][1]:
            maxx = max(maxx, dir[0][0], dir[1][0])
            maxy = max(maxy, dir[0][1], dir[1][1])
            hyp = math.sqrt((dir[1][0]-dir[0][0])**2 + (dir[1][1]-dir[0][1])**2)
            slope = ((dir[1][0] - dir[0][0])/hyp, (dir[1][1] - dir[0][1])/hyp)
            cur = dir[0]
            while cur != dir[1]:
                floor[int(cur[1])][int(cur[0])] += 1
                cur = [int(cur[0] + slope[0]), int(cur[1] + slope[1])]
            floor[int(cur[1])][int(cur[0])] += 1
            

    intCount = 0
    for y in range(maxy+1):
        row = floor[y]
        for x in range(maxx+1):
            # print(row[x], end="")
            if row[x] > 1:
                intCount += 1
        # print()
    print(intCount)
main()