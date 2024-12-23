import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
from collections import defaultdict as defdict, Counter
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


import heapq

def turn(dir):
    cw = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ccw = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    turns = []
    for i in range(4):
        if cw[i] == dir:
            t1 = cw[(i + 1) % 4]
            turns.append(t1)
        if ccw[i] == dir:
            t2 = ccw[(i + 1) % 4]
            turns.append(t2)
    return turns[0], turns[1]


def ne(grid, node, dir):
    r, c = node
    dr, dc = dir
    out = []
    nr, nc = r + dr, c + dc
    if grid[nr][nc] != '#' and 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        out.append((1, (nr, nc), dir))
    turn1, turn2 = turn(dir)
    out.append((1000, (r, c), turn1))
    out.append((1000, (r, c), turn2))
    return out

def dij(grid, start, end, startall = False):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    INF = 10**12
    dist = defdict(lambda: INF)

    pq = []
    if startall:
        for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dist[start, dir] = 0
            pq.append((0, start, dir))
    else:
        dist[start,  (0, 1)] = 0
        pq.append((0, start, (0, 1)))
    heapq.heapify(pq)
    path = defdict(int)
    done = False
    while pq and not done:
        (nd, node, dir) = heapq.heappop(pq)
        if node == end: return dist, nd
        for (dd, nn, ndir) in ne(grid, node, dir):
            alt = dist[node, dir] + dd
            if dist[nn, ndir] > alt:
                dist[nn, ndir] = alt
                path[nn] = node
                heapq.heappush(pq, (dist[nn, ndir], nn, ndir))

    return -1

def getpath(path, end):
    out = []
    node = end
    while node:
        out.append(node)
        node = path[node]
    return list(out[::-1])

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    grid = togrid(lines)
    start = gridfind(grid, 'S')
    end = gridfind(grid, 'E')


    grid[start[0]][start[1]] = '.'
    grid[end[0]][end[1]] = '.'
    dist, tot = dij(grid, start, end)
 
        
    dist2, _ = dij(grid, end, start, startall = True)
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            cw = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for i, dir in enumerate(cw): 
                if dist[(r, c), dir] + dist2[(r, c), cw[(i + 2)%4]] == tot:
                    visited.add((r, c))

    return len(visited)

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    grid = togrid(lines)
    start = gridfind(grid, 'S')
    end = gridfind(grid, 'E')

    grid[start[0]][start[1]] = '.'
    grid[end[0]][end[1]] = '.'
    _, nd = dij(grid, start, end)


    return nd


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,16, p1, p2, cmds)
if stats: print_stats()

#manual()
