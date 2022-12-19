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
    return lazy_ints(multisplit(line, ' ,')) 

def cnt(cube, cubes):
    x, y, z = cube
    alt = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    c = 0
    for dx, dy, dz in alt:
        xx, yy, zz = x + dx, y + dy, z + dz
        c += cubes[xx, yy, zz]
    return 6 - c

def sign(v):
    if v == 0: return 0
    return int(v/abs(v))

def nxt(cube, all):
    x, y, z = cube
    alt = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    c = 0
    li = []
    for dx, dy, dz in alt:
        xx, yy, zz = x + dx, y + dy, z + dz
        
        li.append((xx, yy, zz))
        
    return li

def inside(cube, limits):
    for i in range(3):
        v = cube[i]
        mn, mx = limits[i]
        if v < mn or v > mx: return False
    return True

def bfs(q, all, limits):
    visited = set()
    tot =  0
    for node in q:
        visited.add(node)
    while q:
        q2 = []
        for node in q:
            for ne in nxt(node, all):
                if ne in all:
                    tot += 1
                elif ne not in visited and inside(ne, limits):
                    visited.add(ne)
                    q2.append(ne)
        q = q2
    return tot


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    cubes = dd(int)
    all = set()
    
    for i in range(len(data)):
        x, y, z = data[i]
        cubes[(x, y, z)] = 1
        all.add((x, y, z))
    sides = 0
    tot = 6 * len(all)
    for cube in all:
        sides += cnt(cube, cubes)
    

    return tot - sides


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    cubes = dd(int)
    all = set()
    X = set()
    Y = set()
    Z = set()

    for i in range(len(data)):
        x, y, z = data[i]
        cubes[(x, y, z)] = 1
        all.add((x, y, z))
        X.add(x)
        Y.add(y)
        Z.add(z)

    sides = 0
    mx = max(X) + 1
    my = max(Y) + 1
    mz = max(Z) + 1
    mix = min(X) -1
    miy = min(Y) -1
    miz = min(Z) -1
    return bfs([(mx, my, mz)], all, [[mix, mx], [miy, my], [miz, mz]])


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,18, p1, p2, cmds)
if stats: print_stats()

#manual()
