import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return list(line)

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    steps = 0
    grid, R, C = togrid(lines)
    db(grid)
    N = 4
    i = 0
    changed = True
    while changed:
        steps += 1
        i += 1
        nxt = emptygrid(R, C, '.')
        changed = False
        for r in range(R):
            for c in range(C):
                nind = get8nb(r, c, 0, R, 0, C)
                cnt = 0
                for nr, nc in nind:
                    if grid[nr][nc] == '#':
                        cnt += 1
                
                if grid[r][c] == 'L' and cnt == 0:
                    nxt[r][c] = '#'
                    changed = True
                elif grid[r][c] == '#' and cnt >= 4:
                    nxt[r][c] = 'L'
                    changed = True
                else:
                    nxt[r][c] = grid[r][c]
        grid = nxt
        #printgrid(nxt)
        db('')
    
    occ = cntgrid(grid, '#')
    return occ

def getDiag(grid, r, c, rmin = -INF, rmax = INF, cmin = -INF, cmax = INF):
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    nb = 0
    for dr, dc in diff:
        seen = False
        tr, tc = r, c
    
        while not seen and rmin <= tr + dr < rmax and cmin <= tc + dc < cmax:
            
            tr = tr + dr
            tc = tc + dc
            #if grid[r][c] == 'L':
            #    db(tr, tc, dr, dc, grid[tr][tc])
            if grid[tr][tc] != '.':
                if grid[tr][tc] == '#': nb += 1
                
                seen = True
            
    return nb     

def debug(file):
    v = open(file, 'r').read()
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    steps = 0
    grid, R, C = togrid(lines)
    
    changed = True
    while changed:
        steps += 1
        
        nxt = emptygrid(R, C, '.')
        changed = False
        for r in range(R):
            for c in range(C):
                cnt = getDiag(grid, r, c, 0, R, 0, C)
                if grid[r][c] == 'L':
                    db('Cnt', cnt)
                #db(grid[r][c], cnt)
                if grid[r][c] == 'L' and cnt == 0:
                    nxt[r][c] = '#'
                    changed = True
                elif grid[r][c] == '#' and cnt >= 5:
                    nxt[r][c] = 'L'
                    changed = True
                else:
                    nxt[r][c] = grid[r][c]

        grid = nxt
        db(f'steps {steps}\n')
    
        printgrid(nxt)
        
    occ = cntgrid(grid, '#')


def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    steps = 0
    grid, R, C = togrid(lines)
    N = 4
    i = 0
    changed = True
    while changed:
        steps += 1
        i += 1
        nxt = emptygrid(R, C, '.')
        changed = False
        for r in range(R):
            for c in range(C):
                cnt = getDiag(grid, r, c, 0, R, 0, C)
                
                if grid[r][c] == 'L' and cnt == 0:
                    nxt[r][c] = '#'
                    changed = True
                elif grid[r][c] == '#' and cnt >= 5:
                    nxt[r][c] = 'L'
                    changed = True
                else:
                    nxt[r][c] = grid[r][c]
        grid = nxt
        db(f'steps {steps}\n')
    
        #printgrid(nxt)
        
    occ = cntgrid(grid, '#')
    return occ


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,11, p1, p2, cmds)
if stats: print_stats()
#manual()
