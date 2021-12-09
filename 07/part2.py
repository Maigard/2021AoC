def main():
    locations = [int(i) for i in open("07/inputs.txt", "r").readline().rstrip().split(",")]
    fuelCosts = [0]
    for i in range(1, max(locations)+1):
        fuelCosts.append(fuelCosts[-1]+i)
    bestlocation = (999999999,0)
    for pos in range(min(locations), max(locations)+1):
        cost = sum([fuelCosts[abs(location - pos)] for location in locations])
        if cost < bestlocation[0]:
            bestlocation = (cost, pos)
    print(bestlocation)

main()


1, 3, 6, 10, 15, 21