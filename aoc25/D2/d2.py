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
    vals = multisplit(line,',')
    vals = [v.split('-') for v in vals]
    return list(map(lazy_ints, vals))

def invalid(val):
    s = str(val)
    H = len(s)//2
    first = s[0:H]
    last = s[H:]
    return first == last    

def invalid2(val):
    ks = []
    s = str(val)
    H = len(s)//2
    for k in range(1, H+1):
        if len(s) % k == 0:
            ks.append(k)
    
    for k in ks:
        first = s[0:k]
        checks = True
        for start in range(k, len(s), k):
            other = s[start:start + k]
            if other != first:
                checks = False
        if checks: return True
       
        
    return False


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = parse(lines[0])
    su = 0
    for i in range(len(data)):
        a, b = data[i]
        for val in range(a, b + 1):
            if invalid(val): su += val
        

    return su

def p2(v):
   

    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = parse(lines[0])
    su = 0
    for i in range(len(data)):
        a, b = data[i]
        for val in range(a, b + 1):
            if invalid2(val): su += val
        

    return su

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,2, p1, p2, cmds)
if stats: print_stats()

#manual()
