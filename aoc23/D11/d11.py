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

def hasgal(row):
    return '#' in row

def hasgal2(grid, c):
    for row in grid:
        if row[c] != '.':
            return True
    return False


def getrows(grid):
    empty = set()
    for i, row in enumerate(grid):
        if not hasgal(row):
            empty.add(i)
    return empty


def getcols(grid):
    empty = set()
    C = len(grid[0])
    for c in range(C):
        if not hasgal2(grid, c):
            empty.add(c)
    return empty

def offscols(a, b, cols):
    start = min(a[1], b[1])
    end = max(a[1], b[1])
    d = end- start
    for c in range(start, end + 1):
        if c in cols:
            d += 1000000-1
    return d

def offsrows(a, b, rows):
    start = min(a[0], b[0])
    end = max(a[0], b[0])
    d = end- start
    for c in range(start, end + 1):
        if c in rows:
            d += 1000000-1
    return d


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    grid = togrid(lines)
   
    rows = getrows(grid)
    cols = getcols(grid)
    gals = []
    db(rows)
    db(cols)
    
    su = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                gals.append((r, c))
    for i in range(len(gals)):
        for k in range(i+1, len(gals)):
            d = offscols(gals[i], gals[k], cols)
            db('dist cols', d)
            d2 = offsrows(gals[i], gals[k], rows)
            d += d2
            db('dist rows', d2)
            db('from ', gals[i], 'to', gals[k], 'd', d)
            su += d
        

    return su

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,11, p1, p2, cmds)
if stats: print_stats()

#manual()
