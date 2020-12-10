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

def parse(line):
    return int(line)

def copygrid(grid):
    R = len(grid)
    nxt =[]
    for r in range(R):
        nxt.append(list(grid[r]))
    return nxt

def emptygrid(R, C, val):
    return [[val] * C for r in range(R)]

def cntgrid(grid, val):
    return sum(grid[r].count(val) for r in range(len(grid)))

def nextgen(grid, R, C):
    nxt = emptygrid(R, C, '.')
    for r in range(R):
        for c in range(C):
            nbsindx = get8nb(r, c, 0, R, 0, C)
            nbs = sum([1 if grid[r][c]== '#' else 0 for r, c in nbsindx])
            if grid[r][c] == '#' and 2 <= nbs <= 3:
                nxt[r][c] = '#'
            if grid[r][c] == '.' and nbs == 3:
                nxt[r][c] = '#'
    return nxt

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    grid, R, C = togrid(lines)
    #printgrid(grid)
    N = 100
    for n in range(N):
        grid = nextgen(grid, R, C)
        db(n)
         
    return cntgrid(grid, '#')

def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    grid, R, C = togrid(lines)
    #printgrid(grid)
    N = 100
    for n in range(N):
        grid[0][0] = '#'
        grid[-1][0] = '#'
        grid[-1][-1] = '#'
        grid[0][-1] = '#'
        grid = nextgen(grid, R, C)
        
        print(f'{n+1}')
        #printgrid(grid)
        #print()
    grid[0][0] = '#'
    grid[-1][0] = '#'
    grid[-1][-1] = '#'
    grid[0][-1] = '#'    
    return cntgrid(grid, '#')


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,18, p1, p2, cmds)
if stats: print_stats()
#manual()
