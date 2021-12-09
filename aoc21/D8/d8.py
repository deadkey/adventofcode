import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict as dd, Counter
from itertools import permutations
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(multisplit(line, '|', " "))
    

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    cnt = 0
    
    for i in range(len(data)):
        v = data[i][-4:]
        for w in v:
            if len(w) in set([2, 3, 4, 7]):
                cnt += 1

    return cnt

def check(p, dig):
    orig = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 5: 'abdfg', 6:'abdefg', 7:'acf', 8:'abcdefg', 9:'abcdfg'}
    newdig = []
    for i in range(10):
        o = orig[i]
        s = []
        for l in o:
            lt = p[ord(l) - ord('a')]
            s.append(lt)
        newdig.append(''.join(sorted(s)))
    for d in dig:
        if ''.join(sorted(d)) not in newdig:
            return False, None
    return True, newdig
    

def val(v):
    
    dig = v[0:11]
    r = v[-4:]
    db(dig)
    for p in permutations(list('abcdefg')):
        ok, res = check(p, dig)
        if ok:
            t = 0
            for i, a in enumerate(r):
                index = res.index(''.join(sorted(a)))
                t = 10 * t + index
            return t
    return None


def p2(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    cnt = 0
    
    db(data)
    
    for i in range(len(data)):
        v = data[i]
        cnt += val(v)
        db(cnt)

    return cnt


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,8, p1, p2, cmds)
if stats: print_stats()
#manual()
