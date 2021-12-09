inputs = [int(i) for i in open("01/inputs.txt","r").readlines()]
increased=0
prev = sum(inputs[0:3])
for i in range(1,len(inputs)-2):
    val = sum(inputs[i:i+3])
    if val > prev:
        increased += 1
    prev = val
print(increased)