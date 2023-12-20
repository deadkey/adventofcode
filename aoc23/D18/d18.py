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

def area(polygon):
    A = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i-1]
        x2, y2 = polygon[i]
        A += (x1 + x2) * (y2 - y1)
    return abs(A/2)

# number of integer coordinates inside polygon
# assumes polygon has integer coordinates
# Picks formula:
# A = i + p/2 - 1
def ptsInside(polygon):
    import math
    def countBoundaryPoints(polygon):
        P = polygon
        cnt = 0
        for i in range(len(P)):
            dx = P[i][0] - P[i-1][0]
            dy = P[i][1] - P[i-1][1]
            cnt += math.gcd(abs(dx), abs(dy))
        return cnt
    A = area(polygon)
    p = countBoundaryPoints(polygon)
    cntInside = round(A - p/2 + 1)
    return cntInside + p

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = dd(int)
    visited = set()
    r, c = 0, 0
    path = []

    for i in range(len(data)):
        d, step, col = data[i]
        col = col.replace('(', '')
        col = col.replace(')', '')
        steps = int(col[1:6], 16)
        d = int(col[-1])
       

        dr, dc = 0, 0
        if d == 0:
            dc += 1
        if d == 2:
            dc -= 1
        if d == 3:
            dr -= 1
        if d == 1:
            dr += 1
        r, c = r + steps * dr, c + steps * dc
        visited.add((r, c))
        path.append((r, c))
    

    return ptsInside(path)


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = dd(int)
    visited = set()
    r, c = 0, 0
    path = []
    for i in range(len(data)):
        d, step, col = data[i]
        dr, dc = 0, 0
        if d == 'R':
            dc += 1
        if d == 'L':
            dc -= 1
        if d == 'U':
            dr -= 1
        if d == 'D':
            dr += 1
        for s in range(step):
            r, c = r + dr, c + dc
            visited.add((r, c))
            path.append((r, c))
    
    db(len(path))    

    return ptsInside(path)



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,18, p1, p2, cmds)
if stats: print_stats()

#manual()
