import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
from collections import defaultdict as dd, Counter
from itertools import chain, combinations, permutations
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))

#Run with command p3 setup.py 
# to setup everything
# then cd to day folder
#Run with command p3 d30.py p1 submit stat
# io = input only
# so = sample only

import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

#crazy input, use multisplit? 
def parse(line):
    return lazy_ints(multisplit(line, ' ')) 
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    R, C = len(grid), len(grid[0])
    r, c = gridfind(grid, 'S')
    beams = [(r, c)]
    su = 0
    for row in range(R-1):
        newbeams = set()
        for r, c in beams:
            if grid[r+1][c] == '.':
                newbeams.add((r+1, c))
            elif grid[r+1][c] == '^':
                su += 1
                if c -1 >= 0: newbeams.add((r+1, c-1))
                if c +1 < C: newbeams.add((r+1, c+1))
        beams = newbeams
        
    
    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    R, C = len(grid), len(grid[0])
    r, c = gridfind(grid, 'S')
    beams = [(r, c)]
    su = 0
    ways = dd(int)
    ways[(r, c)] = 1

    for row in range(R-1):
        newbeams = set()
        for r, c in beams:
            if grid[r+1][c] == '.':
                newbeams.add((r+1, c))
                ways[(r+1, c)] += ways[(r, c)]
            elif grid[r+1][c] == '^':
                su += 1
                if c -1 >= 0: 
                    newbeams.add((r+1, c-1))
                    ways[(r+1, c-1)] += ways[(r, c)]
                if c +1 < C: 
                    newbeams.add((r+1, c+1))
                    ways[(r+1, c+1)] += ways[(r, c)]
        beams = newbeams
    su = 0
    for c in range(C):
        su += ways[(R-1, c)]
    return su

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,7, p1, p2, cmds)
if stats: print_stats()

#manual()
