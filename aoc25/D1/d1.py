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
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    
    data = [parse(line) for line in lines]
    su = 0
    val = 50
    for d in data:
        if d[0] == 'L':
            val -= int(d[1:])
        else:
            val += int(d[1:])
        
        val = val%100
        if val == 0:
            su += 1

    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    
    data = [parse(line) for line in lines]
    su = 0
    val = 50
    
    for d in data:
        k = 0
        move = int(d[1:])
        prev = val
        if d[0] == 'L':

            for m in range(move):
                val -= 1
                val = val%100
                if val == 0:
                    k += 1
        else:
            for m in range(move):
                val += 1
                val = val%100
                if val == 0:
                    k += 1
        
        su += k

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,1, p1, p2, cmds)
if stats: print_stats()

#manual()
