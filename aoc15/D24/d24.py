import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import numpy as np
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
from itertools import combinations 
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return int(line)

def div(others, target):
    wt = [0]
    for no in range(1, len(others)+1):
        i = no -1
        wc = others[i]
        for w in list(wt):
            #db(w, wc)
            wt.append(w+wc)
            if w+ wc == target:
                #db(no, wt)
                return True
    return False

def mult(li):
    su = 1
    for i in li: su *= i
    return su

def solve(vals):
    su = sum(vals)
    target = su//3
    ok = False
    best = mult(vals)
    db(f'Best {best}')
    for no in range(1, len(vals)):
        comb = combinations(vals, no)
        
        for c in list(comb):
            if sum(c) != target: continue
            others = []
            #db(c)
            for v in vals:
                if v not in c:
                    others.append(v)
            #db(f'Others {others}')
            if div(others, target):
                #db(c)
                ent = mult(c)
                best = min(best, ent)
                ok = True
        db(no)
        if ok:
            break
    return best


def div2(others, target):
    wt = [set([0]), set([0])]
    for no in range(1, len(others)+1):
        i = no -1
        wc = others[i]
        for side in range(len(wt)):
            otherside = wt[(side + 1)%2]
            for w in list(wt[side]):
                #db(w, wc)
                wt[side].add(w+wc)
                if w+wc == target and target in otherside:
                    return True
                    
    return False

def solve2(vals):
    su = sum(vals)
    target = su//4
    ok = False
    best = mult(vals)
    db(f'Best {best}')
    for no in range(1, len(vals)):
        comb = combinations(vals, no)
        
        for c in list(comb):
            if sum(c) != target: continue
            others = []
            #db(c)
            for v in vals:
                if v not in c:
                    others.append(v)
            #db(f'Others {others}')
            if div2(others, target):
                #db(c)
                ent = mult(c)
                best = min(best, ent)
                ok = True
        db(no)
        if ok:
            break
    return best


def p1(v):
    lines = v.strip().split('\n')
    vals = [parse(line) for line in lines]
    
    return solve(vals)

def p2(v):
    lines = v.strip().split('\n')
    vals = [parse(line) for line in lines]
    
    return solve2(vals)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,24, p1, p2, cmds)
if stats: print_stats()
#manual()
