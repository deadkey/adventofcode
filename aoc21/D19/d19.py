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

def findoverlap(points, left, rotations):
    for i in left:
        for rot in rotations[i]:
            no, delta = overlap(points, rot)
            if no:
                points |= set(add(rot, delta))
                return i, delta
    return None, None

def dists(a, b):
    man = 0
    for i in range(3):
        man += abs(a[i] - b[i])
    return man

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
    left = set([i for i in range(1, len(scanners))])
    diffs = []
    rotations = [[] for _ in range(len(scanners))]
    for s, u in all:
        for i, scan in enumerate(scanners[1:]):
            rot = rotate(scan, s, u)
            rotations[i+1].append(rot)

    while len(left) > 0:
        index, delta = findoverlap(points, left, rotations)
        left.discard(index)
        diffs.append(delta)

    

    return len(points)

def p2(v):
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
    left = set([i for i in range(1, len(scanners))])
    diffs = []
    rotations = [[] for _ in range(len(scanners))]
    for s, u in all:
        for i, scan in enumerate(scanners[1:]):
            rot = rotate(scan, s, u)
            rotations[i+1].append(rot)

    while len(left) > 0:
        index, delta = findoverlap(points, left, rotations)
        left.discard(index)
        diffs.append(delta)

    best = 0
    for a in diffs:
        for b in diffs:
            alt = dists(a, b)
            best = max(best, alt)

    return best


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,19, p1, p2, cmds)
if stats: print_stats()
#manual()
