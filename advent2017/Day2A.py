import sys
lines = sys.stdin.readlines()
tot = 0
for line in lines:
    nbrs = list(map(int, line.split()))
    tot += max(nbrs) - min(nbrs)
print(tot)
