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

def test(r, c, dr, dc, grid):

    beams = [(r, c, dr, dc)]
    R = len(grid)
    C = len(grid[0])
    N = 10
    visited = set()
    while len(beams):
        nxt = []
        for r, c, dr, dc in beams:
            change = len(nxt)
            if 0 <= r < R and 0 <= c < C and (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                t = grid[r][c]
                
                #Forward 
                if t == '.':
                    nxt.append((r + dr, c+ dc, dr, dc))
                if t == '-' and dc != 0:
                    nxt.append((r + dr, c+ dc, dr, dc))
                if t == '|' and dr != 0:
                    nxt.append((r + dr, c+ dc, dr, dc))
                
                #splits
                if t == '-' and dc == 0:
                    nxt.append((r, c +1, 0, 1))
                    nxt.append((r, c - 1, 0, -1))
                    
                if t == '|' and dc != 0:
                    nxt.append((r -1, c, -1, 0))
                    nxt.append((r + 1, c, 1, 0))
                if t == '/':
                    #r to up
                    if (dr, dc) == (0, 1):
                        nxt.append((r -1, c, -1, 0))
                    #down to left
                    if (dr, dc) == (1, 0):
                        nxt.append((r, c-1, 0, -1))
                    #left to down
                    if (dr, dc) == (0, -1):
                        nxt.append((r+1, c, 1, 0))
                    #up to right 
                    if (dr, dc) == (-1, 0):
                        nxt.append((r, c+1, 0, 1))
                if t == '\\':
                    #d to r
                    if (dr, dc) == (1, 0):
                        nxt.append((r, c+1, 0, 1))
                    #left to up
                    if (dr, dc) == (0, -1):
                        nxt.append((r-1, c, -1, 0))
                    #r to down
                    if (dr, dc) == (0, 1):
                        nxt.append((r+1, c, 1, 0))
                    #up to left 
                    if (dr, dc) == (-1, 0):
                        nxt.append((r, c-1, 0, -1))
                   

                #db(nxt)
        
        beams = nxt


    draw = copygrid(grid)        
    for r, c, dr, dc in beams:
        if (dr, dc) == (0, 1):
            draw[r][c] = '>'
                    #down to left
        if (dr, dc) == (1, 0):
            draw[r][c] = 'v'
                    #left to down
        if (dr, dc) == (0, -1):
            draw[r][c] = '<'

                #up to right 
        if (dr, dc) == (-1, 0):
            draw[r][c] = '^'

        printgrid(draw)

    vis2 = set()
    for r, c, _, _ in visited:
        vis2.add((r, c))
    return len(vis2)

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    grid = togrid(lines)
    su = 0
    R = len(grid)
    C = len(grid[0])
    best = 0
    for r in range(R):
        alt = test(r, 0, 0, 1, grid)
        db(alt)
        best = max(best, alt)
    for r in range(R):
        alt = test(r, C-1, 0, -1, grid)
        db(alt)
        best = max(best, alt)
    for c in range(C):
        alt = test(0, c, 1, 0, grid)
        db(alt)
        best = max(best, alt)
    for c in range(C):
        alt = test(R-1, c, -1, 0, grid)
        db(alt)
        best = max(best, alt)
    return best



def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    grid = togrid(lines)
    su = 0
    beams = [(0, 0, 0, 1)]
    R = len(grid)
    C = len(grid[0])
    N = 10
    visited = set()
    while len(beams):
        nxt = []
        for r, c, dr, dc in beams:
            change = len(nxt)
            if 0 <= r < R and 0 <= c < C and (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                t = grid[r][c]
                
                #Forward 
                if t == '.':
                    nxt.append((r + dr, c+ dc, dr, dc))
                if t == '-' and dc != 0:
                    nxt.append((r + dr, c+ dc, dr, dc))
                if t == '|' and dr != 0:
                    nxt.append((r + dr, c+ dc, dr, dc))
                
                #splits
                if t == '-' and dc == 0:
                    nxt.append((r, c +1, 0, 1))
                    nxt.append((r, c - 1, 0, -1))
                    
                if t == '|' and dc != 0:
                    nxt.append((r -1, c, -1, 0))
                    nxt.append((r + 1, c, 1, 0))
                if t == '/':
                    #r to up
                    if (dr, dc) == (0, 1):
                        nxt.append((r -1, c, -1, 0))
                    #down to left
                    if (dr, dc) == (1, 0):
                        nxt.append((r, c-1, 0, -1))
                    #left to down
                    if (dr, dc) == (0, -1):
                        nxt.append((r+1, c, 1, 0))
                    #up to right 
                    if (dr, dc) == (-1, 0):
                        nxt.append((r, c+1, 0, 1))
                if t == '\\':
                    #d to r
                    if (dr, dc) == (1, 0):
                        nxt.append((r, c+1, 0, 1))
                    #left to up
                    if (dr, dc) == (0, -1):
                        nxt.append((r-1, c, -1, 0))
                    #r to down
                    if (dr, dc) == (0, 1):
                        nxt.append((r+1, c, 1, 0))
                    #up to left 
                    if (dr, dc) == (-1, 0):
                        nxt.append((r, c-1, 0, -1))
                   

                #db(nxt)
        
        beams = nxt


    draw = copygrid(grid)        
    for r, c, dr, dc in beams:
        if (dr, dc) == (0, 1):
            draw[r][c] = '>'
                    #down to left
        if (dr, dc) == (1, 0):
            draw[r][c] = 'v'
                    #left to down
        if (dr, dc) == (0, -1):
            draw[r][c] = '<'

                #up to right 
        if (dr, dc) == (-1, 0):
            draw[r][c] = '^'

        printgrid(draw)

    vis2 = set()
    for r, c, _, _ in visited:
        vis2.add((r, c))
    return len(vis2)




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,16, p1, p2, cmds)
if stats: print_stats()

#manual()
