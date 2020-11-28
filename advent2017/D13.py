import sys
from collections import defaultdict as dd
i = sys.stdin.readlines()
layers = dd(int)
for line in i:
    layer, depth = map(int, line.split(':'))
    layers[layer] = depth


time = 0
caught = []
end = max(layers)
while time <= end:
    depth = layers[time]
    per = (depth - 1) * 2
    if depth > 0 and time % per == 0:
        caught.append(time)
    time += 1
severity = 0
for c in caught:
    severity += c * layers[c]
print(severity)
def run(delay):
    time = 0
    while time <= end:
        depth = layers[time]
        per = (depth - 1) * 2
        if depth > 0 and (time + delay) % per == 0:
            return False
        time += 1
    return True
maxdelay = 10000000
delay = 0
while delay < maxdelay:
    if run(delay):
        break
    else:
        delay += 1
print(delay)
