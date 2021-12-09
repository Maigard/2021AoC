def main():
    locations = [int(i) for i in open("07/inputs.txt", "r").readline().rstrip().split(",")]
    bestlocation = (999999999,0)
    for pos in range(min(locations), max(locations)+1):
        cost = sum([abs(location - pos) for location in locations])
        if cost < bestlocation[0]:
            bestlocation = (cost, pos)
        print(pos, cost, bestlocation)

main()