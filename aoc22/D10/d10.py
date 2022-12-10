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
    return lazy_ints(multisplit(line, ' ')) 

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    cycle = 0
    X = 1
    for i in range(len(data)):
        cmd = data[i]
        if data[i] != 'noop':
            cmd, s = data[i]

        if cmd == 'noop':
            cycle += 1
            if cycle == 20 or (cycle - 20) % 40 == 0 and cycle <= 220:
                su += (X * cycle)
                
        if cmd == 'addx':
            for c in range(2):
                cycle += 1
                if cycle == 20 or (cycle - 20) % 40 == 0 and cycle <= 220:
                    su += (X * cycle)
            X += s

    return su    

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    cycle = 0
    X = 1
    li = []
    for i in range(len(data)):
        cmd = data[i]
        if data[i] != 'noop':
            cmd, s = data[i]
        if cmd == 'noop':
           
            pos = cycle % 40
            if X - 1 <= pos <= X + 1:
                li.append('#')
            else:
                li.append(' ') 
            
            cycle += 1

                
        if cmd == 'addx':

            for c in range(2):

                pos = cycle % 40
                if X - 1 <= pos <= X + 1:
                    li.append('#')
                else:
                    li.append(' ')
                
                cycle += 1

            X += s

    rows = []
    for start in range(0, len(li), 40):
        sub = li[start: start+40]
        rows.append(''.join(sub))
    print('\n'.join(rows))


            
        
                
    db(X)
    return su



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,10, p1, p2, cmds)
if stats: print_stats()

#manual()
