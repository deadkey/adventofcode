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
    return lazy_ints(line.split(','))

def solve(grid, folds):
    coord, val = folds[0]
    nxt = dd(int)
    for (x, y), k in grid.items():
        if k == 0: continue
        if coord == 'x':
            if x < val:
                nxt[x, y]= 1
            else:
                diff = x - val
                x = val - diff
                nxt[x, y] = 1
        else:
            if y < val:
                nxt[x, y]= 1
            else:
                diff = y - val
                y = val - diff
                nxt[x, y] = 1
        grid = nxt
    return sum(grid.values())

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in chunks[0].split('\n')]
    su = 0
    grid = dd(int)
    for i in range(len(data)):
        d = data[i]
        db(d)

        x, y = d
        grid[x, y] = 1
    printdict(grid)
    folds = []
    for l in chunks[1].split('\n'):
        p = l.split('=')
        coord = p[0][-1]
        val = int(p[1])
        folds.append((coord, val))
    db(folds)

    return solve(grid, folds)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,13, p1, p2, cmds)
if stats: print_stats()
#manual()
