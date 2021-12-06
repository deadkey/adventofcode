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
    

def p1(v, N = 80):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    fish = Counter(data[0])
    for i in range(N):
        nxt = Counter()
        for (k, v) in fish.items():
            if k == 0:
                nxt[8] += v
                k = 7
            nxt[k-1] += v
        fish = nxt

    return sum(fish.values())

def p2(v):
    return p1(v, 256)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,6, p1, p2, cmds)
if stats: print_stats()
#manual()
