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
    #return lazy_ints(line.split())
    data = line.split(':')
    wins, my = data[1].split('|')
    return lazy_ints(multisplit(wins, ' ')), lazy_ints(multisplit(my, ' ')) 
    

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    cnt = Counter()
    for i in range(len(data)):
        cnt[i] = 1

    for i in range(len(data)):
        wins, my = data[i]
        w = set(wins)
        m = set(my)
        overlap = len(w & m)
        num = cnt[i]
        if overlap >= 1:

            for n in range(overlap):
                cnt[i + 1 + n] += num

    return sum(cnt.values())

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        wins, my = data[i]
        w = set(wins)
        m = set(my)
        overlap = len(w & m)
        if overlap >= 1:
            p = 2 ** (overlap -1)
            su += p

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,4, p1, p2, cmds)
if stats: print_stats()

#manual()
