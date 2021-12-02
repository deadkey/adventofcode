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
    

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    x, y = 0, 0
    for i in range(len(data)):
        a, b = data[i]
        if a == 'forward':
            x += b
        elif a == 'down':
            y += b
        elif a == 'up':
            y -= b

    return x * y

def p2(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    x, y = 0, 0
    aim = 0
    for i in range(len(data)):
        a, b = data[i]
        if a == 'forward':
            x += b
            y += aim * b
        elif a == 'down':
            aim += b
        elif a == 'up':
            aim -= b

    return x * y


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,2, p1, p2, cmds)
if stats: print_stats()
#manual()
