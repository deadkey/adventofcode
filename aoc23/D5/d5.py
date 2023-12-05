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
    return lazy_ints(multisplit(line, ' ')) 
    
def overlap(s1, e1, s2, e2):
    return s1 <= s2 < e1 or s2 <= s1 < e2

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)

    seeds = parse(chunks[0][0].split(':')[-1])
    maps = dd(map)
    order = []
    curr = seeds[0::2]
    curr_range = seeds[1::2]
    curr = list(zip(curr, curr_range))


    for m in chunks[1:]:
        t = m[0]
        ranges1 = m[1:]
        name = t.split()[0]
        f, _, to = name.split('-')
        #maps[(f, to)]
        order.append((f, to))
        used = set()
        nxt = []
        ranges = []
        for r in ranges1:    
            dest, source, w = map(int, r.split())
            ranges.append((source, dest, w))
        ranges.sort()

        nxt = []

        for s, l in curr:
            prev = s

            e = s + l
            for start, dest, w in ranges:
                endr = start + w
                if overlap(s, e, start, endr):
                    newstart = max(s, start)
                    newend = min(e, endr)
                    if newstart - prev: nxt.append((prev,  newstart - prev))

                    L = newend - newstart
                    diff = newstart - start
                    deststart = dest + diff
                    nxt.append((deststart, L))
                    prev = newend

            if prev != e:
                L = e - prev
                nxt.append((prev, L))

        curr = nxt

    return min(curr)[0]

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)

    seeds = parse(chunks[0][0].split(':')[-1])
    maps = dd(map)
    order = []
    curr = seeds

    for m in chunks[1:]:
        t = m[0]
        ranges = m[1:]
        name = t.split()[0]
        f, _, to = name.split('-')
        #maps[(f, to)]
        order.append((f, to))
        used = set()
        nxt = []
        for r in ranges:
            
            dest, source, w = map(int, r.split())
            for s in curr:
                if source <= s <= source + w:
                    diff = s - source
                    target= dest + diff
                    nxt.append(target)
                    used.add(s)
        for c in curr:
            if c not in used:
                nxt.append(c)
        curr = nxt



    return min(curr)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,5, p1, p2, cmds)
if stats: print_stats()

#manual()
