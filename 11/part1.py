from pprint import pprint
def parse_input(filename: "str") -> "list":
    with open(filename, "r") as file:
        return [[int(char) for char in line.rstrip()] for line in file]

dirs = (
    (-1, -1), (-1, 0), (-1, +1),
    ( 0, -1),          ( 0, +1),
    (+1, -1), (+1, 0), (+1, +1)
)

def flash(octs: "list", x: "int", y: "int"):
    for dir in dirs:
        newx = x + dir[1]
        newy = y + dir[0]
        if 0 <= newy < len(octs) and 0 <= newx < len(octs[y]):
            octs[newy][newx] += 1
            if octs[newy][newx] == 10:
                flash(octs, newx, newy)

def main():
    octs = parse_input("11/inputs.txt")
    flashes = 0
    for step in range(100):
        for y in range(len(octs)):
            for x in range(len(octs[y])):
                octs[y][x] += 1
                if octs[y][x] == 10:
                    flash(octs, x, y)
        for y in range(len(octs)):
            for x in range(len(octs[y])):
                if octs[y][x] > 9:
                    flashes += 1
                    octs[y][x] = 0
    print(flashes)

main()
