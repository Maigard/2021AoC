import collections

def parse_input(filename: "str"):
    with open(filename, "r") as file:
        rules = {}
        start = file.readline().rstrip()
        file.readline()
        for line in file:
            line = line.rstrip().split(" ")
            rules[line[0]] = line[2]
    return start, rules

def count_pairs(polymer: "dict", lastChar: "str") -> "int":
    counts = collections.defaultdict(int)
    for (k, v) in polymer.items():
        counts[k[0]] += v
    counts[lastChar] += 1
    return counts

def main():
    (polymerstring, rules) = parse_input("14/inputs.txt")
    polymer = collections.defaultdict(int)
    for i in range(len(polymerstring) - 1):
        polymer[str(polymerstring[i:i+2])] += 1
    for i in range(40):
        newPolymer = collections.defaultdict(int)
        for k in polymer:
            newPolymer[k[0]+rules[k]] += polymer[k]
            newPolymer[rules[k]+k[1]] += polymer[k]
        polymer = newPolymer
    count = count_pairs(polymer, polymerstring[-1])
    print(max(count.values()) - min(count.values()))

main()
