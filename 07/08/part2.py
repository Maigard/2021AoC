def parse_inputs(filename):
    digits = []
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip().split("|")
            input = line[0].split()
            output = line[1].split()
            digits.append({"input": input, "output": output})
    return digits

def get_display(digit):
    display = {}
    segments = {}
    for letter in "abcdefg":
        count = sum([1 for i in digit if letter in set(i)])
        if count == 4:
            segments["bottomleft"] = letter
        elif count == 6:
            segments["topleft"] = letter
        elif count == 9:
            segments["bottomright"] = letter
        elif count == 8:
            one = [i for i in digit if len(i) == 2][0]
            if letter in set(one):
                segments["topright"] = letter
            else:
                segments["top"] = letter
        elif count == 7:
            four = [i for i in digit if len(i) == 4][0]
            if letter in set(four):
                segments["middle"] = letter
            else:
                segments["bottom"] = letter

    for input in digit:
        input = "".join(sorted(input))
        if len(input) == 2:
            display[input] = 1
        elif len(input) == 4:
            display[input] = 4
        elif len(input) == 3:
            display[input] = 7
        elif len(input) == 7:
            display[input] = 8
        elif len(input) == 5:
            if segments["topleft"] in input:
                display[input] = 5
            elif segments["bottomright"] in input:
                display[input] = 3
            else:
                display[input] = 2
        elif len(input) == 6:
            if segments["bottomleft"] not in input:
                display[input] = 9
            elif segments["middle"] not in input:
                display[input] = 0
            else:
                display[input] = 6
    return display

def main():
    digits = parse_inputs("08/inputs.txt")
    sum = 0
    for digit in digits:
        display = get_display(digit["input"])
        sum += int("".join([str(display["".join(sorted(i))]) for i in digit["output"]]))
    print(sum)
                
main()