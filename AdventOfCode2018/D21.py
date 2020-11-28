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


def testrun(regs, inst):
    seen = set()
    ip = regs[ipindex]
    state = (ip, tuple(regs))
    twos = set()
    lastadded2 = 0
    while ip < len(inst):
        
        regs[ipindex] = ip
        ins, a, b, c = inst[ip]
        func = op[ins]
        cval = func(regs, a, b)
        regs[c] = cval
        preip = ip
        ip = regs[ipindex]
        state = tuple(regs)
        if ip == 28:
            if state in seen:
                
                return lastadded2
        
            else:    
                seen.add(state)
            if regs[2] not in twos:
                twos.add(regs[2])
                lastadded2 = regs[2]
                print(lastadded2)
            #  exit()
        ip += 1
    return 0


test = fetchlines(21)

regs= [0, 0, 0, 0, 0, 0]
ipindex = 4
ip = regs[ipindex]


inst = []
for line in test:
    li = line.split()
    ins = li[0]
    a, b, c = map(int, li[1:])
    inst.append((ins, a, b, c))

res = testrun(regs, inst)
print(res)