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
    newvals = [(data[i], i) for i in range(len(data))]
    N = len(data)
    for oldpos in range(len(data)):
        for pos in range(N):
            if newvals[pos][1] == oldpos: break
        
        val = newvals[pos][0]
        item = newvals.pop(pos)
        index = (pos + val) % (N -1)
        newvals.insert(index, item)

    
    for pos in range(N):
        if newvals[pos][0] == 0: break

    return newvals[(pos+1000)%N][0] + newvals[(pos+2000)%N][0] + newvals[(pos+3000)%N][0]


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    V = 811589153
    T = 10
    newvals = [(data[i] * V, i) for i in range(len(data))]
    N = len(data)
    for t in range(T):
        for oldpos in range(N):
            for pos in range(N):
                if newvals[pos][1] == oldpos: break
            
            val = newvals[pos][0]
            item = newvals.pop(pos)
            index = (pos + val) % (N -1)
            newvals.insert(index, item)

            
                    #db(f'Step {step} for {val} {newvals}')
        tmp = [newvals[i][0] for i in range(N)]
        db(tmp)
        #db('Moving val=', val, 'current\n', tmp)
        
    for pos in range(N):
        if newvals[pos][0] == 0: break

    return newvals[(pos+1000)%N][0] + newvals[(pos+2000)%N][0] + newvals[(pos+3000)%N][0]



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,20, p1, p2, cmds)
if stats: print_stats()

#manual()
