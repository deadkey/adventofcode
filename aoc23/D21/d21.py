import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict as dd, Counter
import numpy as np
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

def get4nb(r, c, rmin = -INF, rmax = INF, cmin = -INF, cmax = INF):
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nb = []
    for dr, dc in diff:
        nb.append((r+dr, c + dc))
    return nb 

def nei(loc, grid):
    r, c = loc
    R = len(grid)
    C = len(grid[0])
    alt = get4nb(r, c, rmin = 0, rmax = R, cmin = 0, cmax = C)
    alt2 = []
    for rr, cc in alt:
        if grid[rr % R][cc % C] != '#':
            alt2.append((rr, cc))
    return alt2

def bfs(q, g, N):
    q = set(q)
    #visited = dd(set)
    steps = 0
    
    

    while q and steps < N:
        q2 = set()
        steps += 1
        for node in q:
            for ne in nei(node, g):
                #if ne not in visited:
                #visited[ne].add(steps%2)
                
                q2.add(ne)
        q = q2

    '''
    even = 0
    odd = 0
    both = 0
    for node, li in visited.items():
        if len(li) == 2:
            both += 1
        elif 0 in li:
            even += 1
        elif 1 in li:
            odd += 1
    db('both', both)
    db('even', even)
    db('odd', odd)
    db('tot', both + even + odd)
    '''

    return len(q2)

def addrow(grid1, grid2):
    for row in grid2:
        grid1.append(row)

       

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = togrid(lines)
    S = 0, 0
    R = len(grid)
    C = len(grid[0])
    rocks = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                S = r, c

    N = 26501365
    offs = []

    x0 = 65 + 2 * 131
    x1 = 65 + 3 * 131
    x2 = 65 + 4 * 131 
    '''
    x0 steps 97459
x1 steps 190865
x2 steps 315371
    '''
    f0 = 97459#bfs([S], grid, x0)
    db('x0 steps', f0)
    

    f1 = 190865#bfs([S], grid, x1)
    db('x1 steps', f1)
    f2 = 315371#bfs([S], grid, x2)
    db('x2 steps', f2)
    
    poly = np.polyfit([x0, x1, x2], [f0, f1, f2], 2)
    db(poly)
    a, b, c = poly
    a = round(a)
    b = round(b)
    c = round(c)
    #test
    def ff(x):
        return x **2 * a + x * b + c
    
    g0 = ff(x0)
    g1 = ff(x1)
    g2 = ff(x2)
    db('g0', g0)
    db('g1', g1)
    db('g2', g2)

    #598044246091825.9
    598044246091826
    return ff(N) #len(vis)

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

if not so: run(2023,21, p1, p2, cmds)
if stats: print_stats()

#manual()
