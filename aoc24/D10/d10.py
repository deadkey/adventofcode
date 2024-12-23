import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
from collections import defaultdict as dd, Counter
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



def walk1(r, c, grid):
    q = [(r, c)]
    seen = set(q)
    cnt = 0
    for r, c in q:
        db(r, c, grid[r][c], cnt)
        for nr, nc in get4nb(r, c, rmin = 0, rmax = len(grid), cmin = 0, cmax = len(grid[0])):
            if grid[nr][nc] == grid[r][c] + 1 and not (nr, nc) in seen:
                q.append((nr, nc))
                seen.add((nr, nc))
        if grid[r][c] == 9:
            cnt += 1

    return cnt

def walk(r, c, grid):
    q = [(r, c)]
    seen = Counter()
    seen[(r, c)] = 1
    cnt = 0

    for r, c in q:
        db(r, c, grid[r][c], cnt)
        currseen = seen[(r, c)]
        for nr, nc in get4nb(r, c, rmin = 0, rmax = len(grid), cmin = 0, cmax = len(grid[0])):
            if grid[nr][nc] == grid[r][c] + 1:
                if (nr, nc) in seen:
                    seen[(nr, nc)] += currseen
                else:
                    seen[(nr, nc)] = currseen
                    q.append((nr, nc))
                    
        if grid[r][c] == 9:
            cnt += currseen

    return cnt


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togoneintrid(lines)
    
    start = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                start.append((r, c))
    su = 0  
    for r, c in start:
        su += walk1(r, c, grid)
   
    
    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togoneintrid(lines)
    
    start = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                start.append((r, c))
    su = 0  
    for r, c in start:
        su += walk(r, c, grid)
   
    
    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,10, p1, p2, cmds)
if stats: print_stats()

#manual()
