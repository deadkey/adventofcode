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

def north(grid):
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                #tilt
                moveto = r
                for u in range(r-1, -1, -1):
                    if grid[u][c] == '.':
                        moveto = u
                    else:
                        break
                grid[r][c] = '.'
                grid[moveto][c] = 'O'
  
    su = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                su += R - r
    return su

def south(grid):
    R = len(grid)
    C = len(grid[0])
    for r in range(R-1, -1, -1):
        for c in range(C):
            if grid[r][c] == 'O':
                #tilt
                moveto = r
                for u in range(r+1, R):
                    if grid[u][c] == '.':
                        moveto = u
                    else:
                        break
                grid[r][c] = '.'
                grid[moveto][c] = 'O'
    
    su = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                su += R - r
    return su

def left(grid):
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                #tilt
                moveto = c
                for u in range(c-1, -1, -1):
                    if grid[r][u] == '.':
                        moveto = u
                    else:
                        break
                grid[r][c] = '.'
                grid[r][moveto] = 'O'
   
    su = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                su += R - r
    return su

def right(grid):
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        for c in range(C-1, -1, -1):
            if grid[r][c] == 'O':
                #tilt
                moveto = c
                for u in range(c+1,C):
                    if grid[r][u] == '.':
                        moveto = u
                    else:
                        break
                grid[r][c] = '.'
                grid[r][moveto] = 'O'
   
    su = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                su += R - r
    return su

# NOT 96293

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    grid = togrid(lines)
    #tilt
    R = len(grid)
    C = len(grid[0])
    results = []
    N = 1000
    M = 9
    mod = {}
    for cycle in range(N):
        north(grid)
        left(grid)
        south(grid)
        res = right(grid)
        #db('Cycle ', cycle)
        #printgrid(grid)
        m = cycle % M
        mod[m] = res
        results.append(str(res))
    
    db(mod)
    #db(results[-100:])
    m = (1000000000-1) % M
    

    return mod[m]

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    grid = togrid(lines)
    #tilt
    
    return north(grid)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,14, p1, p2, cmds)
if stats: print_stats()

#manual()
