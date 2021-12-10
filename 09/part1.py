def parse_input(filename):
    with open(filename, "r") as file:
        return [
            [int(i) for i in line.rstrip()] for line in file
        ]

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
    print(sum([map[y][x]+1 for (x,y) in lowPoints]))

main()
