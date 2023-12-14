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

def sameC(grid, c1, c2):
    col1 = []
    col2 = []
    R = len(grid)
    for r in range(R):
        col1.append(grid[r][c1])
        col2.append(grid[r][c2])
        #if grid[r][c1] != grid[r][c2]:
        #    return False
    #return True
    #db('testing', col1, col2)
    cc = 0
    for a, b in zip(col1, col2):
        if a != b:
            cc += 1
    return cc


def sameR(grid, r1, r2):
    row1 = grid[r1]
    row2 = grid[r2]

    cc = 0
    for a, b in zip(row1, row2):
        if a != b:
            cc += 1
    return cc

def midC(grid, mid):

    R = len(grid)
    C = len(grid[0])
    L = min(mid+1, C-mid-1)
    diffs = 0

    for d in range(L):
        res = sameC(grid, mid-d, mid + d+1)
        diffs += res
        if diffs >=2:
            return False
    
    return diffs == 1


def midR(grid, mid):

    R = len(grid)
    L = min(mid+1, R-mid -1)
    diffs = 0
    for d in range(L):
        res= sameR(grid, mid-d, mid + d+1)
        diffs += res
        if diffs >=2:
            return False
        
    return diffs == 1

def cnt(grid):
    R = len(grid)
    C = len(grid[0])
    for c in range(C-1):
        if midC(grid, c):
            return c + 1
    
    for r in range(R-1):
        if midR(grid, r):
            return 100 * (r + 1)
    assert False
    



def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    su = 0
    for ch in chunks:
        grid = togrid(ch)
        db(cnt(grid))
        su += cnt(grid)

    return su

###################################
# Part 1

def sameC1(grid, c1, c2):
    col1 = []
    col2 = []
    R = len(grid)
    for r in range(R):
        col1.append(grid[r][c1])
        col2.append(grid[r][c2])
        #if grid[r][c1] != grid[r][c2]:
        #    return False
    #return True
    #db('testing', col1, col2)
    return col1 == col2


def sameR1(grid, r1, r2):
    row1 = grid[r1]
    row2 = grid[r2]
    return row1 == row2

def midC1(grid, mid):

    R = len(grid)
    C = len(grid[0])
    L = min(mid+1, C-mid-1)
    
    for d in range(L):
        if not sameC1(grid, mid-d, mid + d+1):
            return False
    return True


def midR1(grid, mid):

    R = len(grid)
    L = min(mid+1, R-mid -1)
    for d in range(L):
        if not sameR1(grid, mid-d, mid + d+1):
            return False
    return True

def cnt1(grid):
    R = len(grid)
    C = len(grid[0])
    for c in range(C-1):
        if midC1(grid, c):
            return c + 1
    
    for r in range(R-1):
        if midR1(grid, r):
            return 100 * (r + 1)
    assert False
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    su = 0
    for ch in chunks:
        grid = togrid(ch)
        db(cnt1(grid))
        su += cnt1(grid)

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,13, p1, p2, cmds)
if stats: print_stats()

#manual()
