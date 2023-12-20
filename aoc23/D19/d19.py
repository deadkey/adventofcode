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
    for a in '\{\},':
        line = line.replace(a, ' ')

    return lazy_ints(multisplit(line, ' ')) 


def parse2(line):
    for a in '\{\},= ':
        line = line.replace(a, ' ')

    return lazy_ints(multisplit(line, ' ')) 

def test(op, var, val):
    if op == '>' and var > val:
        return True
    if op == '<' and var < val:
        return True
    return False

def app(part, arules):
    x, m, a, s = part
    for alt in arules:
        if type(alt) != tuple:
            return alt
        else:
            cond, op, val, goto = alt
            if cond ==  'x':
               if test(op, x, val): return goto
            if cond ==  'm':
               if test(op, m, val): return goto
            if cond ==  'a':
               if test(op, a, val): return goto
            if cond ==  's':
               if test(op, s, val): return goto
    assert False

def score(ii):
    xr, mr, ar, sr = ii
    return (xr[1] - xr[0] + 1) * (mr[1] - mr[0] + 1) * (ar[1] - ar[0] + 1) * (sr[1] - sr[0] + 1)

def sim(part, rules):
    curr = 'in'
    while curr != 'A' and curr != 'R':
        arules = rules[curr]
        curr = app(part, arules)
    return curr == 'A'

def intsplit(ii, val, op):
    lo, hi = ii
    if op == '<':
        if lo < val:
            i1 = lo, min(val -1, hi)
            if lo <= val <= hi:
                i2 = val, hi
            else:
                i2 = []
            return i1, i2
    if hi > val:
        i1 = max(lo, val + 1), hi
        if lo <= val <= hi:
            i2 = lo, val
        else:
            i2 = []
        return i1, i2
    

def split(left, rule):
    xr, mr, ar, sr = left
    if type(rule) != tuple:
        return left, [], rule
    else:
        cond, op, val, goto = rule
        if cond ==  'x':
            xin, xout = intsplit(left[0], val, op)
            inside = xin,  mr, ar, sr
            left = xout,  mr, ar, sr
            
        if cond ==  'm':

            mn, mout = intsplit(left[1], val, op)
            inside = xr,  mn, ar, sr
            left = xr,  mout, ar, sr
        if cond ==  'a':

            ain, aout = intsplit(left[2], val, op)
            inside = xr,  mr, ain, sr
            left = xr,  mr, aout, sr
        if cond ==  's':

            sin, sout = intsplit(left[3], val, op)
            inside = xr,  mr, ar, sin
            left = xr,  mr, ar, sout
        return inside, left, goto


def app2(left, rules, curr):
    ans = 0
    arules = rules[curr]
    
    for rule in arules:
        ok, left, goto = split(left, rule)
        ans2 = 0
        if goto == 'A':
            ans += score(ok)
        elif goto == 'R':
            pass
        else:
            ans2 = app2(ok, rules, goto)
        ans += ans2


    return ans

def sim2(xr, mr, ar, sr, rules):
    curr = 'in'
    ii = (xr, mr, ar, sr)
    return app2(ii, rules, curr)
    
    


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    rules = {}
    bw = dd(list)
    coord = dd(list)
    
    for line in chunks[0]:
        line = parse(line)
        name = line[0]
        arule = []
        for rule in line[1:]:
            if ':' in rule:
                l, r = rule.split(':')
                cond = l[0]
                op = l[1]
                val = int(l[2:])
                goto = r
                arule.append((cond, op, val, goto))
                bw[goto].append(name)
                coord[cond].append(val)
                if op == '>':
                    coord[cond].append(val+1)
                if op == '<':
                    coord[cond].append(val-1)
                

            else:
                arule.append(rule)
                bw[goto].append(name)
        rules[name] = arule
    
    '''
    for v, li in coord.items():
        li = sorted(li)
        if li[0] != 1:
            li = [1] + li
        if li[-1] != 4000:
            li.append(4000)
        
        coord[v] = li
    
   
    ranges = {}
    for v, li in coord.items():
        r = []
        for a, b in list(zip(li, li[1:])):
            if b - a > 1:
                r.append((a, b))

        ranges[v] = r
    '''
    
    parts = []
    xr = [1, 4000]
    mr = [1, 4000]
    ar = [1, 4000]
    sr = [1, 4000]
    su = sim2(xr, mr, ar, sr, rules)
    

    '''
    parts = []
    for line in chunks[1]:
        x,xval, m, mval, a, aval, s, sval = parse2(line)
        parts.append((xval, mval, aval, sval))

    acc = set()
    for part in parts:
        if sim(part, rules):
            acc.add(part)        
    
    for part in acc:
        for val in part:
            su += val
        '''


    return su


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    rules = {}
    for line in chunks[0]:
        line = parse(line)
        name = line[0]
        arule = []
        for rule in line[1:]:
            if ':' in rule:
                l, r = rule.split(':')
                cond = l[0]
                op = l[1]
                val = int(l[2:])
                goto = r
                arule.append((cond, op, val, goto))
            else:
                arule.append(rule)
        rules[name] = arule
    

    parts = []
    for line in chunks[1]:
        x,xval, m, mval, a, aval, s, sval = parse2(line)
        parts.append((xval, mval, aval, sval))

    acc = set()
    for part in parts:
        if sim(part, rules):
            acc.add(part)        
    
    for part in acc:
        for val in part:
            su += val

    return su



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,19, p1, p2, cmds)
if stats: print_stats()

#manual()
