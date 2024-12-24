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
    return lazy_ints(multisplit(line, ':')) 

def parse2(line):
    return lazy_ints(multisplit(line, ['->', ' '])) 
    
def sim(start, inputs, outputs, ops):

    def allset(o, values):
       
        for i in inputs[o]:
            if i not in values:
                
                return False
      
        return True

    def getval(o, values):
        op = ops[o]
        vals = []
        for i in inputs[o]:
            vals.append(values[i])
        
        if op == 'AND':
            return vals[0] and vals[1]
        if op == 'OR':
            return vals[0] or vals[1]
        if op == 'XOR':
            return vals[0] ^ vals[1]
        

    fire = [s[0] for s in start]
    values = {}
    for name, v in start:
        values[name] = v
    db('fire', fire)
    db('outputs', outputs)

    while len(fire) > 0:
        fire2 = []
        for conn in fire:
            for o in outputs[conn]:
                if allset(o, values):
                    v = getval(o, values)
                    values[o] = v
                    fire2.append(o)
        db('fire2', fire2)
        fire = fire2
    
    db(values)
    li = []
    for k, v in values.items():
        if k[0] == 'z':
            li.append((k, v))
    li = sorted(li)
    res = [x[1] for x in li]
    return list(res[::-1])


    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    start = [parse(line) for line in chunks[0]]
    db(start)
    conns =  [parse2(line) for line in chunks[1]]

    su = 0
    inputs = dd(list)
    ops = {}
    outputs = dd(list)
    for a, op, b, res in conns:
        inputs[res]= [a, b]
        ops[res] = op
        outputs[a].append(res)
        outputs[b].append(res)

    val = sim(start, inputs, outputs, ops)
    su = int(''.join(map(str, val)), 2)

    return su

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,24, p1, p2, cmds)
if stats: print_stats()

#manual()
