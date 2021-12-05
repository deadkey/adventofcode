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
    return lazy_ints(multisplit(line, ',', '->'))

def draw1(x1, y1, x2, y2, grid):
    if x1 == x2 or y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[y, x] += 1


def draw(x1, y1, x2, y2, grid):
    if x1 == x2 or y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[y, x] += 1
    elif abs(x1 - x2) == abs(y1 -y2):
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        x, y = x1, y1
        while (x, y) != (x2, y2):
            grid[y, x] += 1
            x += dx
            y += dy
        grid[y, x] += 1


def p1(v):
    grid = Counter()
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        a, b, c, d = data[i]
        draw1(a, b, c, d, grid)
    cnt = 0

    for k, v in grid.items():
        if v >= 2:
            cnt += 1


    return cnt

def p2(v):
    lines = v.strip().split('\n')
    grid = Counter()
    data = [parse(line) for line in lines]
    for i in range(len(data)):
        a, b, c, d = data[i]
        draw(a, b, c, d, grid)
    cnt = 0

    for k, v in grid.items():
        if v >= 2:
            cnt += 1


    return cnt


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,5, p1, p2, cmds)
if stats: print_stats()
#manual()
