import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
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


def findkey(pu, N):
    S = pu
    s = 1
    MOD = 20201227

    for n in range(N):
        s *= S
        s %= MOD
        #db(n, s)
    return s

def findloop(pu, S):
    s = 1
    MOD = 20201227
    loop_sz = 0
    while True:
        s *= S
        s %= MOD

        loop_sz += 1
        #db(s, loop_sz)
        if s == pu:
            return loop_sz
        
        


def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    pu_card = data[0]
    pu_door = data[1]
    
    loop_card = findloop(pu_card, 7)
    loop_door = findloop(pu_door, 7)
    

    return findkey(pu_door, loop_card)

def p2(v):
    pass


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,25, p1, p2, cmds)
if stats: print_stats()
#manual()
