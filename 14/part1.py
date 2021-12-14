from collections import Counter

def parse_input(filename: "str"):
    with open(filename, "r") as file:
        rules = {}
        start = file.readline().rstrip()
        file.readline()
        for line in file:
            line = line.rstrip().split(" ")
            rules[line[0]] = line[2]
    return start, rules

def insert_pair(polymer: "str", rules:"dict") -> "str":
    newPolymer = polymer[0]
    for i in range(len(polymer)-1):
        newPolymer += f"{rules[polymer[i:i+2]]}{polymer[i+1]}"
    return newPolymer

def main():
    (polymer, rules) = parse_input("14/inputs.txt")
    for i in range(10):
        polymer = insert_pair(polymer, rules)
    count = Counter(polymer)
    print(count.most_common()[0][1] - count.most_common()[-1][1])

main()
