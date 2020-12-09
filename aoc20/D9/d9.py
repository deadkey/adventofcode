import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line.split()
    pass

def check(li, i, val, n):
    for no in range(i - n, i -1):
        #db(li[no])
        for no2 in range(no, i):
            if li[no] + li[no2] == val:
                return True
    return False

def check2(li, i, val):
    su = 0
    used = []
    for j in range(i-1, -1, -1):
        su += li[j]
        used.append(li[j])
        if su == val:
            db(used)
            return True, min(used), max(used)
        if su > val:
            return False, 0, 0
    return False, 0, 0 


def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    P = 25
    vals = [int(v) for v in lines]
    db(vals)
    pream = vals[0:P]
    rest = vals[P:]
    for i in range(P, len(vals)):
        if not check(vals, i, vals[i], P):
            return vals[i]
    
    return cnt

def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    P = 25
    INV = 1639024365
    
    vals = [int(v) for v in lines]
    for i in range(0, len(vals)):
        ok, a, b = check2(vals, i, INV)
        db('Checking ', vals[i])
        if ok:
            return a + b
    
    return cnt


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(get_year(),  get_day(), p1, p2, cmds)
if stats: print_stats()
#manual()
