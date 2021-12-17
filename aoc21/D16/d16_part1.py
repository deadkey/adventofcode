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
        for start in range(0, len(s), 5):
            block = s[start: start + 5]
            db(block)
            if int(block[0]) == 0:
                return ver, t, start+5 + 6
        return None
    else:
        l = int(s[6], 2)
        db('l',l)
        if l == 0:
            L, i = extract(s, 7, 15)
            db('L', L)
            oi = i
            while i < oi + L:
                v, _, di = read(s[i:])
                ver += v
                i += di

            return ver, t, i
        else:
            L, i = extract(s, 7, 11)
            db('P', L)
            for _ in range(L):
                v, _, di = read(s[i:])
                ver += v
                i+= di

            return ver, t, i
    return None
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    binary = tobin(data[0])
    
    db(binary)
    ver, t, di = read(binary)
   

    return ver

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
