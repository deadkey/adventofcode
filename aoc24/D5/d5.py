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


def check2(nb, rules):
    changed2 = True
    changed = False
    while changed2:
        changed2 = False
        for first, second in rules:
            i1 = 0
            i2 = 10**30
            for i in range(len(nb)):
                if nb[i] == first:
                    i1 = i
                    
                if nb[i] == second:
                    i2 = i
            if i1 > i2: 
                changed = True
                changed2 = True
                nb[i1], nb[i2] = nb[i2], nb[i1]
                break
                
        
    return changed, nb

def check(nb, rules):
    first = 0
    for first, second in rules:
        i1 = 0
        i2 = 10**30
        for i in range(len(nb)):
            if nb[i] == first:
                i1 = i
                
            if nb[i] == second:
                i2 = i
        if i1 > i2: return False
    
    return True

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    rules = []
    for line in chunks[0]:
        line = line.split('|')
        rule = int(line[0]), int(line[1])
        rules.append(rule)
        
    su = 0
    for up in chunks[1]:
        up = up.split(',')
        nb = [int(x) for x in up]
        mid = len(nb)//2
        if check(nb, rules):
            
            su += nb[mid]
        su += 0
    return su


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    rules = []
    for line in chunks[0]:
        line = line.split('|')
        rule = int(line[0]), int(line[1])
        rules.append(rule)
        
    su = 0
    for i, up in enumerate(chunks[1]):
        up = up.split(',')
        nb = [int(x) for x in up]
        mid = len(nb)//2
        changed, new = check2(nb, rules)
        if changed:
            su += new[mid]
        su += 0

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,5, p1, p2, cmds)
if stats: print_stats()

#manual()
