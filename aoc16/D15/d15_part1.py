import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line = removeall(line, 'Disc #', 'has', 'positions; at time=0, it is at position ', '.')
    return lazy_ints(line.split())

def gcd(a, b):return gcd(b, a % b) if b else a

# x * a + y * b = gcd(a, b). Return gcd(a, b), x, y
def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = (a // b, b, a % b)
        x0, x1 = (x1, x0 - q * x1)
        y0, y1 = (y1, y0 - q * y1)
    return (a, x0, y0)



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

def p1(v):
    lines = v.strip().split('\n')
    
    vals = [parse(line) for line in lines]
    la = []
    ln = []
    for ai, ni, si in vals:
        la.append(-(ai + si)%ni)
        ln.append(ni)

    return crt(la, ln)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,15, p1, p2, cmds)
if stats: print_stats()
#manual()
