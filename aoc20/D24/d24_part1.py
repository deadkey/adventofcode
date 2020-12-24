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
    di = []
    L = len(line)
    line = line + ' '
    i = 0
    while i < L:
        ch = line[i]
        if ch == 'e' or ch == 'w':
            di.append(ch)
            i += 1
        else:
            ch = line[i: i+2]
            di.append(ch)
            i += 2
    

    return di
    
def walk(grid, path):
    r, c = 0, 0
    DIR = {'e': (0, 2), 'se':(1, 1), 'sw':(1, -1), 'w':(0, -2), 'nw':(-1, -1), 'ne':(-1, 1)}
    for ins in path:
        d = DIR[ins]
        r, c = r + d[0], c + d[1]
    grid[r, c] = not grid[r, c]

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    grid = defaultdict(bool)
    for path in data:
        walk(grid, path)
    cnt = 0
    for coord, v in grid.items():
        if grid[coord]: cnt +=1

    return cnt

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,24, p1, p2, cmds)
if stats: print_stats()
#manual()
