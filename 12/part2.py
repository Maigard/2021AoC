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
def walk_map(map: "dict", node: "str", visited: "list", visitedSmallNodeTwice: "bool"):
    if node == "end":
        routes.append(visited + [node])
        return
    if node.islower() and visitedSmallNodeTwice and node in visited:
        return
    for nextNode in map[node]:
        if nextNode != "start":
            visitedSmallNodeTwice = visitedSmallNodeTwice or (node.islower() and node in visited)
            walk_map(map, nextNode, visited + [node], visitedSmallNodeTwice)

def main():
    map = parse_input("12/inputs.txt")
    walk_map(map, "start", [], False)
    print(len(routes))

main()
