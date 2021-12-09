inputs = [int(i) for i in open("01/inputs.txt","r").readlines()]
increased=0
prev = inputs[0]
for line in inputs[0:]:
    if line > prev:
        increased += 1
    prev = line
print(increased)