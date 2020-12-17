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
    return lazy_ints(line.split())

def cntgrid(cube):
    return sum(cube.values())


def getnb2(X, Y, Z, W):
    diff = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                for w in [-1, 0, 1]:
                    diff.append((x, y, z, w))
    
    diff.remove((0, 0, 0, 0))

    nb = []
    for dx, dy, dz, dw in diff:
        nb.append((X+dx, Y + dy , Z + dz, W + dw))
    return nb   


def getnb(X, Y, Z):
    diff = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                diff.append((x, y, z))
    
    diff.remove((0, 0, 0))
    assert len(diff) == 26

    nb = []
    for dx, dy, dz in diff:
        nb.append((X+dx, Y + dy , Z + dz))
    return nb   

def nxtgen2(cube):
    nxt = defaultdict(bool)
    c = Counter()
    for (x, y, z, w), active in cube.items():
        if active:
            for coord in getnb2(x, y, z, w):
                #db(coord)
                c[coord]+=1
    #db(c)
    for coord, val in c.items():
        if val == 3 and not cube[coord]:
            nxt[coord]  = True
        if 2 <= val <= 3 and cube[coord]:
            nxt[coord]  = True
        

    return nxt

def nxtgen(cube):
    nxt = defaultdict(bool)
    c = Counter()
    for (x, y, z), active in cube.items():
        if active:
            for coord in getnb(x, y, z):
                #db(coord)
                c[coord]+=1
    #db(c)
    for coord, val in c.items():
        if val == 3 and not cube[coord]:
            nxt[coord]  = True
        if 2 <= val <= 3 and cube[coord]:
            nxt[coord]  = True
        

    return nxt
    

R, C = 0, 0

def p1(v):
    global R, C
    lines = v.strip().split('\n')
    grid, R, C = togrid(lines)
    cube = defaultdict(bool)
    for r in range(R):
        for c in range(C):
            cube[(c, r, 0)] = grid[r][c] == '#'
    #db(cube)

    for level in range(6):
        cube = nxtgen(cube)

    cnt = cntgrid(cube)


    return cnt

def p2(v):
    lines = v.strip().split('\n')
    grid, R, C = togrid(lines)
    cube = defaultdict(bool)
    for r in range(R):
        for c in range(C):
            cube[(c, r, 0, 0)] = grid[r][c] == '#'
    #db(cube)

    for level in range(6):
        cube = nxtgen2(cube)

    cnt = cntgrid(cube)


    return cnt


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,17, p1, p2, cmds)
if stats: print_stats()
#manual()
