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

def diffs(li):
    nxt = []
    for a, v in zip(li[1:], li):
        nxt.append(a -v)
    
    return nxt

def hist(d):
    last = [d[-1]]
    nxt = diffs(d)
    m = max(nxt)
    
    while not all(i == 0 for i in nxt):
        last.append(nxt[-1])
        nxt = diffs(nxt)
        

    val = 0
    for l in last[::-1]:
        val = l + val
    
    return val

def hist2(d):
    last = [d[0]]
    nxt = diffs(d)
    m = max(nxt)
    
    while not all(i == 0 for i in nxt):
        last.append(nxt[0])
        nxt = diffs(nxt)
        

    val = 0
    for l in last[::-1]:
        val = l - val
    
    return val


#1842176504 wrong

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        h = hist2(d)
        su += h

    return su

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        h = hist(d)
        su += h

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,9, p1, p2, cmds)
if stats: print_stats()

#manual()
