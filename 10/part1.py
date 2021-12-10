import pprint
closer = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}"
}
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

def main():
    nav = []
    with open("10/inputs.txt", "r") as file:
        nav = [i.rstrip() for i in file]
    score = 0
    for i in nav:
        stack = []
        for char in i:
            if char in closer:
                stack.append(closer[char])
            else:
                if char != stack.pop():
                    score += points[char]
                    break
    print(score)
main()
