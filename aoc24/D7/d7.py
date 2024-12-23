import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
from collections import defaultdict as dd, Counter
from itertools import product
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
    return lazy_ints(multisplit(line, [' ', ':'])) 

def add(a, b): return a + b
def mul(a, b): return a * b
def conc(a, b): return int(str(a) + str(b))

def rec1(target, nums):
    for ops in product([add, mul], repeat = len(nums) - 1):
        acc = nums[0]
        for i in range(len(ops)):
            acc = ops[i](acc, nums[i + 1])
        if acc == target: return target
    return 0

def rec(target, nums):
    for ops in product([add, mul, conc], repeat = len(nums) - 1):
        acc = nums[0]
        for i in range(len(ops)):
            acc = ops[i](acc, nums[i + 1])
        if acc == target: return target
    return 0

def rec_test(target, nums, pos = []):
    ops = [add, mul]
    if len(nums) == 0:
        return target in pos
    pos2 = []
    n = nums[0]
    for op in ops:
        for p in pos:
            pos2.append(op(p, n))
    return rec_test(target, nums[1:], pos2)


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        if rec1(d[0], d[1:]):
            su += d[0]

    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        
        if rec(d[0], d[1:]):
            su += d[0]

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,7, p1, p2, cmds)
if stats: print_stats()

#manual()
