import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
from collections import defaultdict as dd, Counter
from itertools import chain, combinations, permutations
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
    return lazy_ints(multisplit(line, ': ')) 

#returns order so that edges only point forward in partial order
def topsort(g):
    ps= dd(int)
    nodes = set()
    for node, ns in g.items():
        nodes.add(node)
        for n in ns:
            ps[n] += 1
    
    q =[v for v in nodes if ps[v] == 0]
    
    order = []
    
    while q:
        q2 = []
        for n in q:
            order.append(n)
            for p in g[n]:
                ps[p] -=1
                if ps[p] == 0:
                    q2.append(p)
        q =q2
    return order

def cnt_paths(order, g):
    cnt = dd(int)
    cnt['out'] = 1
    for node in order:
        c = cnt[node]
        for ns in g[node]:
            c += cnt[ns]
        cnt[node] = c
    return cnt

def cnt_paths2(order, g):
    
    cnt = {}
    for node in order:
        cnt[node] = [0, 0, 0]

    cnt['out'] = [1, 0, 0]
    
    for node in order:
        c = cnt[node]
        for ns in g[node]:
            li = cnt[ns]
            c[0] += li[0]
            c[1] += li[1]
            c[2] += li[2]
        if node in ['dac', 'fft']:
            c[2] = c[1]
            c[1] = c[0]
            c[0] = 0
        else:
            cnt[node] = c
    return cnt

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    g = {'out':[]}

    for i in range(len(data)):
        first = data[i][0]
        rest = data[i][1:]
        g[first] = rest
    
    order = topsort(g)
    
    rev = order[::-1]
    num_paths = cnt_paths(rev, g)
    
    return num_paths['you']

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    g = {'out':[]}

    for i in range(len(data)):
        first = data[i][0]
        rest = data[i][1:]
        g[first] = rest
    
    order = topsort(g)
    
    rev = order[::-1]
    num_paths = cnt_paths2(rev, g)
    db('numpaths', num_paths)

    return num_paths['svr'][-1]



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,11, p1, p2, cmds)
if stats: print_stats()

#manual()
