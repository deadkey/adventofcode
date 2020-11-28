from fetch import fetch, fetchlines
from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
import sys

op = {
'addr': lambda reg, a, b: reg[a] + reg[b],
'addi': lambda reg, a, b: reg[a] + b,
'mulr': lambda reg, a, b: reg[a] * reg[b],
'muli': lambda reg, a, b: reg[a] * b,
'banr': lambda reg, a, b: reg[a] & reg[b],
'bani': lambda reg, a, b: reg[a] & b,
'borr': lambda reg, a, b: reg[a] | reg[b],
'bori': lambda reg, a, b: reg[a] | b,
'setr': lambda reg, a, b: reg[a],
'seti': lambda reg, a, b: a,
'gtir': lambda reg, a, b: int(a > reg[b]),
'gtri': lambda reg, a, b: int(reg[a] > b),
'gtrr': lambda reg, a, b: int(reg[a] > reg[b]),
'eqir': lambda reg, a, b: int(a == reg[b]),
'eqri': lambda reg, a, b: int(reg[a] == b),
'eqrr': lambda reg, a, b: int(reg[a] == reg[b]),
}

test = sys.stdin.readlines() 
regs = [1, 0, 0, 0, 0,0]
ipindex = 5
ip = 0
inst = []
for line in test:
    li = line.split()
    ins = li[0]
    a, b, c = map(int, li[1:])
    inst.append((ins, a, b, c))
#print(inst)
#execute
cnt = 0
while ip < len(inst) and cnt< 100:
    regs[ipindex] = ip
    cnt += 1    
    ins, a, b, c = inst[ip]
    func = op[ins]
    cval = func(regs, a, b)
    regs[c] = cval
    preip = ip
    ip = regs[ipindex]

    print('ip = {} (my instr {}) {}'.format(preip, preip +1, regs))
    ip += 1
print(regs[0])