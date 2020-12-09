import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from itertools import permutations

#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def score(li, vals):
    su = 0
    for i in range(len(li)):
        other = (i + 1) % len(li)
        su += vals[li[i], li[other]]
        su += vals[li[other], li[i]]
    return su

def parse(line):
    data = line.split()
    name = data[0]
    sign = -1 if data[2] == 'lose' else 1
    pts = int(data[3])
    other = data[-1][0:-1]
    return name, sign * pts, other    

def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    vals = {}
    names = set()
    for line in lines:
        name, pts, other = parse(line)
        vals[name, other] = pts
        names.add(name)
        #db(name, pts, other)
    me = 'me'
    names.add(me)
    names = list(names)
    for name in names:
        vals[name, me] = 0
        vals[me, name] = 0
    best = 0
    for li in permutations(names):
        alt = score(li, vals)
        best = max(best, alt)
    return best


def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    vals = {}
    names = set()
    for line in lines:
        name, pts, other = parse(line)
        vals[name, other] = pts
        names.add(name)
        #db(name, pts, other)
    names = list(names)
    best = 0
    for li in permutations(names):
        alt = score(li, vals)
        best = max(best, alt)
    return best

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,13, p1, p2, cmds)
if stats: print_stats()
#manual()
