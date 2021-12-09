def main():
    fish = [int(i) for i in open("06/inputs.txt", "r").readline().split(",")]
    for day in range(80):
        newfish = []
        children = 0
        for f in fish:
            if f == 0:
                newfish.append(6)
                children += 1
            else:
                newfish.append(f-1)
        newfish += [8] * children
        fish = newfish
    print(len(fish))

main()