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
   

    while len(fire) > 0:
        fire2 = []
        for conn in fire:
            for o in outputs[conn]:
                if allset(o, values):
                    v = getval(o, values)
                    values[o] = v
                    fire2.append(o)
        
        fire = fire2
    
    li = []
    for k, v in values.items():
        if k[0] == 'z':
            li.append((k, v))
    li = sorted(li)
    res = [x[1] for x in li]
    return list(res[::-1])

def sim2(start, conns):
    
    values = {}
    for name, v in start:
        values[name] = v
   
    changed = True
    while changed:
        changed = False
        for conn in conns:
            a, b, op, res = conn
            if a in values and b in values and res not in values:
                changed = True
                if op == 'AND':
                    values[res] = values[a] and values[b]
                if op == 'OR':
                    values[res] = values[a] or values[b]
                if op == 'XOR':
                    values[res] = values[a] ^ values[b]
        
        
    
    li = []
    for k, v in values.items():
        if k[0] == 'z':
            li.append((k, v))
    li = sorted(li)
    res = [x[1] for x in li]
    return list(res[::-1])



def firstfail(xs, ys, zs,conns):
    start = xs + ys
    res = sim2(start,conns)
    res = list(res[::-1])
    for i in range(len(res)):
        if res[i] != zs[i][1]:
            return i
    return len(res)
    
def bintoint(xs):
    vals = []
    for name, v in xs:
        vals.append(v)
    vals = list(vals[::-1])
    return int(''.join(map(str, vals)), 2)

def inttobin(c):
    c = bin(c)[2:]
    c = '0'*(46 - len(c)) + c
    c = c[::-1]
    names = []
    for i in range(len(c)):
        name = str(i)
        if len(name) == 1:
            name = '0' + name
        name = 'z' + name
        names.append([name, int(c[i])])
    return names                    

def test(start, conns, xs, ys, zs):
    #generate a list of random 45 bit numbers
    import random

    
    

    def improve(best, conns):
        for i in range(len(conns)):
            for k in range(len(conns)):
                conns2 = conns.copy()
                a, b, op, res = conns[i]
                a2, b2, op2, res2 = conns[k]
                conns2[i] = (a, b, op, res2)
                conns2[k] = (a2, b2, op2, res)
                fails = []

                for _ in range(30):
                    xs2 = [[x[0], random.randint(0, 1)] for x in xs]
                    ys2 = [[y[0], random.randint(0, 1)] for y in ys]
                    

                    a = bintoint(xs2)
                    b = bintoint(ys2)
                    c = a + b
                    zs = inttobin(c)
                    ff = firstfail(xs2, ys2, zs, conns2)            
                    fails.append(ff)
                    if ff <= best:
                        break
                ff = min(fails)
                db(ff, best, res, res2, f'{i*len(conns) + k}/{len(conns)**2}')

                if ff > best:

                    return conns2, ff, res, res2
    
    best = 9
    swaps = []
    for i in range(4):
        conns, best2, r1, r2 = improve(best, conns)
        assert best2 > best, 'Best2 is not better than best'
        best = best2
        swaps.append(r1)
        swaps.append(r2)
    s = sorted(swaps)
    db(s)
    return ','.join(s) 



def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    start = [parse(line) for line in chunks[0]]
    
    conns =  [parse2(line) for line in chunks[1]]

    su = 0
    inputs = dd(list)
    ops = {}
    outputs = dd(list)
    connections = []
    
    for a, op, b, res in conns:
        inputs[res]= [a, b]
        ops[res] = op
        outputs[a].append(res)
        outputs[b].append(res)
        connections.append((a, b, op, res))


    x = []
    y = []
    z = set()
    for name, v in start:
        if name[0] == 'x':
            x.append((name, v))
        if name[0] == 'y':
            y.append((name, v))
        if name[0] == 'z':
            z.append((name, v))
    for name, _ in inputs.items():
        if name[0] == 'z':
            z.add(name)
    xs = sorted(x)
    ys = sorted(y)
    zs = sorted(z)

   
    return test(start, connections, xs, ys, zs)
    #val = sim(start, inputs, outputs, ops)
    #changes = test(start, inputs, outputs, ops)
    #su = int(''.join(map(str, val)), 2)


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
