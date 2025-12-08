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
    return lazy_ints(multisplit(line, '-')) 
    
def ok(food, intervals):
    for li in intervals:
        start, end = li
        if start <= food <= end:
            return True
    return False

def p1(v):
    lines = v.strip().split('\n')
    intervals, ing = tochunks(v)
    su = 0
    intervals = [parse(line) for line in intervals]
    ing = [int(line) for line in ing]
    for food in ing:
        if ok(food, intervals): su += 1
        
    return su

def overlaps(A, B):
    return B[0] <= A[1]

def mergeint(A, B):
    start = min(A[0], B[0])
    end = max(A[1], B[1])
    return [start, end]

def p2(v):
    lines = v.strip().split('\n')
    intervals, ing = tochunks(v)
    su = 0
    intervals = sorted([parse(line) for line in intervals])
    newintervals = []
    db(intervals)
    
    while len(intervals) >= 2:
        last = intervals.pop()
        if overlaps(intervals[-1], last):
            newint = mergeint(intervals[-1], last)
            intervals.pop() #the second to last
            intervals.append(newint)
        else:
            newintervals.append(last)
    newintervals.append(intervals[0])
    db(newintervals)
    for li in newintervals:
        start, end = li
        su +=  end - start + 1
    return su
    


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,5, p1, p2, cmds)
if stats: print_stats()

#manual()
