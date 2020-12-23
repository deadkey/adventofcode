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

def flip(grid):
    newgrid = []
    for row in grid:
        newgrid.append(row[::-1])
    return newgrid

def rot(grid):
    newgrid = []
    L = len(grid)
    for c in range(L):
        row = []
        for r in range(L-1, -1, -1):
            row.append(grid[r][c])
        newgrid.append(row)
    return newgrid

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())
    

def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    data = 
    for r in range(L):
[parse(line) for line in lines]
    return cnt

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2017,21, p1, p2, cmds)
if stats: print_stats()
#manual()
