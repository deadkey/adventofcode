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
    
def wins(t, d):
    cnt = 0
    for speed in range(t+1):
        left = t - speed
        dist = left * speed
        if dist > d:cnt += 1
    return cnt

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 1
    times = data[0][1:]
    dist = data[1][1:]
    
    for t, d in zip(times, dist):
        ways = wins(t, d)
        su *= ways

    return su

def p2(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 1
    times = data[0][1:]
    dist = data[1][1:]
    time = int(merge(times))
    dist = int(merge(dist))
    return wins(time, dist)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,6, p1, p2, cmds)
if stats: print_stats()

#manual()
