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
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())

def move(grid):
    canmove = []
    R= len(grid)
    C = len(grid[0])
    no = 0
    canmove = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '>':
                if grid[r][(c + 1) % C] == '.':
                    canmove.append((r, c))
    
    for (r, c) in canmove:
        grid[r][(c + 1) % C] = '>'
        grid[r][c] = '.'
        no += 1
        
    #db('After east')
    #printgrid(grid)

    canmove = []   
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'v':
                if grid[(r + 1) % R][c] == '.':
                    canmove.append((r, c))
               
    for (r, c) in canmove:
        grid[(r + 1) % R][c] = 'v'
        grid[r][c] = '.'
        no += 1

    #db('After south')
    #printgrid(grid)
    return no, grid
    
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    grid = togrid(data)
    N = 10000
    db(f'Initial')
        
    printgrid(grid)
    for step in range(N):
        no, grid = move(grid)
        #db(f'Step {step}')
        #printgrid(grid)
        #db('###########################')
        su += 1
        if no == 0:
            return su
        
    return su

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,25, p1, p2, cmds)
if stats: print_stats()
#manual()
