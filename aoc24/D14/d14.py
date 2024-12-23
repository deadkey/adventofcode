import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
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
    return lazy_ints(multisplit(line, [' ',',','=', 'p', 'v'])) 

def step(robots, w, h):
    new_robots = []
    for r in robots:
        px, py, vx, vy = r
        px += vx
        py += vy
        px %= w
        py %= h
        new_robots.append([px, py, vx, vy])
    return new_robots    

def nb(robots):
    pos = Counter()
    for r in robots:
        px, py, vx, vy = r
        pos[(px, py)] += 1
    
    ne = 0
    for x, y in pos.keys():
        for a, b in get8nb(x, y):
            if (a, b) in pos:
                ne += 1
    return ne


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    robots = []
    for i in range(len(data)):
        d = data[i]
        robots.append(d)
    w = 101
    h = 103
    for s in range(10000):
        robots = step(robots, w, h)

        ne = nb(robots)
        if ne > 1000:
            grid = [['.' for _ in range(w)] for _ in range(h)]
            #if s % 10 == 0:
            db('Step ', s)
            for r in robots:
                px, py, _, _ = r
                grid[py][px] = '#'
            printgrid(grid)
            db('#######################')
            break
    return s+1
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    robots = []
    for i in range(len(data)):
        d = data[i]
        robots.append(d)
    w = 101
    h = 103
    for s in range(100):
        robots = step(robots, w, h)
    
    q = [0, 0, 0, 0]
    wmid = w//2
    hmid = h//2
    for r in robots:
        px, py, _, _ = r
        if px == wmid or py == hmid: continue
        if px < wmid and py < hmid:
            q[0] += 1
        if px < wmid and py > hmid:
            q[1]+=1
        if px > wmid and py < hmid:
            q[2] += 1
        if px > wmid and py > hmid:
            q[3] += 1
    su = 1
    grid = [['.' for _ in range(w)] for _ in range(h)]
    for r in robots:
        px, py, _, _ = r
        grid[py][px] = '#'
    printgrid(grid)
    db(q)
    for n in q:
        su *= n

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,14, p1, p2, cmds)
if stats: print_stats()

#manual()
