import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#import numpy as np
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(multisplit(line, ',', 'x'))

def parse2(line):
    return lazy_ints(multisplit(line, ','))

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    earliest = int(lines[0])
    data = parse(lines[1])
    db(data)
    best = 10 ** 10, 0
    for bus in data:
        k = earliest // bus
        nxt = (k+1) * bus
        best =  min((nxt, bus) ,best)
    
    left =best[0] - earliest
    db(best, left)
    return best[1] * left

def mult(data):
    p = 1
    for v in data:
        p *= v
    return p
def gcd(a, b):return gcd(b, a % b) if b else a

# x * a + y * b = gcd(a, b). Return gcd(a, b), x, y
def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = (a // b, b, a % b)
        x0, x1 = (x1, x0 - q * x1)
        y0, y1 = (y1, y0 - q * y1)
    return (a, x0, y0)

trie

#If a list of t = a1 mod n1, t = a2 mod n2 ... Given a list of a and n, returns t 
def crt(la, ln):
    assert len(la) == len(ln)
    for i in range(len(la)):
        assert 0 <= la[i] < ln[i]
    prod = 1
    for n in ln:
        assert gcd(prod, n) == 1
        prod *= n
    lN = []
    for n in ln:
        lN.append(prod//n)
    x = 0
    for i, a in enumerate(la):
        print(lN[i], ln[i])
        _, Mi, mi = xgcd(lN[i], ln[i])
        x += a*Mi*lN[i]
    return x % prod

def p2(v):
    lines = v.strip().split('\n')
    vals = parse2(lines[1])
    N = []
    A = []
    for i, v in enumerate(vals):
        if v != 'x':
            N.append(v)
            A.append(-i % v)
    return crt(A, N)    
    

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,13, p1, p2, cmds)
if stats: print_stats()
#manual()
