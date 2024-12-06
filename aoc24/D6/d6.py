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

def turn(dir):
    if dir == (-1, 0): return (0, 1)
    if dir == (0, 1): return (1, 0)
    if dir == (1, 0): return (0, -1)
    if dir == (0, -1): return (-1, 0)
    return None

def printgrid(grid, vis):
    grid = copygrid(grid)
    for r, c in vis:
       grid[r][c] = 'X' 
    for r in range(len(grid)):
        out = ''.join(map(str, grid[r]))
        print(out)

def walk1(grid, start):
    R = len(grid)
    C = len(grid[0])
    vis = set()
    dir = (-1, 0)
    r, c = start
    grid[r][c] = '.'

    while 0 <= r < R and 0 <= c < C:
        vis.add((r, c))
        dr, dc = dir
        nxtrr, nxtc = r + dr, c + dc
        if not (0 <= nxtrr < R and 0 <= nxtc < C): 
            printgrid(grid, vis)
            return len(vis)
        if grid[nxtrr][nxtc] == '.':
            r += dr
            c += dc
        else:
            dir = turn(dir)
    return None


def walk(grid, start):
    R = len(grid)
    C = len(grid[0])
    vis = set()
    dir = (-1, 0)
    r, c = start
    grid[r][c] = '.'

    while 0 <= r < R and 0 <= c < C:
        dr, dc = dir
        
        if (r, c, dr, dc) in vis: 
            return True
        
        vis.add((r, c, dr, dc))
        nxtrr, nxtc = r + dr, c + dc
        if not (0 <= nxtrr < R and 0 <= nxtc < C): 
            #printgrid(grid, vis)
            return False
        if grid[nxtrr][nxtc] == '.':
            r += dr
            c += dc
        else:
            dir = turn(dir)
    return False


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    start = (0, 0)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                start = (r, c)
                break
    obs = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.':
                obs.add((r, c))
                
    su = 0
    for a, b in obs:
        grid[a][b] = '#'
        if walk(grid, start):
            su += 1
        grid[a][b] = '.'
    
    return su

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    start = (0, 0)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                start = (r, c)
                break
    su = walk1(grid, start)

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,6, p1, p2, cmds)
if stats: print_stats()

#manual()
