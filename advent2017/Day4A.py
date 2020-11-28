import sys
lines = sys.stdin.readlines()
tot = 0
def valid(w):
    sortedwords = map(str, map(sorted, w))
    return len(set(sortedwords)) == len(w)
pws = set()
for line in lines:
    pws.add(line.strip())
#print(pws)
for pw in pws:
    if valid(pw.split()):
        tot += 1
print(tot)
