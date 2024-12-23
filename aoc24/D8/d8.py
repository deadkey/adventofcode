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


def checkpair1(p1, p2, grid):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    q = p2[0] + dx, p2[1] + dy
    if (0 <= q[0] < len(grid) and 0 <= q[1] < len(grid[0])):
        return q
    return None

def cnt1(a, grid, freq):
    li = freq[a]
    s = set()
    
    for i in range(len(li)):
        for k in range(i + 1, len(li)):
            q = checkpair1(li[i], li[k], grid)
            if q:
                s.add(q)
            q= checkpair1(li[k], li[i], grid)
            if q:
                s.add(q)
    
    return s



def checkpair(p1, p2, grid):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    li = []
    for i in range(0, 100):
        q = p2[0] + i * dx, p2[1] + i * dy
        if (0 <= q[0] < len(grid) and 0 <= q[1] < len(grid[0])):
            li.append(q)
        else:
            break
    return set(li)

def cnt(a, grid, freq):
    li = freq[a]
    s = set()
    
    for i in range(len(li)):
        for k in range(i + 1, len(li)):
            q = checkpair(li[i], li[k], grid)
            if q:
                s |= q
            q= checkpair(li[k], li[i], grid)
            if q:
                s |=q
    
    return s

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    alt = set()
    su = 0
    freq = dd(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]!= '.':
                freq[grid[r][c]].append((r, c))
                alt.add(grid[r][c])
    
    ss = set()

    for a in alt:
        
        ss |=  cnt(a, grid, freq)

    
    return len(ss)

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    alt = set()
    su = 0
    freq = dd(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]!= '.':
                freq[grid[r][c]].append((r, c))
                alt.add(grid[r][c])
    
    ss = set()

    for a in alt:
        
        ss |=  cnt1(a, grid, freq)


    return len(ss)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,8, p1, p2, cmds)
if stats: print_stats()

#manual()
