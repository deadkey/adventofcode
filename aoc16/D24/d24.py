import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from itertools import permutations
from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())


def bfs(grid, R, C, sr, sc, T):
    visited = set()
    seen = frozenset([0])
    node = sr, sc, seen
    
    visited.add(node)
    q = [node]
    moves = 0
    while q:
        q2 = []
        for r, c, seen in q:
            if len(seen) == T: return moves
            nbs = get4nb(r, c, 0, R, 0, C)

            for rr, cc in nbs:
                ch = grid[rr][cc]
                if ch == '#':
                    continue
                node = rr, cc, seen
                if isint(ch):
                    newset = frozenset([int(ch)])| seen
                    node = rr, cc, newset
                    
                if node not in visited:
                    visited.add(node)
                    q2.append(node)
        q = q2
        moves += 1
    return moves    

def bfs2(grid, R, C, sr, sc, sv):
    
    visited = set()
    node = sr, sc
    visited.add(node)
    q = [node]
    moves = 0
    dists = {sv:0}


    while q:
        q2 = []
        for r, c in q:
            nbs = get4nb(r, c, 0, R, 0, C)

            for rr, cc in nbs:
                ch = grid[rr][cc]
                if ch == '#':
                    continue
                node = rr, cc
                    
                if node not in visited:
                    if isint(ch):
                        dists[int(ch)] = moves +1
                    visited.add(node)
                    q2.append(node)

        q = q2
        moves += 1
    return dists  

def calcdist(order, dist_map):
    d = 0
    prev = 0
    for node in order:
        d += dist_map[prev][node]
        prev = node
    return d

def p1(v):
    lines = v.strip().split('\n')
    grid, R, C = togrid(lines)
    sr, sc = findpos(grid, '0')
    mx = 0
    for r in range(R):
        for c in range(C):
            if isint(grid[r][c]):
                mx = max(mx, int(grid[r][c]))
    db('Startnode ', sr, sc, grid[sr][sc])
    return bfs(grid, R, C, sr, sc, mx+1)

def p2(v):
    lines = v.strip().split('\n')
    grid, R, C = togrid(lines)
    sr, sc = findpos(grid, '0')
    mx = 0
    dist_map = {}
    vals = []
    for r in range(R):
        for c in range(C):
            if isint(grid[r][c]):
                
                dist2oth = bfs2(grid, R, C, r, c, int(grid[r][c]))
                dist_map[int(grid[r][c])] = dist2oth
                vals.append(int(grid[r][c]))
    shortest = 10 ** 10
    for p in permutations(vals):
        order = list(p) + [0]
        d = calcdist(order, dist_map)
        shortest = min(shortest, d)
    return shortest


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,24, p1, p2, cmds)
if stats: print_stats()
#manual()
