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
    return lazy_ints(list(line.split()[0]))

def sim(grid):
    flash = set()
    changed = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1
            if grid[r][c] == 10:
                changed.append((r, c))
                flash.add((r, c))

   
    while changed:
        nxt = []
        for r, c in changed:
            nb = grid8nb(r, c, grid)
            for nr, nc in nb:
                grid[nr][nc] += 1
                if grid[nr][nc] >= 10 and (nr, nc) not in flash:
                    nxt.append((nr, nc))
                    flash.add((nr, nc))

        changed = nxt

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] >= 10:
                grid[r][c] = 0

    
    return len(flash)




def p1(v):
    N = 100
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    
    for i in range(N):
        su += sim(data)
    return su

def p2(v):
    N = 1000
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    
    for i in range(N):
        res = sim(data)
        su += res
        if res == 100:
            return i+1
    return -1


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,11, p1, p2, cmds)
if stats: print_stats()
#manual()
