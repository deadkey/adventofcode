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
    return lazy_ints(line.split())

def get9(r, c, img):
    diff = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    nb = []
    bin = []
    for dr, dc in diff:
            lt = img[r+dr, c + dc]
            nb.append((r+dr, c + dc))
            bin.append('1' if lt == 1 else '0')
    s = ''.join(bin)
    return int(s, 2), nb      


def printdict(grid):
    INF = 10**12
    minx = min(grid.keys())[0]
    maxx = max(grid.keys())[0]
    
    miny = min(grid.keys(), key = lambda x: x[1])[1]
    maxy = max(grid.keys(), key = lambda x: x[1])[1]
   
    for x in range(minx, maxx + 1):
        out = []
        for y in range(miny, maxy + 1):   
            p = '#' if grid[x, y] == 1 else ' '
            out.append(p) 
        print(''.join(out))

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    trans = chunks[0]
   
    imgorig = togrid(chunks[1].split('\n'))
    img = dd(int)
    
    
    for r in range(len(imgorig)):
        for c in range(len(imgorig[0])):
            img[r, c] = 1 if imgorig[r][c] == '#' else '0'
    
    N = 2
    
    for i in range(N):
        if i%2 == 0:
            nxt = dd(lambda: 1)
        else:
            nxt = dd(lambda: 0)
        toinc = set(img.keys())
        L = len(toinc)
        for (r, c), v in list(img.items()):
            val, nb = get9(r, c, img)
            toinc |= set(nb)
        
        for r, c in toinc:
            val, nb = get9(r, c, img)
            lt = 1 if trans[val] == '#' else 0
            nxt[r, c] = lt
        
        img = nxt
    #printdict(img)              

    return sum(img.values())

def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    trans = chunks[0]
   
    imgorig = togrid(chunks[1].split('\n'))
    img = dd(int)
    
    
    for r in range(len(imgorig)):
        for c in range(len(imgorig[0])):
            img[r, c] = 1 if imgorig[r][c] == '#' else '0'
    
    N = 50
    
    for i in range(N):
        if i%2 == 0:
            nxt = dd(lambda: 1)
        else:
            nxt = dd(lambda: 0)
        toinc = set(img.keys())
        L = len(toinc)
        for (r, c), v in list(img.items()):
            val, nb = get9(r, c, img)
            toinc |= set(nb)
       
        for r, c in toinc:
            val, nb = get9(r, c, img)
            lt = 1 if trans[val] == '#' else 0
            nxt[r, c] = lt
        
        img = nxt
    #printdict(img)              

    return sum(img.values())


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,20, p1, p2, cmds)
if stats: print_stats()
#manual()
