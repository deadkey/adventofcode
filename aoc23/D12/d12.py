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
    return lazy_ints(multisplit(line, ' ,')) 

def cnt(li):
    
    sp = li[0]
    arr = li[1:]
    
    sp = '?'.join([sp] *5)
    db(sp)
    arr = arr * 5

    ################
    DP = {}
    def lentest(test, seg):
        return len(test) == seg and test.count('.') == 0
    def checkend(pos, seg):
        if pos + seg < len(sp):
            return sp[pos + seg] != '#'
        return True

    def dp(pos, nxt):
        #done
        if nxt == len(arr):
            return 0 if sp[pos:].count('#') > 0 else 1
        
        #fail
        if pos >= len(sp):
            return 0
        
        if (pos, nxt) in DP:
            return DP[pos, nxt]
        
        if sp[pos] == '.':
            res = dp(pos + 1, nxt)
            DP[pos, nxt] = res
            return res

        if sp[pos] == '#':
            seg = arr[nxt]
            test = sp[pos:pos+seg]
            alt1 = 0
            if lentest(test, seg) and checkend(pos, seg):
                alt1 = dp(pos+seg+1, nxt + 1)
            DP[pos, nxt] = alt1
        

        if sp[pos] == '?':
            #to .
            alt1 = dp(pos+1, nxt)
            alt2 = 0
            # to #
            seg = arr[nxt]
            test = sp[pos:pos+seg]
            if lentest(test, seg) and checkend(pos, seg):
                alt2 = dp(pos+seg+1, nxt + 1)
            DP[pos, nxt] = alt1 + alt2

        return DP[pos, nxt]       


    return dp(0, 0)

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0

    for i in range(len(data)):
        d = data[i]
        a = cnt(d)
        su += a

    return su

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

if not so: run(2023,12, p1, p2, cmds)
if stats: print_stats()

#manual()
