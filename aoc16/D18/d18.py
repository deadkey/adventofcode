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

def addrow(grid):
    C = len(grid[-1])
    
    nxt = ['.'] * len(grid[-1])
    nxt[0] = 'x'
    nxt[-1] = 'x'
    for i in range(1, C -1):
        left = grid[-1][i-1] == '^'
        center = grid[-1][i] == '^'
        right = grid[-1][i+1] == '^'
        if not left and (center and right):
            nxt[i] = '^'
        if not right and (center and left):
            nxt[i] = '^'
        if not right and not center and left:
            nxt[i] = '^'
        if not left and not center and right:
            nxt[i] = '^'
    grid.append(nxt)
        

def p1(v):
    lines = v.strip().split('\n')
    grid = [['x'] + list(lines[0]) +['x']]
    db(grid)
    for r in range(40 -1):
        addrow(grid)
    #db('#######')
    cnt = cntgrid(grid, '.')
    #printgrid(grid)
    return cnt

def p2(v):
    lines = v.strip().split('\n')
    grid = [['x'] + list(lines[0]) +['x']]
    db(grid)
    for r in range(400000 -1):
        addrow(grid)
        db(r)
    #db('#######')
    cnt = cntgrid(grid, '.')
    #printgrid(grid)
    return cnt


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,18, p1, p2, cmds)
if stats: print_stats()
#manual()
