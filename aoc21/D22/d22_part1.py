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
    line = line.replace('x=', '').replace(',', ' ').replace('..', ' ').replace('y=', '').replace('z=', '')
    return lazy_ints(line.split())

def on(x, x2, y, y2, z, z2, grid):
    x = max(x, -50)
    x2 = min(x2, 50)
    y = max(y, -50)
    y2 = min(y2, 50)
    z = max(z, -50)
    z2 = min(z2, 50)
    for xx in range(x, x2+1):
        for yy in range(y, y2 + 1):
            for zz in range(z, z2 + 1):
                grid[xx, yy, zz] = 1

def off(x, x2, y, y2, z, z2, grid):
    x = max(x, -50)
    x2 = min(x2, 50)
    y = max(y, -50)
    y2 = min(y2, 50)
    z = max(z, -50)
    z2 = min(z2, 50)
    for xx in range(x, x2+1):
        for yy in range(y, y2 + 1):
            for zz in range(z, z2 + 1):
                grid[xx, yy, zz] = 0

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    grid = dd(int)
    for i, ins in enumerate(data):
        db(f'{i}/{len(data)}')
        cmd, x, x2, y, y2, z, z2 = ins
        if cmd == 'on':
            on(x, x2, y, y2, z, z2, grid)
        else:
            off(x, x2, y, y2, z, z2, grid)

    return sum(grid.values())

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,22, p1, p2, cmds)
if stats: print_stats()
#manual()
