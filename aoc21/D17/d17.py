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
    line = line.replace('target area:', '')
    line = line.replace('..', ' ')
    line = line.replace('x=', '')
    line = line.replace('y=', '')
    line = line.replace(',', '')
    
    
    return lazy_ints(line.split())

def test(sx, sy, target):
    minx, maxx, miny, maxy = target
    x, y = 0, 0
    ok = False
    best = -10**30
    for step in range(1000):
        x += sx
        y += sy
        if sx != 0:
            sx = sx -1 if sx > 0 else sx + 1
        sy -= 1
        #db(step, x, y)
        best = max(best, y)
        if minx <= x <= maxx and miny <= y <= maxy:
            ok = True
    return ok, best
            

def solve(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines][0]
    
    best = 0, 0, 0
    N = 172
    vel = set()
    for x in range(0, N):
        for y in range(-N, N):
            ok, yval = test(x, y, data)
            #db(ok, x, y, yval)
            if ok:
                best = max(best, (yval, x, y))
                vel.add((x, y))


    return best[0], len(vel)


def p1(v):
    return solve(v)[0]

def p2(v):
    return solve(v)[1]


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,17, p1, p2, cmds)
if stats: print_stats()
#manual()
