from collections import defaultdict

def parse_input(filename: "str") -> "dict":
    map = defaultdict(list)
    with open("12/inputs.txt", "r") as file:
        for line in file:
            nodes = line.rstrip().split("-")
            map[nodes[0]].append(nodes[1])
            map[nodes[1]].append(nodes[0])
    return map

routes = []
def walk_map(map: "dict", node: "str", visited: "list"):
    if node == "end":
        routes.append(visited + [node])
        return
    for nextNode in map[node]:
        if nextNode.isupper() or nextNode not in visited:
            walk_map(map, nextNode, visited + [node])

def main():
    map = parse_input("12/sampleinputs.txt")
    walk_map(map, "start", [])
    print(len(routes))

main()
