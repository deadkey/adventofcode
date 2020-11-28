from collections import Counter

val = 312051
c = Counter()

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
currDir = 0
x = 0
y = 0

def calcVal(x, y, c):
    indeces = [(xi, yi) for xi in range(x -1, x + 2) for yi in range(y-1, y +2)]
    s = 0
    for i in indeces:
        s += c[i]
    return s
c[(0, 0)] = 1
valWritten = 1
while valWritten <= val:
    valWritten = calcVal(x, y, c)
    c[(x, y)] = valWritten
    if abs(x) == abs(y):
        currDir = (currDir + 1) % 4

    if x == y and x >= 0:
        x += 1
    else:
        x += dirs[currDir][0]
        y += dirs[currDir][1]
print(valWritten)
