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
    return lazy_ints(multisplit(line, ',', '->'))

grid = Counter()

def draw(a, b, c, d):
    if a == c or b == d:
        db('Line', a, b, c, d)
        a, c = min(a, c), max(a, c)
        b, d= min(b, d), max(b, d)
        for x in range(a, c + 1):
            for y in range(b, d + 1):
                grid[y, x] += 1

def printgrid():
    for r in range(10):
        out = []
        for c in range(10):
            out.append(str(grid[r, c]))
        db(''.join(out))
    db('\n')

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        a, b, c, d = data[i]
        draw(a, b, c, d)
        #printgrid()
    cnt = 0

    for k, v in grid.items():
        if v >= 2:
            cnt += 1

    for r in range(15):
        out = []
        for c in range(15):
            out.append(str(grid[r, c]))
        db(''.join(out))

    return cnt

def p2(v):
    return 0


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,5, p1, p2, cmds)
if stats: print_stats()
#manual()
