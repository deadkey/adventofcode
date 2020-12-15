import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *

from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split(','))

INF = 10**12
def inf():
    return (-1,-1, 0)

def p1(v, N = 2020):
    lines = v.strip().split('\n')
    start = parse(lines[0])
    last = dd(inf)
    seen = start[0]
    for i, s in enumerate(start):
        last[s] = (i, -1, 1)
        seen = s
        
    k = i
    for i in range(k+1, N):
        #db('Last', seen)
        ind, prev, cnt = last[seen]
        if cnt > 1:
            seen= ind - prev
        else:
            seen = 0
            
        ind, _, cnt = last[seen]
        last[seen] = (i, ind, cnt+1)
        #db(seen , last[seen])
       
        

    return seen

def p2(v):
    return p1(v, 30000000)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,15, p1, p2, cmds)
if stats: print_stats()
#manual()
