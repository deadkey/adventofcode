import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def apply(line):
    out = []
    i = 0
    while i < len(line):
        j = i + 1
        while j <len(line) and line[j] == line[i]:
            j += 1
        no = j - i
        out.append(str(no))
        out.append(line[i])
        i = j
    return out

def db(*a): 
    if DB: print(*a)

def p1(v):
    line = v.strip()
    N = 40
    for i in range(N):
        line = apply(line)
    return len(line)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,  10, p1, p2, cmds)
if stats: print_stats()
#manual()
