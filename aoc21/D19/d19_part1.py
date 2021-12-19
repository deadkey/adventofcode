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
    return tuple(lazy_ints(line.split(',')))

def rotate(data, signs, up):
    res = []
    sx, sy, sz = signs
    for d in data:
        x, y, z = d
        xr, yr, zr = sx * x, sy * y, sz * z
        tmp = [xr, yr, zr]
        r = [0]*3
        for i in up:
            r[up[i]] = tmp[i]
        res.append(tuple(r))
    return res

def delta(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return (dx, dy, dz)
     

def overlap(points, other):
    deltas = Counter()
    for p in points:
        for po in other:
            d = delta(p, po)
            deltas[d] += 1

    for d, v in deltas.items():
        if v >= 12:
            return True, d
    return False, None
    
def add(rot, delta):
    res = []
    for r in rot:
        res.append((r[0] - delta[0], r[1] - delta[1], r[2] - delta[2]))
    return res

def findoverlap(points, scanners, all):
    for i, other in enumerate(scanners):
        for s, u in all:
            rot = rotate(other, s, u)
            no, delta = overlap(points, rot)
            if no:
                points |= set(add(rot, delta))
                return i
    return None

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    scanners = []
    for ch in chunks:
        lines = ch.split('\n')[1:]
        data = [parse(line) for line in lines]
        scanners.append(data)
    
    ups = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    signs = [[1, 1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, -1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1]]
    all = [(s, u) for s in signs for u in ups]
    points = set(scanners[0])
    scanners = scanners[1:]
    while len(scanners) > 0:
        index = findoverlap(points, scanners, all)
        scanners.pop(index)

    #for p in sorted(points):
        #print(','.join(map(str, p)))

    return len(points)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,19, p1, p2, cmds)
if stats: print_stats()
#manual()
