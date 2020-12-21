import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *

from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line = line.replace(':', '')
    return lazy_ints(line.split())

def rotate(grid, R, C):
    newgrid = emptygrid(R, C)
    for r in range(R):
        for c in range(C):
            nc = C - r
            nr = c
            newgrid[nr][nc] = grid[r][c]
    return newgrid 

def getsides(grid, R,  C):
    up = [grid[0][c] for c in range(C)]
    right = [grid[r][C-1] for r in range(R)]
    down = [grid[R-1][c] for c in range(C)]
    left = [grid[r][0] for r in range(R)]
    return [up, right, down, left]

def samesides(sides1, sides2):
    for side in sides1:
        for side2 in sides2:
            if side == side2 or side == side2[::-1]:
                return 1
    return 0




def p1(v):
    imgs = chunks(v)
    grids = []
    corners = []
    for img in imgs:
        lines = img.split('\n')
        _, id = parse(lines[0])

        grid, R, C = togrid(lines[1:])
        
        #printgrid(grid)
        #db('')

        sides = getsides(grid, R, C)
        grids.append((id, grid, sides))
    N = len(grids)
    for i in range(N):

        myid, mygrid, mysides = grids[i]
        cnt = 0
        for j in range(N):
            if j != i: 

                oid, ogrid, osides = grids[j]
                cnt += samesides(mysides, osides)  
        if cnt == 2:
            corners.append(myid)
        else:
            db(myid)


    db(corners)
    return mul(corners)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,20, p1, p2, cmds)
if stats: print_stats()
#manual()
