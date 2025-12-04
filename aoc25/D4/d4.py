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
    su = 0
    matches = []

    ne = get8nb(0, 2, rmin = 0, rmax = R, cmin = 0, cmax = C)
    
    for r in range(R):
        for c in range(C):
            cnt = 0
            ne = get8nb(r, c, rmin = 0, rmax = R, cmin = 0, cmax = C)
            for nr, nc in ne:
                if grid[nr][nc] == '@':
                    cnt += 1
            if cnt < 4 and grid[r][c] == '@': 
                su += 1
                matches.append((r, c))

    for mr, mc in matches:
        grid[mr][mc] = 'X'
    #printgrid(grid)  

    return su

def toremove(grid):
    R, C = len(grid), len(grid[0])
    
    matches = []

    for r in range(R):
        for c in range(C):
            cnt = 0
            ne = get8nb(r, c, rmin = 0, rmax = R, cmin = 0, cmax = C)
            for nr, nc in ne:
                if grid[nr][nc] == '@':
                    cnt += 1
            if cnt < 4 and grid[r][c] == '@': 
                matches.append((r, c))
    return matches

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    R, C = len(grid), len(grid[0])
    su = 0
    matches = []
    running = True
    while running:
        matches = toremove(grid)
        for mr, mc in matches:
            grid[mr][mc] = '.'
            su += 1
        running = len(matches) > 0

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,4, p1, p2, cmds)
if stats: print_stats()

#manual()
