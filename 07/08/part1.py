def parse_inputs(filename):
    digits = []
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip().split("|")
            input = line[0].split()
            output = line[1].split()
            digits.append({"input": input, "output": output})
    return digits

def main():
    digits = parse_inputs("08/inputs.txt")
    count = 0
    for digit in digits:
        for output in digit["output"]:
            if len(output) in (2, 4, 3, 7):
                count += 1
    print(count)

main()