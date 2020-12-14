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
    return line.split()

def tobin(val, mask):
    bval = bin(int(val))[2:]
    bval = '0' * (len(mask) - len(bval)) + bval
    return bval

def apply(bval ,mask):
    out = []
    db('bval', bval)
    for i, b in enumerate(mask):
        if b == '0': 
            out.append(bval[i])
        elif b == '1':
            out.append('1')
        else: out.append(mask[i])
    db('out', ''.join(out))
    return ''.join(out)  

def apply1(val ,mask):
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
            mem[m] = apply1(val, mask)
    su = 0
    for key, val in mem.items():
        su += val
    return su
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
            bval = tobin(val)
            assert len(bval) == 32
            mem[m] = apply(bval, mask)
    su = 0
    for key, val in mem.items():
        su += val
    return su

def SU(val):
    bs = []
    alt = [0]
    for i, bit in enumerate(val[::-1]):
        bv = 2 ** i
        if bit == 'X':
            for a in list(alt):
                alt.append(bv + a)
        elif bit == '1':
            
            newalt = [bv + a for a in alt]
            alt = newalt
    db(val)
    db(alt)            

    return alt

def p2(v):
    lines = v.strip().split('\n')
    mask = lines[0].split('=')[-1].strip()
    
    #db(mask)
    cnt = 0
    data = [parse(line) for line in lines[1:]]
    #db(data)
    mem = defaultdict(int)
    for i, line in enumerate(data):
        if len(line) < 3:
            db(i, line)
            mask = line[-1].strip()
            db('mask', mask)
        else:
            _, m, val = line
            val = int(val)
            bval = tobin(val, mask)
            bm = tobin(m, mask)
            am = apply(bm, mask)

            for s in SU(am):
                mem[s] = val
    su = 0
    for key, val in mem.items():
        su += val
    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,14, p1, p2, cmds)
if stats: print_stats()
#manual()
