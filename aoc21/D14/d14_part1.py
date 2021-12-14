import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict as dd, Counter
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split(' -> '))
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    curr = list(chunks[0])
    subs = chunks[1].split('\n')
    rep = dd(str)
    for s in subs:
        a, b = parse(s)
        rep[a] = b 
    N = 10
    for _ in range(N):
        nxt = []
        for i in range(len(curr) -1):
            a = curr[i]
            b = curr[i+1]
            lt = a + b
            r = rep[lt]
            nxt.append(a)
            nxt.append(r)
        nxt.append(curr[-1])
        curr = nxt
    cnt = Counter(curr)
    mx = max(cnt.values())
    mn = min(cnt.values())

    return mx - mn

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,14, p1, p2, cmds)
if stats: print_stats()
#manual()
