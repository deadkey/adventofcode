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


def merge(holes, fi):
    files = deque(fi)
    db(files)
    m = []
    db(holes)
    c = 0
    for i, a in enumerate(holes):
        if a == -1:
            db('hole')
            if len(files) == 0:
                return m
            k = files.pop()
            c += 1
            m.append(k)
            
        else:
            if len(files) == 0:
                return m
            _ = files.popleft()
            m.append(a)

    return m

def best(size, a):
    ss = []
    for s in range(a, 10):
        if len(size[s]) > 0:
            ss.append((size[s][0], s))
    ss.sort()
    if len(ss) == 0:
        return []
    return ss


def fill(holes, block, size):
    m = []
    for i, a, index in block[::-1]:
        cand = best(size, a)
        if len(cand) == 0:
            continue
        idx, s = cand.pop(0)
        if idx > index:
            continue
        for k in range(a):
            holes[idx + k] = i
            holes[index + k] = -1
        
        size[s].pop(0)
        #new hole
        s = s - a
        if s > 0:
            size[s].append(idx + a)
            size[s].sort()
    return holes
    
# WRONG 8573601415879
def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    data =[int(x) for x in str(data[0])]
    
    fi = []
    holes = []
    idx = 0
    block = []
    size = [[] for s in range(10)]
    index = 0
    for i, a in enumerate(data):
        if i % 2 == 0:
            #file
            block.append((idx, a, index))
            for k in range(a):
                holes.append(idx)
                fi.append(idx)
            idx += 1
            index += a
        else:
            #free
            size[a].append(index)
            for k in range(a):
                holes.append(-1)
            index += a
    
    db('holes', holes)
    #m = merge(holes, fi)
    m = fill(holes, block, size)
    db('m', m)
    for i, a in enumerate(m):
        if a != -1:
            su += a * i
    su += 0

    return su

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    data =[int(x) for x in str(data[0])]
    
    fi = []
    holes = []
    idx = 0
    for i, a in enumerate(data):
        if i % 2 == 0:
            #file
            
            for k in range(a):
                holes.append(idx)
                fi.append(idx)
            idx += 1
        else:
            #free
            for k in range(a):
                holes.append(-1)
    
    db('fi', fi)
    m = merge(holes, fi)
    for i, a in enumerate(m):
        su += a * i
    su += 0

    return su



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,9, p1, p2, cmds)
if stats: print_stats()

#manual()
