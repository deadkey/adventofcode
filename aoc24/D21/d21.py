import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
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
    return lazy_ints(multisplit(line, ' ')) 

NUMPAD = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['#', '0', 'A']]
NUMPOS = {}
for r in range(len(NUMPAD)):
    for c in range(len(NUMPAD[r])):
        NUMPOS[NUMPAD[r][c]] = (r, c)

DIRPAD = [['#', '^', 'A'], ['<', 'v', '>']]
DIRPOS = {}
for r in range(len(DIRPAD)):
    for c in range(len(DIRPAD[r])):
        DIRPOS[DIRPAD[r][c]] = (r, c)

def oknum(path, start, target):
    r, c = start
    for p in path:
        if p == '^':
            r -= 1
        if p == 'v':
            r += 1
        if p == '>':
            c += 1
        if p == '<':
            c -= 1
        try:
            if NUMPAD[r][c] == '#':
                return False
        except:
            db('Error #', start, target, path)
            exit()
    return True

def okdir(path, start, target):
    r, c = start
    for p in path:
        if p == '^':
            r -= 1
        if p == 'v':
            r += 1
        if p == '>':
            c += 1
        if p == '<':
            c -= 1
        try:
            if DIRPAD[r][c] == '#':
                return False
        except:
            db('Error #', start, target, path)
            exit()
    return True

def getPaths(start, target):
    r, c = start
    br, bc = target
    dr, dc = br - r, bc - c
    path1 = []
    if dr < 0:
        path1.extend(['^'] * abs(dr))
    if dr > 0:
        path1.extend(['v'] * abs(dr))
    if dc < 0:
        path1.extend(['<'] * abs(dc))
    if dc > 0:
        path1.extend(['>'] * abs(dc))
    
    path2 = []
    if dc < 0:
        path2.extend(['<'] * abs(dc))
    if dc > 0:
        path2.extend(['>'] * abs(dc))
    if dr < 0:
        path2.extend(['^'] * abs(dr))
    if dr > 0:
        path2.extend(['v'] * abs(dr))
    return [path1, path2]


def getnum(d, totlevels = 26):
    #all = allpathsnum()
    
    curr = 'A'
    score = 0
    for digit in d:
        cost = costrec(NUMPOS[curr], NUMPOS[digit], 0, totlevels)
        score += cost
        curr = digit

    return score


'''    
def cost3(start, end):
    return 1

def cost2(start, end):
    paths = getPaths(start, end)
    best = 10**18
    for path in paths:
        if not okdir(path, start, end): continue
        last = DIRPOS['A']
        score = 0
        for p in path:
            score += cost3(last, DIRPOS[p])
            last = DIRPOS[p]
        score += cost3(last, DIRPOS['A'])
        if score < best:
            best = score
    return best

def cost1(start, end):
    paths = getPaths(start, end)
    best = 10**18
    for path in paths:
        if not okdir(path, start, end): continue
        last = DIRPOS['A']
        score = 0
        for p in path:
            score += cost2(last, DIRPOS[p])
            last = DIRPOS[p]
        score += cost2(last, DIRPOS['A'])
        if score < best:
            best = score
    return best    

def cost0(start, end):
    paths = getPaths(start, end)
    best = 10**18
    for path in paths:
        if not oknum(path, start, end): continue
        last = DIRPOS['A']
        score = 0
        for p in path:
            score += cost1(last, DIRPOS[p])
            last = DIRPOS[p]
        score += cost1(last, DIRPOS['A'])
        if score < best:
            best = score
    return best    
'''
DP = {}
def costrec(start, end, level, totlevels = 26):
    if (start, end, level) in DP:
        return DP[start, end, level]
    
    if level == totlevels: return 1

    paths = getPaths(start, end)
    best = 10**18
    for path in paths:
        if level == 0 and not oknum(path, start, end): continue
        if level > 0 and not okdir(path, start, end): continue
        last = DIRPOS['A']
        score = 0
        for p in path:
            score += costrec(last, DIRPOS[p], level+1, totlevels)
            last = DIRPOS[p]
        score += costrec(last, DIRPOS['A'], level+1, totlevels)
        if score < best:
            best = score
    DP[start, end, level] = best
    return best   


def p1(v):
    global DP
    DP = {}
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    codes = [list(parse(line)) for line in lines]
    
    # return -1
    su = 0

    for i in range(len(codes)):
        d = codes[i]
        score = getnum(d, totlevels = 3)
        
        value = int(''.join(d[0:-1]))
        db('Values',  score,  value)

        su += score * value

    return su

def p2(v):
    global DP
    DP = {}
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    codes = [list(parse(line)) for line in lines]
    
    # return -1
    su = 0
    for i in range(len(codes)):
        d = codes[i]
        score = getnum(d, totlevels = 26)
        
        value = int(''.join(d[0:-1]))
        db('Values',  score,  value)

        su += score * value

    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,21, p1, p2, cmds)
if stats: print_stats()

#manual()
