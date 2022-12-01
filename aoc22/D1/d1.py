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

def parse(line):
    return lazy_ints(line.split())
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    #data = [parse(line) for line in lines]
    su = 0
    for i in range(len(chunks)):
        alt = 0
        for line in chunks[i].split('\n'):
            c = int(line)
            alt += c
        su = max(su, alt)

    return su


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    #data = [parse(line) for line in lines]
    su = 0
    li = []
    for ch in chunks:
        alt = 0
        for line in ch:
            c = int(line)
            alt += c
        li.append(alt)
    li.sort(reverse = True)
    return sum(li[0:3])


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,1, p1, p2, cmds)
if stats: print_stats()

#manual()
