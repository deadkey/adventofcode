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
# Up, right, down, left
MAP = {'|': (1, 0, 1, 0),'-': (0, 1, 0, 1), 'L': (1, 1, 0, 0), 'J' : (1, 0, 0, 1), '7' : (0, 0, 1, 1), 'F' : (0, 1, 1, 0), '.': (0, 0, 0, 0)} 

def replacefirst(grid, start):
    r, c =start
    right = MAP[grid[r][c+1]]
    up = MAP[grid[r-1][c]]
    down = MAP[grid[r+1][c]]
    left = MAP[grid[r][c-1]]
    dir = [0, 0, 0, 0]
    if up[2] == 1:
        dir[0] = 1
    if left[1] == 1:
        dir[-1] = 1
    if down[0] == 1:
        dir[2] = 1
    if right[-1] == 1:
        dir[1] = 1
    for letter, dd in MAP.items():
        if tuple(dir) == dd:
            grid[r][c] = letter
            return grid
    assert False

def D(i, r, c):
    li = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    delta =  li[i]
    
    return r + delta[0], c + delta[1]



def nei(node, g):
    r = len(g)
    c = len(g[0])
    letter = g[node[0]][node[1]]
    dir = MAP[letter]
    cand = []
    
    for i in range(4):
        if dir[i] == 1:
            cc = D(i, node[0], node[1])
          
            if cc[0]  < r and cc[1] < c:
                cand.append(cc)
    
    return cand

def bfs(q, g, part = 1):
    visited = set()
    dist = {}
    for node in q:
        visited.add(node)
        dist[node] = 0

    path = [node]
    
    while q:
        q2 = []
        for node in q:
            s = 0
            for ne in nei(node, g):
                if ne not in visited and s == 0:
                    visited.add(ne)
                    dist[ne] = dist[node] + 1
                    path.append(ne)
                    q2.append(ne)
                    if part == 2: s += 1
       
        q = q2
    
    return dist, path

        
## 1030 too high
## 394 too low
def polygonArea(P):
    n = len(P)
    X = [x for x, _ in P]
    Y  = [y for _, y in P]
    area = 0.0
 
    # Calculate value of shoelace formula
    j = n - 1
    for i in range(0,n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i   # j is previous vertex to i
     
    return abs(area / 2.0)

def picks(P):
    area = polygonArea(P)
    return int(area - len(P)/2 + 1)

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    start = 0, 0
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                start = r, c
    grid = replacefirst(grid, start)    
    _, path = bfs([start], grid, part = 2)

    return picks(path)

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    start = 0, 0
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                start = r, c
    grid = replacefirst(grid, start)    
    dist, _ = bfs([start], grid)
    
    mx = 0
    for r in range(R):
        for c in range(C):
            if (r, c) in dist:
                mx = max(mx, dist[r, c])

    return mx


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,10, p1, p2, cmds)
if stats: print_stats()

#manual()
