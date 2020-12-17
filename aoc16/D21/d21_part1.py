import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *

from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())

def swap(ins, pw):
    if ins[1]== 'position':
        p1 = ins[2]
        p2 = ins[-1]
        pw[p1], pw[p2] = pw[p2], pw[p1]
        return pw
    else:
        lt1 = ins[2]
        lt2 = ins[-1]
        for i, ch in enumerate(list(pw)):
            if ch == lt1:
                pw[i] = lt2
            elif ch == lt2:
                pw[i] = lt1
            
        return pw

def rotate(ins, pw):
    le = ins[2]
    n = len(pw)
    db(ins, le)
    
    if ins[1] == 'right':
        if le == 0:
            return pw
        return pw[-le:] + pw[0:n - le]
    if ins[1] == 'left':
        if le == 0:
            return pw
        return pw[le:] + pw[0:le]
    lt = ins[-1]
    ind = pw.index(lt)
    add = (1 if ind >= 4 else 0)
    le = (1 + ind + add) % n
    db(le)
    if le == 0:
        return pw
    return pw[-le:] + pw[0:n - le]

def reverse(ins, pw):
    a = ins[2]
    b = ins[-1]
    sub = pw[a:b+1][::-1]
    return pw[0:a] + sub + pw[b+1:]

def move(ins, pw):
    fr = ins[2]
    to = ins[-1]
    rm = pw.pop(fr)
    pw.insert(to, rm)
    return pw

def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    T = 'abcdefgh'
    pw = list(T)
    data = [parse(line) for line in lines]
    for ins in data:
        op = ins[0]
        if op == 'swap':
            pw = swap(ins, pw)
        
        if op == 'rotate':
            pw = rotate(ins, pw)

        if op == 'reverse':
            pw = reverse(ins, pw)

        if op == 'move':
            pw = move(ins, pw)
        db(''.join(pw))
    return ''.join(pw)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,21, p1, p2, cmds)
if stats: print_stats()
#manual()
