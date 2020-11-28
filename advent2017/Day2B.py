import sys
lines = sys.stdin.readlines()
tot = 0
def getDiv(ns):
    for n in ns:
        for m in ns:
            if n != m and n % m == 0:
                return n//m

for line in lines:
    nbrs = list(map(int, line.split()))
    tot += getDiv(nbrs)
print(tot)
