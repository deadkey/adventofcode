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
    return lazy_ints(multisplit(line, ' ')) 

def gen(d):
    s = d
    for i in range(2000):
        res = s * 64
        s = s ^ res
        s %= 16777216
        
        res = s//32
        s = s ^ res
        s %= 16777216
        
        res = s * 2048
        s = s ^ res
        s %= 16777216
        
        
    return s

def gen2(d):
    seqs = {}
    s = d
    li = []
    for i in range(2000):
        prev = s % 10

        res = s * 64
        s = s ^ res
        s %= 16777216
        
        res = s//32
        s = s ^ res
        s %= 16777216
        
        res = s * 2048
        s = s ^ res
        s %= 16777216
        

        diff = (s%10) - prev

        li.append(diff)
        if len(li) > 4:
            li = li[1:]
        if len(li) == 4:
            if not tuple(li) in seqs:
                seqs[tuple(li)] = (s %10)
    
    return seqs



def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    cnt = Counter()
    for d in data:
        seq = gen2(d)
        for k, v in seq.items():
            cnt[k] += v

    return max(cnt.values())

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for d in data:
        r = gen(d)
        su += r

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,22, p1, p2, cmds)
if stats: print_stats()

#manual()
