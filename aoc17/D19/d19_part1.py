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

def newdir(r, c, grid, dir):
    if r + 1 < len(grid) and grid[r+1][c] != ' ' and dir[0] != -1:
        return 1, 0
    
    if 0<=r - 1 < len(grid) and grid[r-1][c] != ' ' and dir[0] != 1:
        return -1, 0
    
    if c + 1 < len(grid[0]) and grid[r][c+1] != ' ' and dir[1] != -1:
        return 0, 1
    
    if 0<+ c + 1 and grid[r][c-1] != ' ' and dir[1] != 1:
        return 0, -1
    

def walk(grid, startpos, dir):
    path = []
    r, c = startpos
    move = True
    while move:
        while grid[r][c] == '|' or grid[r][c] == '-':
            
            #db(r, c, grid[r][c], dir)
            r, c = r + dir[0], c + dir[1]
        
        ch = grid[r][c]
        if ch == '+':
            dir = newdir(r, c, grid, dir)
        elif ch == ' ':
            move = False
        else:
            path.append(ch)
        #db('Path = ', path)
        r, c= r + dir[0], c + dir[1]
    return path



def p1(v):
    lines = v.split('\n')
    grid, R, C = togrid(lines)
    printgrid(grid)
    startpos = 0
    for c in range(C):
        if grid[0][c] == '|': startpos = 0, c
    db(startpos)
    path = walk(grid, startpos, (1, 0))   
    return ''.join(path)

def p2(v):
    pass


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2017,19, p1, p2, cmds)
if stats: print_stats()
#manual()
