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
    return line.split('-')

def bfs2(start, end, g, small):
    visited = set()
    visited.add(start)
    q = [([start], 0)]

    while q:
        q2 = []
        for path, dup in q:
            db(path)
            for nxt in g[path[-1]]:
                du = dup
                if nxt in small and nxt in path: 
                    if dup == 1: continue
                    if nxt == start or nxt == end: continue
                    du = 1

                newpath = list(path) + [nxt]
                s = ','.join(newpath)
                if s not in visited:
                    visited.add(s)
                    q2.append((newpath, du))
        q = q2
    cnt = 0
    db(visited)
    for path in visited:
        if path.endswith('end'):
            cnt += 1
    return cnt

def bfs(start, end, g, small):
    visited = set()
    visited.add(start)
    q = [[start]]
    while q:
        q2 = []
        for path in q:
            for nxt in g[path[-1]]:
                if nxt in small and nxt in path: continue

                newpath = list(path) + [nxt]
                s = ','.join(newpath)
                if s not in visited:
                    visited.add(s)
                    q2.append(newpath)
        q = q2
    cnt = 0
    db(visited)
    for path in visited:
        if path.endswith('end'):
            cnt += 1
    return cnt


def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    g = dd(list)
    for i in range(len(data)):
        a, b = data[i]
        g[a].append(b)
        g[b].append(a)
    start = 'start'
    end = 'end'
    small = set()
    for k in g.keys():
        if k.islower():
            small.add(k)
    return bfs(start, end, g, small)


def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    g = dd(list)
    for i in range(len(data)):
        a, b = data[i]
        g[a].append(b)
        g[b].append(a)
    start = 'start'
    end = 'end'
    small = set()
    for k in g.keys():
        if k.islower():
            small.add(k)
            
    return bfs2(start, end, g, small)




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,12, p1, p2, cmds)
if stats: print_stats()
#manual()
