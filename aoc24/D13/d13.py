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
    return lazy_ints(multisplit(line, [' ',',', '+', '='])) 


def solve_manual(m):
    ax, ay, bx, by, px, py = m
    t = py*ax - ay*px
    n = by*ax - bx*ay
    if n != 0 and t % n == 0:
        k2 = t // n
        t2 = px - k2 * bx
        n2 = ax
        if n2 != 0 and t2 % n2 == 0:
            k = t2 // n2
            return 3 * k + k2
    return 0

# OK, this is smarter than my solution
import z3
def solve_z3(m):
    ax, ay, bx, by, px, py = m
    solver = z3.Solver()
    k= z3.Int('k')
    k2 = z3.Int('k2')
    solver.add(k * ax + k2 * bx == px)
    solver.add(k * ay + k2 * by == py)
    if solver.check() == z3.sat:
        model = solver.model()
        return 3 * model[k].as_long() + model[k2].as_long()

    return 0


def solve(m):
    ax, ay, bx, by, px, py = m
    alt = []
    for k in range(0, 101):
        xleft = px - k * ax
        yleft = py - k * ay
        if xleft % bx == 0:
            k2 = xleft // bx
            if k2 * by == yleft:
                alt.append(3 * k + k2)
    if len(alt) == 0: return 0
    return min(alt)
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    machines = []
    for chunk in chunks:
        a = parse(chunk[0])
        adx = a[3]
        ady = a[5]
        b = parse(chunk[1])
        bdx = b[3]
        bdy = b[5]
        price = parse(chunk[2])
        px = price[2]
        py = price[4]

        machines.append((adx, ady, bdx, bdy, px, py))
        
    
    for m in machines:
        s = solve_manual(m)
    
        su += s

    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    machines = []
    for chunk in chunks:
        a = parse(chunk[0])
        adx = a[3]
        ady = a[5]
        b = parse(chunk[1])
        bdx = b[3]
        bdy = b[5]
        price = parse(chunk[2])
        px = price[2] + 10000000000000
        py = price[4] + 10000000000000

        machines.append((adx, ady, bdx, bdy, px, py))
        
    
    for m in machines:
        s = solve_manual(m)
    
        su += s

    return su



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,13, p1, p2, cmds)
if stats: print_stats()

#manual()
