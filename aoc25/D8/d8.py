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
    return lazy_ints(multisplit(line, ', ')) 

def dist(n1, n2):
    sq = 0
    for i in range(3):
        diff = n1[i] - n2[i]
        sq += diff **2
    return sq ** 0.5

def get_dist(nodes):
    edges = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            n1 = nodes[i]
            n2 = nodes[j]
            d = dist(n1, n2)
            edges.append((d, i, j))
    return edges    


def bfs(start, g):
    visited = set()
    
    visited.add(start)
    q = [start]
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
        q = q2
    return visited

def p1(v):
    
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    nodes = [parse(line) for line in lines]
    su = 0
    distances = sorted(get_dist(nodes))
    X = 1000 if len(nodes) > 100 else 10
    edges = distances[0:X]
    g = dd(list)
    for d, a, b in edges:
        g[a].append(b)
        g[b].append(a)
    comp = []
    seen = set()
    for i in range(len(nodes)):
        if i not in seen:
            c = bfs(i, g)
            seen = seen | c
            comp.append(len(c))
    comp = sorted(comp, reverse = True)
    #48880 That's not the right answer; your answer is too low.
    return comp[0] * comp[1] * comp[2]

parents = {}
size = dd(lambda: 1)

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def add(a_parent, b_parent):

    size[b_parent] += size[a_parent]
    parents[b_parent] = b_parent
    parents[a_parent] = b_parent

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
        return False

    if size[a_parent] < size[b_parent]:
        add(a_parent, b_parent)

    else:
        add(b_parent,a_parent)

    return True

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    nodes = [parse(line) for line in lines]
    for i in range(len(nodes)):
        parents[i] = i
    distances = sorted(get_dist(nodes), reverse = True)
    merge_cnt = 0
    while merge_cnt < len(nodes) -1:
        d, a, b = distances.pop()
        merged = union(a, b)
        if merged: merge_cnt += 1
        if merge_cnt == len(nodes) -1:
            return nodes[a][0] * nodes[b][0]
    return -1


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,8, p1, p2, cmds)
if stats: print_stats()

#manual()
