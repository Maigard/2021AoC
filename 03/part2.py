def mostLeast(inputs):
    count = [0] * len(inputs[0])
    for i in inputs:
        for (loc, digit) in enumerate(i):
            if digit == "1":
                count[loc] += 1
    (gamma, epsilon) = [["0"]*len(count), ["0"]*len(count)]
    numInputs = len(inputs)
    for (loc, digit) in enumerate(count):
        if digit > numInputs/2:
            gamma[loc] = "1"
        elif digit == numInputs/2:
            gamma[loc] = "1"
            epsilon[loc] = "1"
        else:
            epsilon[loc] = "1"
    return ("".join(gamma), "".join(epsilon))

(ox, co2) = (0, 0)
allinputs = [i.rstrip() for i in open("03/inputs.txt","r").readlines()]
for system in ('ox', 'co2'):
    inputs = allinputs
    for digit in range(len(inputs[0])):
        (most, least) = mostLeast(inputs)
        valid = []
        for num in inputs:
            if most[digit] == least[digit]:
                if system == "ox" and num[digit] == "1":
                    valid.append(num)
                elif system == "co2" and num[digit] == "0":
                    valid.append(num)
            else:
                if system == "ox" and num[digit] == most[digit]:
                    valid.append(num)
                elif system == "co2" and num[digit] == least[digit]:
                    valid.append(num)
        if len(valid) == 1:
            break
        inputs = valid
    if system == "ox":
        ox = int(valid[0], 2)
    else:
        co2 = int(valid[0], 2)
print(ox, co2, ox*co2)