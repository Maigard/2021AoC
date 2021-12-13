def parse_input(filename: "str") -> "tuple(set, list)":
    dots = set()
    folds = []
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            if line.startswith("fold along"):
                (dir,line) = line.split()[2].split("=")
                folds.append((dir, int(line)))
            elif "," in line:
                dots.add(tuple([int(i) for i in line.split(",")]))
    return dots, folds

def print_paper(paper: "list"):
    (maxx, maxy) = (0, 0)
    for (x, y) in paper:
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    print("\n".join(["".join([{True: "#", False: " "}[(x, y) in paper] for x in range(maxx + 1)]) for y in range(maxy + 1)]))

def main():
    (dots, folds) = parse_input("13/inputs.txt")
    for (dir, line) in folds:
        newdots = set()
        for dot in dots:
            comp = {"x": 0, "y": 1}[dir]
            if dot[comp] > line:
                dot = list(dot)
                dot[comp] = line + (line - dot[comp])
                dot = tuple(dot)
            newdots.add(dot)
        dots = newdots
    print_paper(dots)

main()
