import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a):
    if DB: print(*a)

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    ins = []
    cnt = 0

    for line in lines:
        i, val = lazy_ints(line.split())
        ins.append((i, val))
    used = [False] * len(ins)
    db(ins)
    accu = 0
    cont = True
    curr = 0
    while cont:
        i, val = ins[curr]
        if used[curr]:
            return accu
        used[curr] = True
        db(i, val)
        if i == 'acc':
            accu += val
            curr += 1
        elif i == 'jmp':
            curr += val
        elif i == 'nop':
            curr += 1
        

    
    return cnt

def helper(ins):
    used = [False] * len(ins)
    accu = 0
    cont = True
    db(ins)
    curr = 0
    while cont:
        i, val = ins[curr]
        if used[curr]:
            return False, 0
        used[curr] = True
        if i == 'acc':
            accu += val
            curr += 1
        elif i == 'jmp':
            curr += val
        elif i == 'nop':
            curr += 1
        if curr >= len(ins):
            return True, accu
    
    return False, 0   

def p2(v):

    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    ins = []
    cnt = 0

    for line in lines:
        i, val = lazy_ints(line.split())
        ins.append((i, val))
    

    for index, (i, val) in enumerate(ins):
        db(ins, i)
        if i == 'jmp':
            iins = list(ins)
            iins[index] = ('nop', val)
        
            test, acc = helper(iins)
            if test:
                return acc
        if i == 'nop':
            iins = list(ins)
            iins[index] = ('jmp', val)
        
            test, acc = helper(iins)
            if test:
                return acc
        
    return -999



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
    



cmds, stats, io, so, DB = get_args(sys.argv)    
#if not io: run_samples(p1, p2, cmds)
#if not so: run(get_year(),  get_day(), p1, p2, cmds)
#if stats: print_stats()
manual()
