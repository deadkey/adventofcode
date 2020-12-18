import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *

from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line = line.replace('(', ' ( ').replace(')', ' ) ')
    return lazy_ints(line.split())

def evval(li):
    v = 0
    #db('In evval', li)
    op = '+'
    for val in li:
        if isint(val):
            val = int(val)
            if op == '+':
                v += val
            
            if op == '*':
                v *= val
            
            if op == '-':
                v -= val
            
            if op == '/':
                v /= val

        else:
            op = val
        #db(val, op, v)
    return v


def evval2(li):
    v = 0
    #db('In evval', li)
    op = ''
    stack = []
    for val in li:
        if isint(val):
            val = int(val)

            if op == '+':
                val1 = stack.pop()
                newval = val1 + val
                stack.append(newval)
            else:
                stack.append(val)


            '''
            if op == '-':
                v -= val
            
            if op == '/':
                v /= val
            '''

        else:
            op = val
        #db(val, op, v)
    
    return mul(stack)

def evexpr(expr):
    #db(expr)
    li = [[]]
    for ch in expr:
        if ch == '(':
            li.append([])
        elif ch == ')':
            v = evval(li[-1])
            li.pop()
            li[-1].append(v)
        else:
            li[-1].append(ch)
        
    return evval(li[-1])

def evexpr2(expr):
    #db(expr)
    li = [[]]
    for ch in expr:
        if ch == '(':
            li.append([])
        elif ch == ')':
            v = evval2(li[-1])
            li.pop()
            li[-1].append(v)
        else:
            li[-1].append(ch)
        
    return evval2(li[-1])

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 0
    for ex in data:
        res = evexpr(ex)
        su += res
        db('Result = ', res)
    return su

def p2(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 0
    for ex in data:
        db(add(ex))
        res = evexpr2(ex)
        su += res
        #db('Result = ', res)
    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,18, p1, p2, cmds)
if stats: print_stats()
#manual()
