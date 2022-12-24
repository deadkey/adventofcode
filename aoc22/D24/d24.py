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
    return lazy_ints(multisplit(line, ' ')) 

def addonrow(occ, row, startcol, dc, k):
    startcol -= 1
    for i in range(k):
        index = (startcol + dc * i) % k
        index += 1
        occ[row, index].append((i, k))

def addoncol(occ, startrow, col, dr, k):
    startrow -= 1
    for i in range(k):
        index = (startrow + dr * i) % k
        index += 1
        occ[index, col].append((i, k))

def alt(node, grid):
    r, c = node
    li = get4nb(r, c, 0, len(grid), 0, len(grid[0]))
    li.append((r, c))
    return li

def ok(node, time, occ, grid):
    r, c, = node
    if grid[r][c] == '#': return False
    blizz = occ[r, c]
    for start, k in blizz:
        if time % k == start: return False
    return True

def bfs(grid, occ, start, target, time = 0):
    q = [(start, time)]
    visited = set()
    for node in q:
        visited.add(node)
    
    while q:
        q2 = []
        for node,t in q:
            if node == target: return t
            for ne in alt(node, grid):
                if ok(ne, t+1, occ, grid):
                    if (ne, t+1) not in visited:
                        visited.add((ne, t + 1))
                        q2.append((ne, t+1))
        q = q2
    return visited

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = []
    for i in range(len(data)):
        d = data[i]
        grid.append(d)
    
    start = 0, data[0].index('.')
    target = len(grid) -1, data[-1].index('.')
    blizz = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            ch = grid[r][c]
            if ch == '>':
                blizz.append((r, c, 0))
            if ch == 'v':
                blizz.append((r, c, 1))
            if ch == '<':
                blizz.append((r, c, 2))
            if ch == '^':
                blizz.append((r, c, 3))
    
    Rk = len(grid) - 2
    Ck = len(grid[0]) - 2
    occ = dd(list)
    for b in blizz:
        r, c, dir = b
        if dir == 0:
            addonrow(occ, r, c, 1, Ck)
        if dir == 2:
            addonrow(occ, r, c, -1, Ck)
        if dir == 3:
            addoncol(occ, r, c, -1, Rk)
        if dir == 1:
            addoncol(occ, r, c, 1, Rk)
    t1 = bfs(grid, occ, start, target, 0)
    t2 = bfs(grid, occ, target, start, t1)
    t3 = bfs(grid, occ, start, target, t2)
    return t3
    
      
def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = []
    for i in range(len(data)):
        d = data[i]
        grid.append(d)
    
    start = 0, data[0].index('.')
    target = len(grid) -1, data[-1].index('.')
    blizz = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            ch = grid[r][c]
            if ch == '>':
                blizz.append((r, c, 0))
            if ch == 'v':
                blizz.append((r, c, 1))
            if ch == '<':
                blizz.append((r, c, 2))
            if ch == '^':
                blizz.append((r, c, 3))
    
    Rk = len(grid) - 2
    Ck = len(grid[0]) - 2
    occ = dd(list)
    for b in blizz:
        r, c, dir = b
        if dir == 0:
            addonrow(occ, r, c, 1, Ck)
        if dir == 2:
            addonrow(occ, r, c, -1, Ck)
        if dir == 3:
            addoncol(occ, r, c, -1, Rk)
        if dir == 1:
            addoncol(occ, r, c, 1, Rk)
    return bfs(grid, occ, start, target)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,24, p1, p2, cmds)
if stats: print_stats()

#manual()
