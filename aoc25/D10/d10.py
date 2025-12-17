import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
from z3 import *
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
    data = list(multisplit(line, ' '))
    
    ligths = list(data[0][1:-1])
    reqs = lazy_ints(data[-1][1:-1].split(','))
    buttons = [list(map(int, (x[1:-1].split(',')))) for x in data[1:-1]]
    
    return ligths, buttons, reqs

def getstate(curr, button):
    curr = list(curr)
    for b in button:
        curr[b] = '#' if curr[b] == '.' else '.'
    return ''.join(curr)

def steps(li, buttons):
    start = '.' * len(li)
    goal = ''.join(li)
    visited = set()
    visited.add(start)
    q = [start]
    steps = 0
    while q:
        steps += 1
        q2 = []
        for node in q:
            db('node', node)
            for button in buttons:
                nextstate = getstate(node, button)
                db('next', nextstate, 'with', button)
                if nextstate == goal: return steps
                if nextstate not in visited:
                    visited.add(nextstate)
                    q2.append(nextstate)
        q = q2
    return -10**10

def solve(buttons, reqs):
    
    s = Optimize()
    variables = []
    for i, b in enumerate(buttons):
        var = Int('a' + str(i))
        s.add(var >= 0)
        variables.append(var)
    for index in range(len(reqs)):
        
        c = 0
        for i, b in enumerate(buttons):
            if index in b:
                c += variables[i]
        s.add(c == reqs[index])
    tot = Int('tot')
    s.add(tot == sum(variables))
    s.minimize(tot)
    if s.check():
        m = s.model()
        return m.evaluate(tot).as_long()
        
    return -10 ** 10


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        li, buttons, reqs = data[i]
        step = steps(li, buttons)

        db('steps', step)
        su += step
    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        li, buttons, reqs = data[i]
        db(f'{i}/{len(data)}')
        step = solve(buttons, reqs)

        db('steps', step)
        su += step
    return su



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,10, p1, p2, cmds)
if stats: print_stats()

#manual()
