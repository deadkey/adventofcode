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
    return lazy_ints(multisplit(line, [' ', ','])) 

def ispossible(des, towels):
    ok = set([0])
    for start in range(len(des)):
        if start not in ok: continue
        for t in towels:
            if des[start:start + len(t)] == t:
                ok.add(start + len(t))
    return len(des) in ok

def ispossible2(des, towels):
    ok = Counter([0])
    for start in range(len(des)):
        if start not in ok: continue
        for t in towels:
            if des[start:start + len(t)] == t:
                ok[start + len(t)] += ok[start]
    return ok[len(des)]

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    towels = parse(chunks[0][0])
    designs = [parse(line) for line in chunks[1]]

    su = 0
    for des in designs:
        su += ispossible(des, towels)


    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v) 
    towels = parse(chunks[0][0])
    designs = [parse(line) for line in chunks[1]]
    
    su = 0
    for des in designs:
        su += ispossible2(des, towels)


    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,19, p1, p2, cmds)
if stats: print_stats()

#manual()
