import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)


def iswall(x, y, fav):
    f = x*x + 3*x + 2*x*y + y + y*y + fav
    ones = bin(f).count('1')
    return ones % 2 != 0

def bfs(q, T, grid, R, C):
    visited = set()
    for node in q:
        visited.add(node)
    moves = 0
    while q:
        q2 = []
        for node in q:
            if node == T: return moves
            x, y = node
            for ne in get4nb(x, y, 0, R, 0, C):
                if ne not in visited and grid[ne[0]][ne[1]] == '.':
                    visited.add(ne)
                    q2.append(ne)
        q = q2
        moves += 1
    return moves

def p1(v):
    lines = v.strip().split('\n')
    fav = int(lines[0])
    db(fav)
    N = 100
    grid = [['.'] *N for n in range(N)]
    for r in range(N):
        for c in range(N):
            if iswall(c, r, fav):
                grid[r][c] = '#'
    printgrid(grid)
    return bfs([(1, 1)], (39, 31), grid, N, N)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,13, p1, p2, cmds)
if stats: print_stats()
#manual()
