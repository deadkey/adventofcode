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
    return lazy_ints(line.split('-'))
    
# Failed 753114. too low. 
def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    N = 4294967295
    data = [parse(line) for line in lines]
    ints = [(0, N)]

    for i, (a, b) in enumerate(data):
        newints = []
        for s, e in ints:
            if e < a or s > b:
                newints.append((s, e))
            else:
                if a <= s <= b and a <= e <= b:
                    #inside
                    continue
                elif s < a and a <= e <= b:
                    newints.append((s, a-1))
                elif a <= s <= b and e > b:
                    newints.append((b+1, e))
                elif s < a and e > b:
                    newints.append((s, a-1))
                    newints.append((b+1, e))
        ints = newints
        #db(ints)
                    
                
    lo = 10**12
    for s, e in ints:
        lo = min(lo, s)
    return lo
    

def p2(v):
    lines = v.strip().split('\n')
    N = 4294967295
    data = [parse(line) for line in lines]
    ints = [(0, N)]

    for i, (a, b) in enumerate(data):
        newints = []
        for s, e in ints:
            if e < a or s > b:
                newints.append((s, e))
            else:
                if a <= s <= b and a <= e <= b:
                    #inside
                    continue
                elif s < a and a <= e <= b:
                    newints.append((s, a-1))
                elif a <= s <= b and e > b:
                    newints.append((b+1, e))
                elif s < a and e > b:
                    newints.append((s, a-1))
                    newints.append((b+1, e))
        ints = newints
        #db(ints)


    cnt = 0                             
    for s, e in ints:
        cnt += (e -  s +1)
    return cnt

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,20, p1, p2, cmds)
if stats: print_stats()
#manual()
