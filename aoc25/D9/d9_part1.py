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
    return lazy_ints(multisplit(line, ', ')) 
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    tiles = [parse(line) for line in lines]
    biggest = 0
    areas = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            dr = abs(tiles[i][0] - tiles[j][0]) + 1
            dc = abs(tiles[i][1] - tiles[j][1]) + 1
            
            area = dr * dc
            
            areas.append(area)

    return max(areas)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,9, p1, p2, cmds)
if stats: print_stats()

#manual()
