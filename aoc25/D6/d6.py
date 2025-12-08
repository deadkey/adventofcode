import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
from collections import defaultdict as dd, Counter
from itertools import chain, combinations, permutations
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

def mult(vals):
    p = 1
    for v in vals:
        p *= v
    return p   

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    rows = [parse(line) for line in lines]
    su = 0
    for c in range(len(rows[0])):
        op = rows[-1][c]
        vals = []
        for r in range(len(rows)-1):
            vals.append(rows[r][c])
        if op == '+': su += sum(vals)  
        if op == '*': su += mult(vals)
    return su

def apply(op, vals):

    if op == '+': return sum(vals)  
    if op == '*': return mult(vals)

def p2(v):
    lines = v.split('\n')
    rows = [list(line) for line in lines]
    su = 0
    grid = togrid(rows[0:-1])
    ops = lines[-1].split()
    R, C = len(grid), len(grid[0])
    values = []
    for col in range(C-1, -1, -1):
        curr = 0
        ws = 0
        for row in range(R):
            if grid[row][col] == ' ': ws += 1
            else:
                value = int(grid[row][col])
                curr *= 10
                curr += value
        if ws == R:
            op = ops.pop()
            db('Apply', op, 'values', values)
            su += apply(op, values)
            values = []
        else:
            values.append(curr)

    su += apply(ops.pop(), values)

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,6, p1, p2, cmds)
if stats: print_stats()

#manual()
