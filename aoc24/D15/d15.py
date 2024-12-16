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

def free(grid, r, c, dr, dc):
    
    while True:
        r += dr
        c += dc
        if grid[r][c] == '#':
            return -1, -1, False
        if grid[r][c] == '.':
            return r, c, True
        #grid[r][c] == 'O' continue
    return -1, -1, False
        

def step(grid, step, curr):
    dir = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    dr, dc = dir[step]
    nxtgrid = grid.copy()
    r, c = curr
    nr, nc = r + dr, c + dc
    if grid[nr][nc] == '.':
        return nxtgrid, (nr, nc)
    if grid[nr][nc] == '#':
        return nxtgrid, curr
    if grid[nr][nc] == 'O':
        freer, freec, ok = free(grid, r, c, dr, dc)
        if ok:
            nxtgrid[freer][freec] = 'O'
            nxtgrid[nr][nc] = '.'
            return nxtgrid, (nr, nc)
    return grid, curr

def pushupdown(grid, r, c, dr, curr):
    
    nxtgrid = grid.copy()
    r, c = curr 
    tomove = [curr]
    cols = set([c])

    cr = r + dr
    while True:
        pnt = 0
        for cc in cols:
            if grid[cr][cc] == '#':
                return nxtgrid, curr
            if grid[cr][cc] == '.':
                pnt += 1
        if pnt == len(cols):
            break
        
        nxtcols = set()
        for cc in cols:
            if grid[cr][cc] == '[':
                nxtcols.add(cc)
            
                nxtcols.add(cc+1)
                if (cr, cc) not in tomove:
                    tomove.append((cr, cc))
                if (cr, cc+1) not in tomove:
                    tomove.append((cr, cc+1))
            if grid[cr][cc] == ']':
                nxtcols.add(cc)
            
                nxtcols.add(cc-1)
                if (cr, cc) not in tomove:
                    tomove.append((cr, cc))
                if (cr, cc-1) not in tomove:
                    tomove.append((cr, cc-1))
        cols = nxtcols
        cr += dr
    
    for nr, nc in tomove[::-1]:
        nxtgrid[nr+dr][nc] = nxtgrid[nr][nc]
        nxtgrid[nr][nc] = '.'
    return nxtgrid, (r+dr, c)
        

    
   

def pushleftright(grid, r, c, dc, curr):
    
    nxtgrid = grid.copy()
    r, c = curr
    nr, nc = r, c + dc
    tomove = [curr]
    
    while grid[nr][nc] == ']' or grid[nr][nc] == '[':
        tomove.append((nr, nc))
        nr, nc = nr, nc + dc
    if grid[nr][nc] == '#':
        return nxtgrid, curr
    
    assert grid[nr][nc] == '.'
    for nr, nc in tomove[::-1]:
        nxtgrid[nr][nc+dc] = nxtgrid[nr][nc]
        nxtgrid[nr][nc] = '.'
    return nxtgrid, (r, c+dc)
    

def step2(grid, step, curr):
    dir = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    dr, dc = dir[step]
    nxtgrid = grid.copy()
    r, c = curr
    nr, nc = r + dr, c + dc
    if grid[nr][nc] == '.':
        return nxtgrid, (nr, nc)
    if grid[nr][nc] == '#':
        return nxtgrid, curr
    if grid[nr][nc] == '[' or grid[nr][nc] == ']':
        if dr != 0:
            return pushupdown(grid, r, c, dr, curr)
        else:
            return pushleftright(grid, r, c, dc, curr)
    return grid, curr
            
            
def modify(line):
    row = []
    for c in line[::-1]:
        if c == '#':
            row.extend(['#','#'])
        if c == 'O':
            row.extend([']','['])
        if c == '.':
            row.extend(['.','.'])
        if c == '@':
            row.extend(['.','@'])
    return list(row[::-1])
        


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    modified = []
    for line in chunks[0]:
        modified.append(modify(line))
    grid = togrid(modified)
    
    lines = chunks[1]
    moves = []
    start = (0, 0)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                start = (r, c)
    grid[start[0]] [start[1]] = '.'
    for line in lines:
        moves.extend(list(line))
    
    su = 0
    curr = start
    for i, s in enumerate(moves):
        pos, curr = step2(grid, s, curr)
       
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '[':
                su += 100 * r + c
        

    return su

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(chunks[0])
    
    lines = chunks[1]
    moves = []
    start = (0, 0)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                start = (r, c)
    grid[start[0]] [start[1]] = '.'
    for line in lines:
        moves.extend(list(line))
    
    su = 0
    curr = start
    for i, s in enumerate(moves):
        pos, curr = step(grid, s, curr)
        
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                su += 100 * r + c
        

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,15, p1, p2, cmds)
if stats: print_stats()

#manual()
