def parse_input(filename):
    dots = []
    folds = []
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            if line.startswith("fold along"):
                (dir,line) = line.split()[2].split("=")
                folds.append((dir, int(line)))
            elif "," in line:
                dots.append([int(i) for i in line.split(",")])
    return dots, folds

def make_paper(paper: "list") -> "list":
    (maxx, maxy) = (0, 0)
    for (x, y) in paper:
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    grid = [[False for x in range(maxx + 1)] for y in range(maxy + 1)]
    for (x, y) in paper:
        grid[y][x] = True
    return grid

def main():
    (dots, folds) = parse_input("13/inputs.txt")
    for (dir, line) in folds[:1]:
        for dot in range(len(dots)):
            comp = {"x": 0, "y": 1}[dir]
            if dots[dot][comp] > line:
                dots[dot][comp] = line + (line - dots[dot][comp])
    count = 0
    for y in make_paper(dots):
        for x in y:
            count += x
    print(count)

main()
