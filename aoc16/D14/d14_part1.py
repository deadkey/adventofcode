import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import hashlib
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())

def has3(ha):
    for i in range(len(ha)-2):
        if ha[i] == ha[i+1] == ha[i+2]:
            return True, ha[i]
    return False, -1

def has5(ha):
    all = set()
    for i in range(len(ha)-4):
        if ha[i] == ha[i+1] == ha[i+2] == ha[i+3] == ha[i+4]:
            all.add(ha[i])
    return all

def iskey(fives, active):
    all = []
    for five in fives:
            for i, ok, val in active:
                if ok and five == val:
                    all.append(i)
    return len(all) > 0, sorted(all)

def p1(v):
    lines = v.strip().split('\n')
    salt = lines[0]
    cnt = 0
    i = 0
    N = 64
    active = deque()
    i = 0
    keys = set()
 
    while len(keys) < N:
        if len(active) == 1001:
            active.popleft()
        ha = salt + str(i)
        r = hashlib.md5(ha.encode()).hexdigest()
        ok, val = has3(r)
        fives = has5(r)
        key, ind = iskey(fives, active)
        if key:
            keys |= set(ind)

            

        active.append((i, ok, val))
        i += 1
    iss = sorted(list(keys))
    return iss[63]
        

        

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,14, p1, p2, cmds)
if stats: print_stats()
#manual()
