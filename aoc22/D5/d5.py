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
    return lazy_ints(multisplit(line, ']')) 

def parse2(line):
    #return lazy_ints(line.split())
    line = line.replace('move', '')
    line = line.replace('from', '')
    line = line.replace('to', '')
    return lazy_ints(multisplit(line, ' ')) 



def p1(v):
    lines = v.strip().split('\n')
    chunks = v.split('\n\n')
    su = 0
    stacklines = chunks[0].split('\n')[::-1]
    stacklines = [line.replace('[', ' ').replace(']', ' ') for line in stacklines]
    moves = chunks[1].split('\n')

    cols = {}
    indeces = []
    for i, ch in enumerate(stacklines[0]):
        if ch != ' ':
            cols[i] = int(ch)-1
            indeces.append(i)
    

    N = max(cols.values()) + 1
    stacks = [[] for _ in range(N)]
    
    for line in stacklines[1:]:
        for i in indeces:
            ch = line[i]
            if ch != ' ':
                stacks[cols[i]].append(ch)
                
    db(stacks)
    moves = [parse2(line) for line in moves]
    for line in moves:
        no, fr, t = line
        db(no, fr, t)
        li = []
        for i in range(no):
            lt = stacks[fr-1].pop()
            stacks[t-1].append(lt)
        db(stacks)
    out = []
    for s in stacks:
        out.append(s[-1])

    return ''.join(out)

def p2(v):
    lines = v.strip().split('\n')
    chunks = v.split('\n\n')

    data = [parse(line) for line in lines]
    su = 0
    stacklines = chunks[0].split('\n')[::-1]
    stacklines = [line.replace('[', ' ').replace(']', ' ') for line in stacklines]
    moves = chunks[1].split('\n')

    cols = {}
    indeces = []
    for i, ch in enumerate(stacklines[0]):
        if ch != ' ':
            cols[i] = int(ch)-1
            indeces.append(i)
    

    N = max(cols.values()) + 1
    stacks = [[] for _ in range(N)]
    
    for line in stacklines[1:]:
        
        spaces = 0
        for i in indeces:
            ch = line[i]
            if ch != ' ':
                stacks[cols[i]].append(ch)
                
    db(stacks)
    moves = [parse2(line) for line in moves]
    for line in moves:
        no, fr, t = line
        db(no, fr, t)
        li = []
        for i in range(no):
            lt = stacks[fr-1].pop()
            li.append(lt)
        for lt in li[::-1]:
            stacks[t-1].append(lt)
        db(stacks)
    out = []
    for s in stacks:
        out.append(s[-1])

    return ''.join(out)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,5, p1, p2, cmds)
if stats: print_stats()

#manual()
