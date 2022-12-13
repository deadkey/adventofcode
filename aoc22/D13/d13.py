import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import functools
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
    #return lazy_ints(line.split())
    return lazy_ints(multisplit(line, ' ')) 

def compare(l, r):
    if type(l) == int and type(r) == int:
        res = l - r
        return res
    
    elif type(l) == int or type(r) == int:
        if type(l) == int:
            l = [l]
        if type(r) == int:
            r = [r]
        res = compare(l, r)
        return res
    #both lists
    for ll, rr in zip(l, r):
        res = compare(ll, rr)
        if res != 0: return res
        
    return len(l) - len(r)
    
            

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    item1= [[2]]
    item2 = [[6]]
    items = []
    for i, ch in enumerate(chunks):
        line1 = eval(ch[0])
        line2 = eval(ch[1])
        items.append(line1)
        items.append(line2)
    '''
    index1 = 1
    for item in items:
        if compare(item, item1) < 0:
            index1 += 1
    index2 = 2
    for item in items:
        if compare(item, item2) < 0:
            index2 += 1
    '''
    items.append(item1)
    items.append(item2)
    
    items = sorted(items, key=functools.cmp_to_key(compare))
    for i, item in enumerate(items):
        if item == item1:
            index1 = i +1
        if item == item2:
            index2 = i +1
        

    return index1 * index2

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i, ch in enumerate(chunks):
        line1 = eval(ch[0])
        line2 = eval(ch[1])
        
        if compare(line1, line2) < 0:
            db('index' , i + 1)
            su += i + 1

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,13, p1, p2, cmds)
if stats: print_stats()

#manual()
