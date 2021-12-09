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
    return lazy_ints(list(line.split()[0]))


def bfs(q, g, R, C):
    visited = set()

    for node in q:
        visited.add(node)
    while q:
        q2 = []
        for node in q:
            row, col = node
            nb = get4nb(row, col, 0, R, 0, C)
            for r, c in nb:
                if (r, c) not in visited and g[r][c] < 9:

                    visited.add((r, c))
                    q2.append((r, c))
        q = q2
    return visited

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 0
    R = len(data)
    C = len(data[0])
    for row in range(len(data)):
        rowdata = data[row]
        for col in range(len(rowdata)):
            nb = get4nb(row, col, 0, R, 0, C)
            vals = []
            for r, c in nb:
                vals.append(data[r][c])
            mn = min(vals)
            if mn > data[row][col]:
                su += 1 + data[row][col]
    return su

def p2(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 0
    db(data)
    R = len(data)
    C = len(data[0])
    lowpoints = []
    for row in range(len(data)):
        rowdata = data[row]
        for col in range(len(rowdata)):
            nb = get4nb(row, col, 0, R, 0, C)
            vals = []
            for r, c in nb:
                vals.append(data[r][c])
            mn = min(vals)
            if mn > data[row][col]:
                su += 1 + data[row][col]
                lowpoints.append((data[row][col], row, col))
    
    vislen = []
    #seen = set()
    lowpoints.sort()
    for low in lowpoints:
        vis = bfs([(low[1], low[2])], data, R, C)
        #seen = seen | vis
        vislen.append(len(vis))
    vislen.sort(reverse = True)
    return vislen[0] * vislen[1] * vislen[2]


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,9, p1, p2, cmds)
if stats: print_stats()
#manual()
