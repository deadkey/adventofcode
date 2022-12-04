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
    #return lazy_ints(multisplit(line, '')) 
    #return lazy_ints(line.split())
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    winning = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    same = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    points = {'X':1, 'Y': 2, 'Z':3}
    for i in range(len(data)):
        a, x = data[i]
        better = winning[a]
        if same[a] == x:
            su += points[x] + 3
        elif better == x:
            su += points[x]
        else:
            #I won
            su += points[x] + 6
            
    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    winning = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    same = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    points = {'X':1, 'Y': 2, 'Z':3}
    for i in range(len(data)):
        a, res = data[i]
        if res == 'X':
            x = winning[a]
            su += points[x]
        elif res == 'Y':
            x= same[a]
            su += points[x] + 3
        else:
            #I won
            for ch in ['X', 'Y', 'Z']:
                if ch != same[a] and ch != winning[a]:
                    x = ch
            su += points[x] + 6



    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,2, p1, p2, cmds)
if stats: print_stats()

#manual()
