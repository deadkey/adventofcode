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

def addleft(index, li, val):
    while type(li[index]) == list:
        li = li[index]
        index = len(li) -1
    li[index] += val


def addright(index, li, val):
    while type(li[index]) == list:
        li = li[index]
        index = 0
    li[index] += val

def explode(li, depth):
    if type(li) == int:
        return 0, None
    if depth == 4:
        #explode
        return 1, li
    for index, x in enumerate(li):
        res, value = explode(x, depth + 1)
        if res:
            break
    if res == 1:
        li[index] = 0
    if res:
        a, b = value

        if index - 1 >= 0 and a != None:
            addleft(index-1, li, a)
            a = None
        if index + 1 < len(li) and b != None:
            addright(index+1, li, b)
            b = None
        
        return 2, (a, b)
        
    return 0, None    
            
def split(li):
    if type(li)  == int:
        return False
    for i, x in enumerate(li):
        if type(x) == int:
            if x >= 10:
                lo, hi = x//2 , (x+1)//2
                li[i] = [lo, hi]
                return True
        else:
            if split(x):
                return True
    return False
    
def reduce(li):
    while True:
        status, ret = explode(li, 0)
        if status:
            continue
        if split(li):
           continue
        else:
            break
    
def magnitude(li):
    if type(li) == int:
        return li
    left = magnitude(li[0])
    right = magnitude(li[1])
    return 3 * left + 2 * right

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    numbers = []
    for i in range(len(data)):
        d = data[i]
        num = eval(d)
        numbers.append(num)
    while len(numbers) > 1:
        first = numbers[0]
        second = numbers[1]
        num = [first, second]
        reduce(num)
        numbers = [num] + numbers[2:]
    return magnitude(numbers[0])


def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,18, p1, p2, cmds)
if stats: print_stats()
#manual()
