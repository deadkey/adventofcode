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
    return lazy_ints(line.split(','))

def cost1(pos, target):
    cnt = 0
    for p in pos:
        cnt += abs(p - target)
    return cnt

def cost2(pos, target):
    cnt = 0
    for p in pos:
        diff = abs(p - target)
        d = (diff + 1) * diff//2
        cnt += d
    return cnt

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 10**30
    data = data[0]
    mn = min(data)
    mx = max(data)
    for v in range(mn, mx + 1):

        alt = cost1(data, v)
        su = min(su, alt)


    return su

def p2(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 10**30
    data = data[0]
    mn = min(data)
    mx = max(data)
    for v in range(mn, mx + 1):

        alt = cost2(data, v)
        su = min(su, alt)


    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,7, p1, p2, cmds)
if stats: print_stats()
#manual()
