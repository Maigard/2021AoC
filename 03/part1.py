inputs = [i.rstrip() for i in open("03/inputs.txt","r").readlines()]
count = [0] * 12
for i in inputs:
    for (loc, digit) in enumerate(i):
        if digit == "1":
            count[loc] += 1
(gamma, epsilon) = (0,0)
numInputs = len(inputs)
for (loc, digit) in enumerate(count):
    if digit > numInputs/2:
        gamma ^= 2**(len(count)-loc-1)
    else:
        epsilon ^= 2**(len(count)-loc-1)
print(gamma, epsilon, gamma*epsilon)