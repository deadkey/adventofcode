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
    return lazy_ints(multisplit(line, ' ')) 

def isinc(li):
    prev = li[0]
    
    for n in li[1:]:
        if 1<= n - prev <= 3: 
            pass
        else:
            return False    
        prev = n
    return True

def isdec(li):
    prev = li[0]
    
    for n in li[1:]:
        if 1<= prev - n <= 3: 
            pass
        else:
            return False    
        prev = n
    return True


def safe(li):
    if isinc(li): return True
    if isdec(li): return True
    return False

def safe2(li):
    for i in range(len(li)):
        li2 = li[:i] + li[i+1:]

        if isinc(li2): return True
        if isdec(li2): return True
    return False

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        if safe(d): su += 1
        

    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        if safe2(d): su += 1
        

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,2, p1, p2, cmds)
if stats: print_stats()

#manual()
