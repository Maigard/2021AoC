inputs = [(i.split()[0], int(i.split()[1])) for i in open("02/inputs.txt","r").readlines()]
dist, depth, aim = (0,0, 0)
for dir in inputs:
    if dir[0] == "forward":
        dist += dir[1]
        depth += aim * dir[1]
    elif dir[0] == "down":
        aim += dir[1]
    elif dir[0] == "up":
        aim -= dir[1]
print(dist, depth, dist*depth)