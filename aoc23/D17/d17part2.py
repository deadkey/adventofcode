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
    return list(map(int, list(line)))


import heapq



def gen(node, grid):
    R = len(grid)
    C = len(grid[0])
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c, dir, cnt = node
    alt = []
    orr, orc = deltas[dir]
    if cnt < 3:
        dr, dc = deltas[dir]
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C:
            d2 = grid[nr][nc]
            alt.append((d2, (nr, nc, dir, cnt +1)))
        return alt

    for d in range(4):
        if cnt == 9 and d == dir:
            continue
        
        dr, dc = deltas[d]
        
        if (dr, dc) == (-orr, -orc): continue

        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C:
            d2 = grid[nr][nc]
            steps = cnt + 1 if d == dir else 0
            alt.append((d2, (nr, nc, d, steps)))

    return alt

def printpath(path, node, grid):
    draw = copygrid(grid)
    p = True
    while p:
        r, c, dir, _ = node
        L = '>'
        if dir == 1: L = 'v'
        if dir == 2: L = '<'
        if dir == 3: L = '^'
        draw[r][c] = L

        node = path[node]
        if node[0] == 0 and node[1] == 0:
            p = False
    printgrid(draw)


def dij(S, g):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    INF = 10**12
    R = len(g) -1
    C = len(g[0]) -1
    path = {}


    def inf():
        return INF
    dist = dd(inf)

    pq = []
    for node in S:
        dist[node] = 0
        pq.append((0, node))
    heapq.heapify(pq)
    done = False
    steps = 0
    pr = False
    while pq and not done:
        (nd, node) = heapq.heappop(pq)

        if (node[0] == R and node[1] == C and node[3] >= 3):
            #printpath(path, node, g)
            
            return nd
        if dist[node] != nd: continue
        #if node == T: return dist[T]
        for (dd_, nn) in gen(node, g):

            alt = dist[node] + dd_
            
            if dist[nn] > alt:
                dist[nn] = alt
                path[nn] = node
                steps += 1
                heapq.heappush(pq, (dist[nn], nn))



    return dist   

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = [parse(line) for line in lines]
    su = dij([(0, 0, 0, 0), (0, 0, 1, 0)], grid)
    
    
    return su

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = [parse(line) for line in lines]
    su = dij([(0, 0, 0, 0), (0, 0, 1, 0)], grid)
    
    
    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,17, p1, p2, cmds)
if stats: print_stats()

#manual()
