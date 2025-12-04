import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
from collections import defaultdict as dd, Counter
from itertools import chain, combinations, permutations
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
    return list(map(int, list(line)))

def getmax(li):
    first = 0
    first_indx = 0
    last = 0
    for i in range(0, len(li)-1):
        if li[i] > first:
            first = li[i]
            first_indx = i
    for i in range(first_indx+1, len(li)):
        if li[i] > last:
            last = li[i]
    return 10 * first + last 


def getmax2(li):
    numbers = []
    start = 0
    for k in range(1, 13):
        best = 0
        best_index = start
        for i in range(start, len(li) - (12-k)):
            if li[i] > best:
                best = li[i]
                best_index = i
        start = best_index + 1
        numbers.append(best)
   
    s = 0
    for k in numbers:
        s *= 10
        s += k
    return s
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        g=  getmax(d)
        db(g)
        su += g

    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        g=  getmax2(d)
        db(g)
        su += g

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,3, p1, p2, cmds)
if stats: print_stats()

#manual()
