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

    return list(multisplit(line, '=() ,'))


def walk(fr, m, lr, ends):
    curr = fr
    steps = 0
    z =[]
    for _ in range(1000):
        for i, ins in enumerate(lr):
            if ins == 'L':
                inx = 0
            else:
                inx = 1
            curr = m[curr][inx]
            steps += 1
            if curr in ends:
                z.append(steps)
    return z
  

def gcd(a, b):return gcd(b, a % b) if b else a

def lcm(a, b): return a*b//gcd(a,b)

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    lr = chunks[0][0]
    data = [parse(li) for li in chunks[1]]
    m = {}
    su = 0
    for i in range(len(data)):
        fr, l, r = data[i]
        m[fr] = (l, r)

    start = [node for node in m.keys() if node[-1] == 'A']
    ends = set([node for node in m.keys() if node[-1] == 'Z'])
    
    A = []
    b = []
    for s in start:
        z = walk(s, m, lr, ends)
        #db('start = '+ str(s) + ' z ' +  str(z))
        e = z[-1000:]
        diffs = []
        for i in range(len(e) -1):
            diffs.append(e[i+1] - e[i])
        A.append(e[-1])
        b.append(diffs[-1])
        db(' ')
        db(e)
        db(diffs)
    
    prod = b[0]
    for d in b[1:]:
        prod = lcm(prod, d)

    return prod


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    lr = chunks[0][0]
    data = [parse(li) for li in chunks[1]]
    m = {}
    su = 0
    for i in range(len(data)):
        fr, l, r = data[i]
        m[fr] = (l, r)

    curr = 'AAA'
    steps = 0
    while 1:
        for i, ins in enumerate(lr):
            if ins == 'L':
                inx = 0
            else:
                inx = 1
            curr = m[curr][inx]
            steps += 1
            if curr == 'ZZZ':
                return steps
            

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,8, p1, p2, cmds)
if stats: print_stats()

#manual()
