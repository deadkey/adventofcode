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

def tolocks(lock):
    res = []
    for c in range(len(lock[0])):
        cnt = 0
        for r in range(len(lock)):
            if lock[r][c] == '.':
                res.append(cnt-1)
                break
            cnt += 1
    db('lock', res)
    return tuple(res)

def tokeys(key):
    res = []
    for c in range(len(key[0])):
        cnt = 0
        for r in range(len(key)-1, -1, -1):
            if key[r][c] == '.':
                res.append(cnt-1)
                break
            cnt += 1
    db('key', res)
    return tuple(res)      
                
def fit(lock, key):
    for l, k in zip(lock, key):
        if l + k > 5:
            return False
    return True

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    keys = []
    locks = []
    for ch in chunks:
        grid = togrid(ch)
        if grid[0] == ['#'] *len(grid[0]) and grid[-1] == ['.'] * len(grid[0]):
            locks.append(grid)
        
        if grid[0] == ['.'] *len(grid[0]) and grid[-1] == ['#'] * len(grid[0]):
            keys.append(grid)

    locks = set([tolocks(lock) for lock in locks])
    keys = set([tokeys(key) for key in keys])


    
    su = 0

    for lock in locks:
        for key in keys:
            
            if fit(lock, key):
                su += 1

    #    su += 0

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

if not so: run(2024,25, p1, p2, cmds)
if stats: print_stats()

#manual()
