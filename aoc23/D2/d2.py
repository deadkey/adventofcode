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
    #return lazy_ints(line.split())
    line = line.replace('Game', '').split(':')[1:]
    return lazy_ints(multisplit(line[-1], ' ,;'))
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    MAX = {'red': 12, 'green': 13, 'blue': 14}
    imp = set()
    for i in range(len(data)):
        d = data[i]
        
        for n, c in zip(d[::2], d[1::2]):
            if n > MAX[c]:
                imp.add(i)
        
        if i not in imp:
            su += i +1
        


    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    MAX = {'red': 12, 'green': 13, 'blue': 14}
    imp = set()
    for i in range(len(data)):
        d = data[i]
        
        game = {'red': 0, 'green': 0, 'blue': 0}
        for n, c in zip(d[::2], d[1::2]):
            game[c] = max(game[c], n)
        
        p = 1
        for v in game.values():
            p *= v
        su += p

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,2, p1, p2, cmds)
if stats: print_stats()

#manual()
