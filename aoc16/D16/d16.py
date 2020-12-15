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

def gen(a):
    b = a[::-1]
    flipb = ['1' if bit == '0' else '0' for bit in b]
    c = a + '0' + ''.join(flipb)
    return c

def pairwise(T):
    ch= []
    for s in range(0, len(T), 2):
        if T[s] == T[s+1]:
            ch.append('1')
        else:
            ch.append('0')
    return ch

def checksum(T):
    while len(T) % 2 == 0:
        T = pairwise(T)
    return ''.join(T)

def p1(v):
    lines = v.strip().split('\n')
    a = lines[0]
    L = 272
    while len(a) < L:
        a = gen(a)
    return checksum(a[0:L])



def p2(v):
    lines = v.strip().split('\n')
    a = lines[0]
    L = 35651584
    while len(a) < L:
        a = gen(a)
    db('Generated a')
    return checksum(a[0:L])


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,16, p1, p2, cmds)
if stats: print_stats()
#manual()
