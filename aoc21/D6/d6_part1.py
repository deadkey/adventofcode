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
    

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 0
    N = 80
    fish = data[0]
    db(fish)
    for i in range(N):
        nxt = []
        for f in fish:
            n = f - 1
            if n < 0:
                n = 6
                nxt.append(n)
                nxt.append(8)
            else:
                nxt.append(n)
        fish = nxt

    return len(nxt)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,6, p1, p2, cmds)
if stats: print_stats()
#manual()
