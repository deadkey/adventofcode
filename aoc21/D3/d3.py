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
    return line.split()[0]
    

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    N = len(data[0])
    ones = [0] * N
    zeros = [0] * N
    gamma = [0] * N
    eps = [0] * N
    for i in range(len(data)):
        v = data[i]
        #db(len(v))
        for p in range(N):
            if v[p] == '1':
                ones[p] += 1
            else:
                zeros[p] +=1
    for p in range(N):
        if ones[p] >= zeros[p]:
            gamma[p] = 1
            eps[p] = 0
        else:
            gamma[p] = 0
            eps[p] = 1
    g = ''.join(map(str, gamma))
    e = ''.join(map(str, eps))
    

        

    return int(g, 2) * int(e, 2)

def count(li, pos):
    N = len(li[0])
    ones = 0
    zeros = 0
    for v in li:
        #db(len(v))
        if v[pos] == '1':
            ones += 1
        else:
            zeros += 1
    if ones >= zeros:
        return '1'
    else:
        return '0'

def p2(v):

    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    ox = list(data)
    pos = 0
    while len(ox) > 1:
        q = []
        common = count(ox, pos)
        for val in ox:
            if val[pos] == common:
                q.append(val)
        pos += 1
        ox = q
    co = list(data)
    pos = 0
    while len(co) > 1:
        q = []
        common = count(co, pos)
        for val in co:
            if val[pos] != common:
                q.append(val)
        pos += 1
        co = q

    return int(ox[0], 2) * int(co[0], 2)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,3, p1, p2, cmds)
if stats: print_stats()
#manual()
