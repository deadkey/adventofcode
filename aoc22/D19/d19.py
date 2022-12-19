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
    line = line.replace('and', ' ')
    return lazy_ints(multisplit(line, ':.')) 

map = {'ore': 0, 'clay': 1, 'obsidian': 2}


def canbuild(i, state, blue):
    li = [v for v in state]
    
    req = blue[i]

    for k in range(0, len(req), 2):
        no = req[k]
        t = req[k + 1]
        index = map[t]
        if li[index] >= no:
            li[index] -= no
        else:
            return False
    return True

def build(i, state, blue):
    li = [v for v in state]
    
    req = blue[i]

    for k in range(0, len(req), 2):
        no = req[k]
        t = req[k + 1]
        index = map[t]
        if li[index] >= no:
            li[index] -= no
    li[i + 3] += 1
    return li


def calc1(state, blue, dp, time):
    if time <= 0: return 0
    if state in dp: return dp[state]

    ore, clay, obs, orerob, clayrob, obsrob, georob, _ = state
    #Build robots first!
    best  = 0
    didgeod = False
    for i in range(3, -1, -1):
        if canbuild(i, state, blue):
            if i == 3: didgeod = True
            #build
            li = build(i, state, blue)
            li[0] = li[0] + orerob
            li[1] = li[1] + clayrob
            li[2] = li[2] + obsrob
            #li[3] = li[3] + georob
            li[-1] = time - 1
            nstate = tuple(li)
            alt = calc1(nstate, blue, dp, time - 1) + georob
            best = max(best, alt)
        if didgeod:
            break
    #cannot build anything
    if not didgeod:
        li = [v for v in state]
        li[0] = li[0] + orerob
        li[1] = li[1] + clayrob
        li[2] = li[2] + obsrob
        #li[3] = li[3] + georob
        li[-1] = time - 1
        nstate = tuple(li)
        alt = calc1(nstate, blue, dp, time - 1) + georob
        best = max(best, alt)

    dp[state] = best
    return best

def calc2(state, blue, dp, time):
    if time <= 0: return 0
    if state in dp: return dp[state]

    ore, clay, obs, orerob, clayrob, obsrob, georob, _ = state
    #Build robots first!
    best  = 0
    didgeod = False
    didobs = False
    for i in range(3, -1, -1):
        if canbuild(i, state, blue):
            if i == 3: didgeod = True
            if i == 2: didobs = True
            #build
            li = build(i, state, blue)
            li[0] = li[0] + orerob
            li[1] = li[1] + clayrob
            li[2] = li[2] + obsrob
            #li[3] = li[3] + georob
            li[-1] = time - 1
            nstate = tuple(li)
            alt = calc2(nstate, blue, dp, time - 1) + georob
            best = max(best, alt)
        if didgeod or didobs:
            break
    #cannot build anything
    if not didgeod and not didobs:
        li = [v for v in state]
        li[0] = li[0] + orerob
        li[1] = li[1] + clayrob
        li[2] = li[2] + obsrob
        #li[3] = li[3] + georob
        li[-1] = time - 1
        nstate = tuple(li)
        alt = calc2(nstate, blue, dp, time - 1) + georob
        best = max(best, alt)

    dp[state] = best
    return best


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    bp = []
    for i in range(len(data)):
        d = [s.split() for s in data[i]]
        vals = [lazy_ints(d[1][4:]), lazy_ints(d[2][4:]), lazy_ints(d[3][4:]), lazy_ints(d[4][4:])]
        bp.append(vals)
    best = 0
    bi = 0
    #ore, clay, obs, orerob, clayrob, obsrob, georob, _ = state
    start = 0, 0, 0, 1, 0, 0, 0, 24
    
    all = []
    for i, blue in enumerate(bp):
        db('Runing blueprint ', i+1)
        dp = {}
        #def calc(state, blue, dp, time)
        alt = calc1(start, blue, dp, 24)
        all.append(alt)
        best += alt * (i + 1)
        db('Result', i+1, alt)
    db('results', all)
    return best


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    bp = []
    for i in range(len(data)):
        d = [s.split() for s in data[i]]
        vals = [lazy_ints(d[1][4:]), lazy_ints(d[2][4:]), lazy_ints(d[3][4:]), lazy_ints(d[4][4:])]
        bp.append(vals)
    best = 1
    bi = 0
    #ore, clay, obs, orerob, clayrob, obsrob, georob, _ = state
    start = 0, 0, 0, 1, 0, 0, 0, 32
    
    all = []
    for i, blue in enumerate(bp[0:3]):
        db('Runing blueprint ', i+1)
        dp = {}
        #def calc(state, blue, dp, time)
        alt = calc2(start, blue, dp, 32)
        all.append(alt)
        best *= alt
        db('Result', i+1, alt)
    db('results', all)
    return best

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,19, p1, p2, cmds)
if stats: print_stats()

#manual()
