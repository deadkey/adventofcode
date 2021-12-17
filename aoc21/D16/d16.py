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
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())

def tobin(line):
    MAP = {'0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'
    }

    out= []
    for lt in line:
        out.append(MAP[lt])
    return ''.join(out)

def extract(s, i, L):
    return int(s[i:i+L], 2), i + L

def calc(t, vals):
    if t == 0: return sum(vals)
    if t == 1: 
        p = 1
        for v in vals:
            p *= v
        return p
    if t == 2: return min(vals)
    if t == 3: return max(vals)
    if t == 5:return int(vals[0] > vals[1])
    if t == 6:return int(vals[0] < vals[1])
    if t == 7:return int(vals[0] == vals[1])
    

def read(s):
    db(s)

    ver = s[0:3]
    ver = int(ver, 2)
    t = s[3:6]
    t = int(t, 2)
    db('t', t)
    if t == 4:
        s = s[6:]
        #literal, do something else
        out = []
        for start in range(0, len(s), 5):
            block = s[start: start + 5]
            db(block)

            out.append(block[1:])
            if int(block[0]) == 0:
                tmp= ''.join(out)
                val = int(tmp, 2)
                return ver, val, start+5 + 6
            
        return None
    else:
        l = int(s[6], 2)
        db('l',l)
        vals = []
        if l == 0:
            L, i = extract(s, 7, 15)
            db('L', L)
            oi = i
            while i < oi + L:
                v, val, di = read(s[i:])
                ver += v
                i += di
                vals.append(val)

            return ver, calc(t, vals), i
        else:
            L, i = extract(s, 7, 11)
            db('P', L)
            for _ in range(L):
                v, val, di = read(s[i:])
                ver += v
                i+= di
                vals.append(val)

            return ver, calc(t, vals), i
    return None
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    binary = tobin(data[0])
    
    db(binary)
    ver, val, di = read(binary)
   

    return val

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,16, p1, p2, cmds)
if stats: print_stats()
#manual()
