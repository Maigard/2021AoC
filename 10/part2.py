import pprint
closer = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}"
}
points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def score_string(input: "str") -> "int":
    score = 0
    for i in input:
        score = (score * 5) + points[i]
    return score

def main():
    nav = []
    with open("10/inputs.txt", "r") as file:
        nav = [i.rstrip() for i in file]
    scores = []
    for i in nav:
        stack = []
        for char in i:
            if char in closer:
                stack.append(closer[char])
            else:
                if char != stack.pop():
                    break
        else:
            stack.reverse()
            scores.append(score_string(stack))
    print(sorted(scores)[len(scores)//2])
main()
