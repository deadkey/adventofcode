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
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line =line.replace('[', ' ').replace(']', ' ').replace('=', ' ')
    return lazy_ints(line.split())

def apply(val ,mask):
    bval = bin(val)[2:]
    db(bval, len(mask), len(bval))
    bval = '0' * (len(mask) - len(bval)) + bval
    db('bval ', bval)
    out = []
    for i, b in enumerate(mask):
        if b == 'X': 
            out.append(bval[i])
        else: out.append(mask[i])
    return int(''.join(out), 2)  

def p1(v):
    lines = v.strip().split('\n')
    mask = lines[0].split('=')[-1]
    
    db(mask)
    cnt = 0
    data = [parse(line) for line in lines[1:]]
    db(data)
    mem = defaultdict(int)
    for i, line in enumerate(data):
        if len(line) < 3:
            db(i, line)
            mask = line[-1]
            db('mask', mask)
        else:
            _, m, val = line
            mem[m] = apply(val, mask)
    su = 0
    for key, val in mem.items():
        su += val
    return su

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,14, p1, p2, cmds)
if stats: print_stats()
#manual()
