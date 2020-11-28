from collections import defaultdict as dd
import sys
lines = sys.stdin.readlines()
regs = dd(int)
highest = 0
inst = {'inc': ' += ', 'dec': ' -= '}

for line in lines:
    r1, ins, v, _, r2, c, v2 = line.split()
    if eval(str(regs[r2]) + c + v2):
            exec('regs[r1]'+ inst[ins] + v)
            highest = max(highest, regs[r1])

print(max(regs.values()))
print('highest: ', highest)
