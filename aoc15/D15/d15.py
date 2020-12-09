import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line = removeall(line, ':', ',')
    data = lazy_ints(line.split())
    name = data[0]
    cap = data[2]
    dur = data[4]
    flav = data[6]
    text = data[8]
    cal = data[-1]
    return name, cap, dur, flav, text, cal


def score(vals, ing):

    res = [0] * 4
    for k in range(4):
        for i in range(len(ing)): 
            res[k] += vals[i] * ing[i][k+1]
    alt = 1
    for r in res:
        alt *= max(r, 0)
    return alt

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    ing = [parse(line) for line in lines]
    N = 100
    best = 0
    C = 500

    for a in range(N):
        
        for b in range(N-a+1):
            for c in range(N-a-b+1):
                d = N - a - b - c
                vals = [a, b, c, d]
                alt = score(vals, ing)
                best = max(alt, best)


    return best

def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    ing = [parse(line) for line in lines]
    N = 100
    best = 0
    C = 500

    for a in range(N):
        
        for b in range(N-a+1):
            for c in range(N-a-b+1):
                d = N - a - b - c
                vals = [a, b, c, d]
                cals = sum(vals[i] * ing[i][-1] for i in range(len(ing)))
                if cals != C: continue
                
                alt = score(vals, ing)
                best = max(alt, best)


    return best


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,15, p1, p2, cmds)
if stats: print_stats()
#manual()
