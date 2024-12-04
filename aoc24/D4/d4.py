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

def search(grid, x, y, dx, dy):
    c = 0
    if grid[x][y] != 'X': return c
    nxt = 'MAS'
    for step in range(3):
        x += dx
        y += dy
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return c
        if grid[x][y] != nxt[step]:
            return c
    
    return 1

def ismid(grid, x, y):
    if grid[x][y] != 'A': return 0
    s1 = set()
    s2 = set()
    ms = set(['M', 'S'])
    if 0 < x < len(grid) - 1 and 0 < y < len(grid[0]) - 1: 
        s1.add(grid[x-1][y-1])
        s1.add(grid[x+1][y+1])
        s2.add(grid[x-1][y+1])
        s2.add(grid[x+1][y-1])
        if s1 == ms and s2 == ms:
            return 1
    return 0

    


def checkall(grid, x, y):
    c = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0: continue
            c += search(grid, x, y, dx, dy)
   
    return c


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    
    data = [parse(line) for line in lines]
    su = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            cnt=checkall(grid, r, c)
            su += cnt
    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    
    data = [parse(line) for line in lines]
    su = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            cnt=ismid(grid, r, c)
            su += cnt
    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,4, p1, p2, cmds)
if stats: print_stats()

#manual()
