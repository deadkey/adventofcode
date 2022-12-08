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
    return line
    #return lazy_ints(line.split())
    #return lazy_ints(multisplit(line, ' ')) 

def visible(r, c, grid):
    t = grid[r][c]
    ok = True
    for rr in range(0, r):
        if grid[rr][c] >= t:
            
            ok = False
    if ok: return True
    ok = True
    for rr in range(r+1, len(grid)):
        if grid[rr][c]>= t:
            ok = False

    if ok: return True
    ok = True
    for cc in range(0, c):
        if grid[r][cc] >= t:
            ok = False
        
    if ok: return True
    ok = True
    for cc in range(c+1, len(grid[0])):
        if grid[r][cc] >=  t:

            ok = False
    if ok: return True
    
    
    return False


def visible2(r, c, grid):
    t = grid[r][c]
    ok = True
    score = 1
    steps = 0
    for rr in range(r-1, -1, -1):
        steps += 1
        if grid[rr][c] >= t:
            
            ok = False
            break
    
    score *= steps


    steps = 0
    for rr in range(r+1, len(grid)):
        steps += 1
        if grid[rr][c]>= t:
           
            break
    score *= steps

    steps = 0
    for cc in range(c-1, -1, -1):
        steps += 1
        if grid[r][cc] >= t:
            
            break
    score *= steps
    steps = 0
    for cc in range(c+1, len(grid[0])):
        steps += 1
        if grid[r][cc] >=  t:
            
            break
    score *= steps
    
    return score


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = []
    for i in range(len(data)):
        d = data[i]
        grid.append(d)
    
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if visible(r, c, grid):
                db('vis', r, c, grid[r][c])
                su += 1


    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = []
    for i in range(len(data)):
        d = data[i]
        grid.append(d)
    
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            score =  visible2(r, c, grid)
            su = max(score, su)


    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,8, p1, p2, cmds)
if stats: print_stats()

#manual()
