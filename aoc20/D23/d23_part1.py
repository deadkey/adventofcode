import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *

from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())

def getdest(v, order):
    targetv = v -1
    while True:
        db('Targetv', targetv)
        for i, c in enumerate(order):
        
            if c == targetv:
                return i
        targetv -= 1
        if targetv <= 0: targetv = 9

def one(i, curr, order):
    L = len(order)
    val = order[curr]
    db('\nNew step', i+1, '\n', val, order)
    
    picked = []
    for i in range(1, 4):
        ind = (curr + i) % L
        picked.append(order[ind])
    for p in picked:
        order.remove(p)
    db(curr, val, order)
    db(picked)
    dest = getdest(val, order)
    for i, p in enumerate(picked):

        order.insert(dest +1 + i, p)
    db('Dest val', order[dest])
    db(order)
    curr = (order.index(val) + 1) % L
    return order, curr


def solve(order, N):
    curr = 0
    for i in range(N):
        order, curr = one(i, curr, order)
    start = order.index(1) +1
    out = []
    for i in range(len(order)-1):
        out.append(str(order[(start + i)% len(order)]))
    return ''.join(out)
    



def p1(v):
    lines = v.strip()
    order = lazy_ints(list(v))
    N = 100
    return solve(order, N)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,23, p1, p2, cmds)
if stats: print_stats()
#manual()
