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

def he(lt):
    return ord(lt) - ord('a')

def ne4_part1(ne, R, C, grid):
    r, c = ne
    cand = grid4nb(r, c, grid)
    alt = []
    for rr, cc in cand:
        if grid[rr][cc] - grid[r][c] <= 1:
            alt.append((rr, cc))
    return alt


def bfs_part1(q, grid, end):
    R = len(grid)
    C = len(grid[0])
    visited = set()
    dist = 0
    for node in q:
        visited.add(node)
    while q:
        q2 = []
        
        for node in q:
            if node == end:
                return dist
            for ne in ne4_part1(node, R, C, grid):
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
        dist += 1
        q = q2
    return -1

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = togrid(data)
    start = 0, 0
    end = 0, 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start = r, c
                grid[r][c] = 0
            elif grid[r][c] == 'E':
                end = r, c
                grid[r][c] = he('z')
            else:
                grid[r][c] = he(grid[r][c])
    
    
    q= [start]
    dist = bfs_part1(q, grid, end)


    return dist

def ne4_part2(ne, R, C, grid):
    r, c = ne
    cand = grid4nb(r, c, grid)
    alt = []
    for rr, cc in cand:
        
        if grid[rr][cc] >= grid[r][c] or grid[rr][cc] == grid[r][c] -1:
            alt.append((rr, cc))
    return alt


def bfs_part2(q, grid, end):
    R = len(grid)
    C = len(grid[0])
    visited = set()
    dist = dd(int)
    for node in q:
        visited.add(node)
    while q:
        q2 = []
        
        for node in q:
            for ne in ne4_part2(node, R, C, grid):
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
                    dist[ne] = dist[node] + 1
        q = q2
    return dist

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = togrid(data)
    start = 0, 0
    end = 0, 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start = r, c
                grid[r][c] = 0
            elif grid[r][c] == 'E':
                end = r, c
                grid[r][c] = he('z')
            else:
                grid[r][c] = he(grid[r][c])
    
    
    q= [end]
    dist = bfs_part2(q, grid, [])
    mn = 10 ** 30
    for item in dist.items():
        r, c = item[0]
        if grid[r][c] == 0:
            mn = min(mn, item[1])

    return mn



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,12, p1, p2, cmds)
if stats: print_stats()

#manual()
