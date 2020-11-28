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

def behaves_like(regbef, regafter, a, b, c):
    likes = set()
    for opcode, func in op.items():
        testli = list(regbef)
        cres = func(regbef, a, b)
        testli[c] = cres
        if testli == regafter:
            likes.add(opcode)
    return likes

def findone(c):
    for i, s in enumerate(c):
        if len(s) == 1:
            return i, s.pop()
    return -1, ''

def prune(cand):
    assignment = {}
    fixedcode, fixedop = findone(cand)
    while fixedcode > -1:
        assignment[fixedcode] = fixedop
        for c in cand:
            if fixedop in c:
                c.remove(fixedop)
        fixedcode, fixedop = findone(cand)
    return assignment

data = sys.stdin.read()
parts = data.split('\n\n\n\n')
part1 = parts[0].split('\n\n')
cand = [set(op.keys()) for _ in range(16)]

for chunk in part1:
    chunk = chunk.replace('Before:', '').replace('After:', '')
    test = chunk.split('\n')
    regbef= eval(test[0])
    regaft = eval(test[2])
    opcode, a,b, c = map(int, test[1].split())
    same = behaves_like(regbef, regaft,a, b, c)
    cand[opcode] = cand[opcode] & same
#print(cand)
ass = prune(cand)
#print(ass)
#print(len(ass))
register = [0, 0, 0, 0]
part2 = parts[1].strip().split('\n')

for codeline in part2:
    opcode, a, b, c = map(int, codeline.split())
    func = op[ass[opcode]]
    register[c] = func(register, a, b)
print(register[0])
