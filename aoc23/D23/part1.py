import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
sys.setrecursionlimit(100000)
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

def dfs(s, t, g, vis):
    if s == t: return 0
    vis.add(s)
    R = len(g)
    C = len(g[0])
    r, c = s
    alt = []
    if g[r][c] == '.':
        ne = get4nb(r, c, 0, R, 0, C)
        
        for rr, cc in ne:
            if g[rr][cc] != '#':
                alt.append((rr, cc))
    
    elif g[r][c] == '>':
        alt.append((r, c+1))
    elif g[r][c] == '<':
        alt.append((r, c-1))
    elif g[r][c] == 'v':
        alt.append((r+1, c))
    elif g[r][c] == '^':
        alt.append((r-1, c))
    
    alt2 = [(rr, cc) for (rr, cc) in alt if (rr, cc) not in vis]
    alt = alt2
    
    mx = 0
    for n in alt:
        a = dfs(n, t, g, vis)
        mx = max(mx, a)
        if n in vis: vis.remove(n)
    if s in vis: vis.remove(s)
    return mx +1



def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = togrid(lines)
    S = 0, 0
    T = 0, 0
    R = len(grid)
    C = len(grid[0])
    for c in range(C):
        if grid[0][c] == '.':
            S = 0, c
        if grid[R-1][c] == '.':
            T = 0, c

    longest = dfs(S, T, grid, set()) -1


    return longest

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

if not so: run(2023,23, p1, p2, cmds)
if stats: print_stats()

#manual()
