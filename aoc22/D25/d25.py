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
    #return lazy_ints(line.split())
    return lazy_ints(multisplit(line, ' ')) 

def val(d):
    L = len(d)
    cnt = 0
    power = 1
    for lt in d[::-1]:    
        if lt == '-':
            cnt -= power
        elif lt == '=':
            cnt -= 2 * power
        else:
            v = int(lt)
            cnt += v * power
        power *= 5
    return cnt

def snafu(v):
    out = []
    while v > 0:
        if v % 5 < 3:
            out.append(str(v % 5))
        elif v % 5 == 3:
            v += 5
            out.append('=')
        elif v % 5 == 4:
            v += 5
            out.append('-')
        v //= 5
    return ''.join(out[::-1])

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [line for line in lines]
    su = 0
    for i in range(len(data)):
        d = data[i]
        su += val(d)

    db(su)

    return snafu(su)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,25, p1, p2, cmds)
if stats: print_stats()

#manual()
