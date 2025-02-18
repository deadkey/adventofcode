import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
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

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    stones = data[0]
    
    for i in range(25):
        nxt = []
        for stone in stones:
            if stone == 0:
                nxt.append(1)
            elif len(str(stone)) %2 == 0:
                s = str(stone)
                a, b = s[:len(s)//2], s[len(s)//2:]
                
                a = int(a)
                b = int(b)
                nxt.append(a)
                nxt.append(b)
            else:
                nxt.append(stone*2024)
        stones = nxt   
    return len(stones) 

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    stones = Counter(data[0])

    
    for i in range(75):
        nxt = Counter()
        for stone, cnt in stones.items():
            if stone == 0:
                nxt[1] += cnt
            elif len(str(stone)) %2 == 0:
                s = str(stone)
                a, b = s[:len(s)//2], s[len(s)//2:]
                
                a = int(a)
                b = int(b)
                nxt[a] += cnt
                nxt[b] += cnt
            else:
                nxt[stone*2024] += cnt
        stones = nxt
        #db(stones)

    return sum(stones.values())




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,11, p1, p2, cmds)
if stats: print_stats()

#manual()
