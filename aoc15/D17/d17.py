import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from itertools import chain, combinations
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

from itertools import chain, combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def parse(line):
    return int(line)

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    vals = [parse(line) for line in lines]
    ps = power_set(vals)
    T =150
    cnt=0
    for s in ps:    
        if sum(s) == T:
            cnt+= 1
    return cnt

def p2(v):

    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    vals = [parse(line) for line in lines]
    ps = power_set(vals)
    T =150
    cnt=0
    minL = len(vals) 
    for s in ps:
        alt = len(s)    
        if sum(s) == T:
            if alt < minL: 
                cnt = 1
                minL = alt
            elif alt == minL:
                cnt += 1
            
    return cnt


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,17, p1, p2, cmds)
if stats: print_stats()
#manual()
