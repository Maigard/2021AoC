from functools import reduce

def parse_input(filename):
    with open(filename, "r") as file:
        return [
            [int(i) for i in line.rstrip()] for line in file
        ]
checked = []
def basin_size(map, x, y):
    if (x, y) in checked:
        return 0
    checked.append((x, y))
    # print(checked)
    sum = 0
    if map[y][x] == 9:
        return 0
    if y-1 >= 0:
        sum += basin_size(map, x, y-1)
    if y+1 < len(map):
        sum += basin_size(map, x, y+1)
    if x-1 >= 0:
        sum += basin_size(map, x-1, y)
    if x+1 < len(map[y]):
        sum += basin_size(map, x+1, y)
    return sum + 1

def main():
    map = parse_input("09/inputs.txt")
    lowPoints = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            adjacent = []
            if y-1 >= 0:
                adjacent.append(map[y-1][x])
            if y+1 < len(map):
                adjacent.append(map[y+1][x])
            if x-1 >= 0:
                adjacent.append(map[y][x-1])
            if x+1 < len(map[y]):
                adjacent.append(map[y][x+1])
            if map[y][x] < min(adjacent):
                lowPoints.append((x,y))
    basinSizes = []
    for (x, y) in lowPoints:
        # print(map[y][x], x, y)
        checked = []
        basinSizes.append(basin_size(map, x, y))
    print(reduce(lambda a,b: a*b, sorted(basinSizes)[-3:]))
main()