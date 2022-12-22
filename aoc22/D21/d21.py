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
    return lazy_ints(multisplit(line, ' :')) 

#returns order so that edges only point forward in partial order
def topsort(g, all):
    ps= Counter()
    for node in all:
        for n in g[node]:
            ps[n] += 1
    q =[]
    for node in all:
        if ps[node] == 0:
            q.append(node)
    order = []
    while q:
        q2 = []
        for n in q:
            order.append(n)
            for p in g[n]:
                ps[p] -=1
                if ps[p] == 0:
                    q2.append(p)
        q =q2
    return order[::-1]

def ev(op, a, b):
    if op == '+': return a + b
    if op == '*': return a * b
    if op == '-': return a - b
    if op == '/': return a / b

def reva(op, res, b):
    if op == '+': return res - b
    if op == '*': return res /b
    if op == '-': return res + b
    if op == '/': return res * b


def revb(op, res, a):

    if op == '+': return res - a
    if op == '*': return res /a
    if op == '-': return a - res
    if op == '/': return a / res

def test(order, g, wrongtree, guess, oper, orig):
    vals = {}
    node = 'root'
    a, b = g[node]
    if a in orig:
        other = b
    if b in orig:
        other = a
    

    for node in orig.keys():
        vals[node] = orig[node]

    vals['humn'] = guess

    for node in order:
        if node in wrongtree and node != 'root':
            if node in oper:
                a, b = g[node]
                val = ev(oper[node], vals[a], vals[b])
                vals[node] = val
    
    return vals[other]


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    g = dd(list)
    oper = {}
    vals= dd(int)
    all = set()
    for i in range(len(data)):
        if len(data[i]) > 2:
            parent, a, op, b = data[i]
            
            db(parent, a, op, b)
            g[parent].append(a)
            g[parent].append(b)
            oper[parent] = op
            all.add(parent)
            all.add(a)
            all.add(b)
        else:
            node, val = data[i]
            db(node, val)
            vals[node] = val
            g[node] = []
            all.add(node)
            

    order = topsort(g,all)
    #db('order', order)
    for node in order:
        if node in oper:
            a, b = g[node]
            val = ev(oper[node], vals[a], vals[b])
            vals[node] = val
        

    return int(vals['root'])


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    g = dd(list)
    oper = {}
    vals= {}
    all = set()
    pars = {}
    for i in range(len(data)):
        if len(data[i]) > 2:
            parent, a, op, b = data[i]
            
            #db(parent, a, op, b)
            g[parent].append(a)
            g[parent].append(b)
            oper[parent] = op
            all.add(parent)
            all.add(a)
            all.add(b)
            pars[a] = parent
            pars[b] = parent
        else:
            node, val = data[i]
            #db(node, val)
            vals[node] = val
            g[node] = []
            all.add(node)
            

    order = topsort(g,all)
    #db('order', order)
    wrongtree = set()
    node = 'humn'
    while node != 'root':
        wrongtree.add(node)
        node = pars[node]
    #db('wrong', wrongtree)
    
    for node in order:
        if node not in wrongtree and node != 'root':
            if node in oper:
                a, b = g[node]
                val = ev(oper[node], vals[a], vals[b])
                vals[node] = val
    
    node = 'root'
    a, b = g[node]
    if a in vals:
        db('Val a', vals[a])
        target = vals[a]
    if b in vals:
        db('Val b', vals[b])
        target = vals[b]
    '''
    hi = 10**20
    lo = 0

    #return 'Fail'

    best = -1
    for _ in range(400):
        guess = (lo + hi) // 2
        res = test(order, g, wrongtree, guess, oper, vals)
        #db('Guess', guess, 'res', res, 'target', target)
        if res > target:
            lo = guess + 1
        if res == target:
            hi = guess
            best = guess
        if res < target:
            hi = guess -1


    for v in range(best - 100, best + 100):
        res = test(order, g, wrongtree, v, oper, vals)
        if res == target: db('Good guess', v, 'res', res, 'target', target)
        
    '''
    pushed = {}
    other = a if a not in vals else b
    pushed[other] = target
    
    del vals['humn']

    for node in order[::-1]:
        if node in wrongtree:
            target = pushed[node]
            #db('node', node, 'target', target)
            if node in oper:
                op = oper[node]
                a, b, = g[node]
                #db('target', target)
                if a in vals:

                    val = revb(op, target, vals[a])
                    pushed[b] = val

                    #db('target', target, 'op', op, 'a', vals[a], 'b res', val)
                if b in vals:
                    val = reva(op, target, vals[b])
                    pushed[a] = val

                    #db('target', target, 'op', op, 'a res', val, 'b', vals[b])
                
                
                
    

    return int(pushed['humn'])





def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,21, p1, p2, cmds)
if stats: print_stats()

#manual()
