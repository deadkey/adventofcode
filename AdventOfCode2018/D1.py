from fetch import fetch
import sys
f = 0
"""
for line in sys.stdin.readlines():
    change = eval(line)
    f += change
print f
"""
lines = fetch(1).split() #sys.stdin.readlines()
seen = set([0])
index = 0
while True:
    change = eval(lines[index])
    index += 1
    index %= len(lines)
    f += change
    if f in seen:
        print("twice", f)
        exit()
    seen.add(f)
