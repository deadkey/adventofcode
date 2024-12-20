import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
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
  


def close(node, paths):
    ok = []
    for p in paths:
        dr = abs(node[0] - p[0])
        dc = abs(node[1] - p[1])
        if dr + dc <= 20:
            ok.append((p, dr+dc))
    return ok


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    su = 0
    start = gridfind(grid, 'S')
    end = gridfind(grid, 'E')
    grid[start[0]][start[1]] = '.'
    grid[end[0]][end[1]] = '.'
    walls = gridfindall(grid, '#')
    paths = gridfindall(grid, '.')
    
    diststart = gridbfs([start], grid)
    distend = gridbfs([end], grid)
    tot = gridbfs([start], grid, end)
    cnt = Counter()

    for i in range(len(paths)):
        points = close(paths[i], paths)
        for p, d in points:
            newtot = diststart[paths[i]] + distend[p] + d
            saved = tot - newtot
            cnt[saved] += 1
    
    limit = 100
    
    for k, v in sorted(cnt.items()):
        if k >= limit:
            su += v


    return su

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    su = 0
    start = gridfind(grid, 'S')
    end = gridfind(grid, 'E')
    walls = gridfindall(grid, '#')
    #walls = [goofwall(w, grid) for w in walls]
    tot = gridbfs([start], grid, target = end)
    cnt = Counter()
    for i, w in enumerate(walls):
        grid[w[0]][w[1]] = '.'
        newtot = gridbfs([start], grid, end)
        cnt[tot - newtot]+=1
        grid[w[0]][w[1]] = '#'
        db(f'{i}/{len(walls)}')
    
    limit = 100
    
    for k, v in cnt.items():
        if k >= limit:
            su += v

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,20, p1, p2, cmds)
if stats: print_stats()

#manual()
