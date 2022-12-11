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
    return lazy_ints(multisplit(line, ' ')) 

def oper(op, old, val):
    if op == '+':
        return old + val
    if op == '*':
        return old * val
    if op == '-':
        return old - val
    if op == '**':
        return old ** val
   
    


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    monkeys = []
    for i, c in enumerate(chunks):
        c[1] = c[1].replace(',', '')
        items = parse(c[1])[2:]
        #db(items)
        op = parse(c[2])[-2]
        val = parse(c[2])[-1]
        div = parse(c[3])[-1]
        tr = parse(c[4])[-1]
        fa =parse(c[5])[-1]
        monkeys.append((items, op, val, div, tr, fa))
        

    N = 10000
    MOD = 1

    for i in range(len(monkeys)):
        items, op, val, div, tr, fa = monkeys[i]
        MOD *= div

    cnt = Counter()
    for round in range(N):
        for i in range(len(monkeys)):
            items, op, val, div, tr, fa = monkeys[i]
            #inspect
            for it in items:
                cnt[i] += 1
                
                nn = oper(op, it, val)
                nn = nn % MOD
                if nn % div == 0:
                    monkeys[tr][0].append(nn)
                else:
                    monkeys[fa][0].append(nn)
            monkeys[i] = [], op, val, div, tr, fa
                
    vals = list(cnt.values())
    vals.sort()




    return vals[-2] * vals[-1]

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    monkeys = []
    for i, c in enumerate(chunks):
        c[1] = c[1].replace(',', '')
        items = parse(c[1])[2:]
        #db(items)
        op = parse(c[2])[-2]
        val = parse(c[2])[-1]
        div = parse(c[3])[-1]
        tr = parse(c[4])[-1]
        fa =parse(c[5])[-1]
        monkeys.append((items, op, val, div, tr, fa))
        

    N = 20
    cnt = Counter()
    for round in range(N):
        for i in range(len(monkeys)):
            items, op, val, div, tr, fa = monkeys[i]
            #inspect
            for it in items:
                cnt[i] += 1
                
                nn = oper(op, it, val)
                nn = nn// 3
                db('throw', i, tr, fa, 'item', it)
                if nn % div == 0:
                    monkeys[tr][0].append(nn)
                else:
                    monkeys[fa][0].append(nn)
            monkeys[i] = [], op, val, div, tr, fa
                
    vals = list(cnt.values())
    vals.sort()

    return vals[-2] * vals[-1]


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,11, p1, p2, cmds)
if stats: print_stats()

#manual()
