blocks = list(map(int, input().split()))
count = 0
seen = {str(blocks):0}
loop = 0

def redistribute(b):
    index, value= max(enumerate(b), key=lambda x: x[1])
    b[index] = 0
    for i in range(index + 1, index + value + 1):
        b[i % len(b)] += 1

#print(blocks)
while 1:
    count += 1
    redistribute(blocks)
    if str(blocks) in seen:
        break
    else:
        seen[str(blocks)] = count
    #print(blocks)
print(count)
print('Size of loop', (count - seen[str(blocks)]))
