import collections
def main():
    fishlist = [int(i) for i in open("06/inputs.txt", "r").readline().split(",")]
    fish = collections.defaultdict(lambda: 0)
    for f in fishlist:
       fish[f] += 1
    print(fish)
    for day in range(256):
        newfish = collections.defaultdict(lambda: 0)
        for f in fish:
            if f == 0:
                newfish[8] = fish[0]
                newfish[6] += fish[0]
            else:
                newfish[f-1] += fish[f]
        fish = newfish
        print(day, sum(fish.values()))

main()