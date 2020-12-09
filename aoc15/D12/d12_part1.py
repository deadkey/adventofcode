import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph only works for python3!
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def p1(v):
    lines = v.strip().split('\n')
    filtered = []
    cnt = 0
    for line in lines:
        for ch in line:
            if ch.isdigit() or ch == '-':
                filtered.append(ch)
            else:
                filtered.append(' ')
    newstr = ''.join(filtered)
    no = lazy_ints(newstr.split())
    
    return sum(no)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,12, p1, p2, cmds)
if stats: print_stats()
#manual()
