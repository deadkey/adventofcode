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
    #return lazy_ints(line.split())
    line = line.replace('->', ' ')
    return lazy_ints(multisplit(line, ' ,')) 

def sign(d):
    if d == 0: return 0
    return d//abs(d)


def move(paths):
    grid = dd(int)
    for path in paths:
        px, py = path[0]
        grid[px, py] = 1
        for x, y in path[1:]:
            dx = sign(x - px)
            dy = sign(y - py)
            cx, cy = px, py
            while (cx, cy) != (x, y):
                cx += dx
                cy += dy
                grid[cx, cy] = 1
            px, py = cx, cy
    return grid

def fall(grid, limit):
    x, y = 500, 0
    while y <= limit:
        if grid[x, y+1] == 0:
            y +=1
        elif grid[x-1, y+1] == 0:
            x -= 1
            y += 1
        elif grid[x + 1, y+1] == 0:
            x += 1
            y += 1
        else:
            return True, x, y
    return False, 0, 0


def simulate(grid, limit):
    cnt = 0
    ok, x, y = fall(grid, limit)
    while ok:
        grid[x, y] = 1
        cnt += 1
        
        ok, x, y = fall(grid, limit)
    return cnt

    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    allpaths = []
    limit = 0
    
    for i in range(len(data)):
        path = []
        for x in range(0, len(data[i]), 2):
            path.append((data[i][x], data[i][x+1]))
            limit = max(limit, data[i][x+1])
        allpaths.append(path)

    grid = move(allpaths)
    db(grid)
    grid[500, 0] = 2
    cnt = simulate(grid, limit)
    

    return cnt

##############################################################################

def fall2(grid, limit):
    x, y = 500, 0
    while y <= limit:
        if grid[x, y+1] == 0:
            y +=1
        elif grid[x-1, y+1] == 0:
            x -= 1
            y += 1
        elif grid[x + 1, y+1] == 0:
            x += 1
            y += 1
        else:
            return True, x, y
    return True, x, y


def simulate2(grid, limit):
    cnt = 0

    for x in range(-1000, 1000):
        grid[x, limit] = 1
    ok, x, y = fall2(grid, limit)
    while (x, y) != (500, 0):
        grid[x, y] = 1
        cnt += 1
        
        ok, x, y = fall2(grid, limit)
    cnt += 1
    return cnt

    

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    allpaths = []
    limit = 0
    
    for i in range(len(data)):
        path = []
        for x in range(0, len(data[i]), 2):
            path.append((data[i][x], data[i][x+1]))
            limit = max(limit, data[i][x+1])
        allpaths.append(path)
    limit += 2
    db('limit', limit)
    grid = move(allpaths)
    
    grid[500, 0] = 0
    cnt = simulate2(grid, limit)
    

    return cnt




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,14, p1, p2, cmds)
if stats: print_stats()

#manual()
