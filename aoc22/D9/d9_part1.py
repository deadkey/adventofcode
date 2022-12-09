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
    #return lazy_ints(line.split())
    return lazy_ints(multisplit(line, ' ')) 
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    head = 0, 0
    tail = 0,0
    vis = set()
    for i in range(len(data)):
        d = data[i]
        dir, steps = d
        dr = 0
        dc = 0
        if dir == 'R':
            dc = 1
        if dir == 'U':
            dr = 1
        if dir == 'D':
            dr = -1
        if dir == 'L':
            dc = -1
        for s in range(steps):
            head = head[0] + dr, head[1] + dc
            if head[0] == tail[0] and abs(head[1] - tail[1]) > 1:
                tail = tail[0], tail[1] + dc
            elif head[1] == tail[1] and abs(head[0] - tail[0]) > 1:
                tail = tail[0] + dr, tail[1]
            elif abs(head[0] - tail[0]) == 2:
                tail = tail[0] + dr, head[1]
            elif abs(head[1] - tail[1]) == 2:
                tail = head[0], tail[1] + dc
            vis.add(tail)
                
            


    return len(vis)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,9, p1, p2, cmds)
if stats: print_stats()

#manual()
