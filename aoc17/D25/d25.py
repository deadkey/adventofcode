import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())
    
A = 0
B = 1
C = 2
D = 3
E = 4
F = 5

def doit(state, cursor, tape):
    val = tape[cursor]
    if state == A:
        if val == 0:
            tape[cursor] = 1
            return cursor+1, B
        if val == 1:
            tape[cursor] = 0
            return cursor -1, F
    elif state == B:
        if val == 0:
            tape[cursor] = 0
            return cursor+1, C
        if val == 1:
            tape[cursor] = 0
            return cursor +1, D
    elif state == C:
        if val == 0:
            tape[cursor] = 1
            return cursor -1, D
        tape[cursor] = 1
        return cursor +1, E
    elif state == D:
        if val == 0:
            tape[cursor] = 0
            return cursor-1, E
        tape[cursor] = 0
        return cursor -1,D
    elif state == E:
        if val == 0:
            tape[cursor] = 0
            return cursor+1, A
        tape[cursor] = 1
        return cursor +1, C
    elif state == F:
        if val == 0:
            tape[cursor] = 1
            return cursor-1, A
        tape[cursor] = 1
        return cursor + 1, A
    

def p1(v):
    tape = Counter()
    state = A
    cursor = 0
    N = 12994925
    for _ in range(N):
        cursor, state = doit(state, cursor, tape)
        #db(cursor)
        #db(tape)
    return sum(tape.values())


def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2017,25, p1, p2, cmds)
if stats: print_stats()
#manual()
