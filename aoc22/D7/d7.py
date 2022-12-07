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
    
def toname(dir):
    return ' '.join(dir)

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    dir = ['/']
    folders = dd(list)
    parent = {}
    cnt = dd(int)
    all = set()
    all.add('/')
    parent['/'] = ''
    cnt['/'] = 0
    
    # FEL 1444547
    for i in range(len(data)):
        line = data[i]
        if line[0] == '$':
            cmd = line[1]
            if cmd == 'cd':
                t = line[2]
                if t == '..':
                    dir.pop()
                elif t == '/':
                    dir = dir[0:1]
                else:
                    parentname = toname(dir)
                    dir.append(t)
                    tname = toname(dir)

                    parent[tname] = parentname
                    all.add(tname)
                    cnt[parentname] += 1
                    

            elif cmd == 'ls':
                pass
        else:

            curr = toname(dir)
            sz, name = line
            folders[curr].append((sz, name))
        
    
    order = topsort(parent, cnt, all)
    sizes = {}
    su = 0
    for f in order:
        s = 0
        for a, b in folders[f]:
            if a == 'dir':

                aname = f + ' ' + b
                s += sizes[aname]
            else:
                s += int(a)
        sizes[f] = s
    N = 100000
    for n, s in sizes.items():
        if s <= N:
            su += s
    
    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    dir = ['/']
    folders = dd(list)
    parent = {}
    cnt = dd(int)
    all = set()
    all.add('/')
    parent['/'] = ''
    cnt['/'] = 0
    
    for i in range(len(data)):
        line = data[i]
        db(line)
        if line[0] == '$':
            cmd = line[1]
            if cmd == 'cd':
                t = line[2]
                if t == '..':
                    dir.pop()
                elif t == '/':
                    dir = dir[0:1]
                else:
                    parentname = toname(dir)
                    dir.append(t)
                    tname = toname(dir)

                    parent[tname] = parentname
                    all.add(tname)
                    cnt[parentname] += 1
                    

            elif cmd == 'ls':
                pass
        else:

            curr = ' '.join(dir)
            sz, name = line
            folders[curr].append((sz, name))
        
    
    order = topsort(parent, cnt, all)
    sizes = {}
    su = 0
    for f in order:
        s = 0
        for a, b in folders[f]:
            if a == 'dir':

                aname = f + ' ' + b
                s += sizes[aname]
            else:
                s += int(a)
        sizes[f] = s
    N = 30000000
    su = sizes['/']
    tot = 70000000
    missing = N - (tot - su)
    
    best = 10 ** 30
    for n, s in sizes.items():
        if s > missing:
            best = min(s, best)
    return best

#returns order so that edges only point forward in partial order
def topsort(parent, cnt, all):
    q = []
    for n in all:
        if cnt[n] == 0:
            q.append(n)
    order = []
    while q:
        q2 = []
        for n in q:
            order.append(n)
            p = parent[n]
            cnt[p] -=1
            if cnt[p] == 0:
                q2.append(p)
        q =q2
    return order



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,7, p1, p2, cmds)
if stats: print_stats()

#manual()
