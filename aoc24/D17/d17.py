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
    line = removeall(line, ['Register', 'A:', 'B:', 'C:', 'Program:'])
    return lazy_ints(multisplit(line, [' ', ','])) 

def getval(val, A, B, C):
    if 0 <= val <= 3:
        return val
    if val == 4: return A
    if val == 5: return B
    if val == 6: return C
# 2,4,
# 1,2,
# 7,5,
# 1,7,
# 4,4,
# 0,3,
# 5,5,
# 3,0

def op(code, val, A, B, C, pos, out):
    
    if code == 0:
        val = getval(val, A, B, C)
        #division
        res = A//2**val
        return res, res, B, C, pos + 2
    if code == 1:
        res = B ^ val
        return res, A, res, C, pos + 2
    if code == 2:
        val = getval(val, A, B, C)
        res = val % 8
        return res, A, res, C, pos + 2
    if code == 3:
        if A == 0: return 0, A, B, C, pos + 2
        return 0, A, B, C, val
    if code == 4:
        res = B ^ C
        return res, A, res, C, pos + 2
    if code == 5:
        val = getval(val, A, B, C)
        res = val % 8
        out.append(res)
        return res, A, B, C, pos + 2
    if code == 6:
        val = getval(val, A, B, C)
        res = A//2**val
        return res, A, res, C, pos + 2
    if code == 7:
        val = getval(val, A, B, C)
        res = A//2**val
        return res, A, B, res, pos + 2
    db('FAILS')

#WRONG 190593311067057 too high

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    A = parse(chunks[0][0])
    B = parse(chunks[0][1])
    C = parse(chunks[0][2])
    program = parse(chunks[1][0])
    i = 0
    out = []
    while i < len(program):
        
        res, A, B, C, i = op(program[i], program[i+1], A, B, C, i, out)
    

    return ','.join(map(str, out))

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    A = parse(chunks[0][0])
    B = parse(chunks[0][1])
    C = parse(chunks[0][2])
    program = parse(chunks[1][0])
    i = 0
    
    startC = [0]
    cand = [c*8 + i for i in range(8) for c in startC]
    test = [0]

    while len(test) <= len(program):
        nxtcand = []
        for startval in cand:
            
            A = startval
            out = []
            i = 0
            while 0 <= i < len(program):
                res, A, B, C, i = op(program[i], program[i+1], A, B, C, i, out)
            
            if out == test:
                db('startval', startval, out)
                nxtcand.append(startval)
                
        cand = [c*8 + i for i in range(8) for c in nxtcand] 
        if len(test) != len(program): 
            test = program[-(len(test)+1):]
        else:
            break
    print(min(nxtcand))
    
    
    

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,17, p1, p2, cmds)
if stats: print_stats()

#manual()
