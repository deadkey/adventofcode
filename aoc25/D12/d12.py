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
    W, H, S = lazy_ints(multisplit(line, 'x:'))
    s = lazy_ints(multisplit(S, ' ')) 
    return (W, H), s

def trivial(W, H, S, shapes):
    total = sum(S)
    can_fit_W = W //3
    can_fit_H = H//3
    can_fit = can_fit_W * can_fit_H
    return total <= can_fit

def area(shape):
    c = 0
    for row in shape:
        for col in row:
            if col == '#': c += 1
    return c

def obv_not(W, H, S, shapes):
    tot_space = 0
    for i, v in enumerate(S):
        tot_space += v * area(shapes[i])
    return tot_space > W * H

def p1(v):
    chunks = tochunks(v)
    shapes = []
    for chunk in chunks[0:-1]:
        shapes.append(chunk[1:])
    qu = [parse(line) for line in chunks[-1]]
    su = 0
    ob_not = 0
    db('Len Q', len(qu))
    for (W, H), S in qu:
        if trivial(W, H, S, shapes):
            su += 1
        elif obv_not(W, H, S, shapes):
            ob_not += 1
        else:
            db('FUUUCK', W, H, S)
    
    db('Obv not', ob_not)
    return su

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,12, p1, p2, cmds)
if stats: print_stats()

#manual()
