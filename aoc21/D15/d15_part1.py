import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict, Counter
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(list(line.split()[0]))
    

import heapq

def dij(S, T, grid):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    INF = 10**12
    def inf(): return INF

    dist = defaultdict(inf)
    R = len(grid)
    C = len(grid[0])
    pq = []
    dist[S] = 0
    pq.append((0, S))
    heapq.heapify(pq)
    done = False
    while pq and not done:
        (nd, node) = heapq.heappop(pq)
        if node == T: return dist[T]
        r, c = node
        for nn in get4nb(r, c, 0, R, 0, C):
            rr,cc = nn
            alt = dist[node] + grid[rr][cc]
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn))

    return dist[T]

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    grid = [parse(line) for line in lines]
    R = len(grid)
    C = len(grid[0])
    dists = dij((0, 0), (R-1, C-1), grid)
    return dists

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,15, p1, p2, cmds)
if stats: print_stats()
#manual()
