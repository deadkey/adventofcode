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
    #return lazy_ints(multisplit(line, '')) 
    return lazy_ints(line.split())

def inall(ch, allset):
    for s in allset:
        if ch not in s: return False
    return True

def prio(ch):
    if ch.islower():
        return ord(ch) - ord('a') + 1
    else:
        return ord(ch) - ord('A') + 27

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        k = len(d)//2
        first = set(d[0:k])
        second = set(d[k:])
        common = first & second
        
        su += sum([prio(ch) for ch in common])


    return su


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(0, len(data), 3):
        first = set(data[i])
        second = set(data[i+1])
        third = set(data[i + 2])
        common = first & second & third
        
        su += sum([prio(ch) for ch in common])


    return su




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,3, p1, p2, cmds)
if stats: print_stats()

#manual()
