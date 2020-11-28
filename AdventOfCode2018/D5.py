from fetch import fetch
import sys

fetch(5)
caps = [chr(ord('A') + ch) for ch in range(26) ]

gem = [chr(ord('a') + ch) for ch in range(26) ]
#print(caps)
pairs = []
pl = []
for index in range(26):
    pairs.append([caps[index], gem[index]])
    pl.append(caps[index] + gem[index])
    pl.append(gem[index]+ caps[index])
#print(pairs)
data = sys.stdin.read().strip()
#print(data)
#print(len(data))
def react(data):
    c=len(data)
    while True:
        for p in pl:

            data = data.replace(p, '')
        if len(data) < c:
            c = len(data)
        else:
            break
    return len(data), data
INF = 10**12
res = INF
_, data = react(data)
for pair in pairs:
    testdata =data
    for p in pair:
        testdata = testdata.replace(p, '')
    tres, _ = react(testdata)
    res= min(res, tres)
print(res)
#for line in data:
