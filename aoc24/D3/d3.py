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
def parse1(line):
    import re
    array = list(re.finditer(r'mul\(([0-9]+),([0-9]+)\)', line))
    res = [(s.group(1),s.group(2)) for s in array]
    res = [(int(a), int(b)) for (a,b) in res]
    return res

def parse2(line):
    import re
    array = list(re.finditer(r'mul\(([0-9]+),([0-9]+)\)', line))
    res = [(s.group(1),s.group(2), s.start()) for s in array]
    res = [(int(a), int(b), s) for (a,b, s) in res]
    return res

  

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse1(line) for line in lines]
    su = 0
  
    for i in range(len(data)):
        d = data[i]
        for a, b in d:
            if 0 <= a < 1000 and 0 <= b < 1000:
                su += a * b
            

    return su

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse2(line) for line in lines]
    su = 0
    enabled = True
    for i, line in enumerate(lines):
        d = parse2(line)
        ok = []
        
        for j in range(len(line)):
            D = len('do()')
            D2 = len("don't()")
            if line[j:j+D] == 'do()':
                enabled = True
                
            if line[j:j+D2] == "don't()":
                enabled = False
            ok.append(enabled)
        
        for a, b,s in d:
            if 0 <= a < 1000 and 0 <= b < 1000 and ok[s]:
                su += a * b
    return su            



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,3, p1, p2, cmds)
if stats: print_stats()

#manual()
