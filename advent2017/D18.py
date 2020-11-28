import sys
from collections import defaultdict as dd
instr = sys.stdin.readlines()

def add(a, v):
    return 2
def myset(a, v):
    return 8

regs = dd(int)
funcs = {'add': add, 'set': myset}
for i in instr:
    data = i.split()
    f = funcs[data[0]]
    f()
