import sys
lines = sys.stdin.readlines()
ins = []
for line in lines:
    ins.append(int(line.strip()))
index = 0
steps = 0
end = len(lines)
#print(ins)
while index >= 0 and index < end:
    jumps = ins[index]
    if jumps >= 3:
        ins[index] += -1
    else:
        ins[index] += 1
    index += jumps
    steps += 1
    #print(ins, ' new pos ' , index)
print(steps)
