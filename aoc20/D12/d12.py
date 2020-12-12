import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return line[0], int(line[1:])

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    data = [parse(line) for line in lines]
    DIRS = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W':(0, -1)}
    rot = ['N', 'E', 'S', 'W']
    facing = 1
    r, c = 0, 0
    for d, val in data:
        if d in DIRS:
            dr, dc = DIRS[d]
            r += dr * val
            c += dc * val
        if d == 'F':
            dr, dc = DIRS[rot[facing]]
            r += dr * val
            c += dc * val
        if d == 'R':
            
            db(f'{val}')
            facing += val//90
            facing %= len(rot)
        if d == 'L':
            db(f'{val}')
            facing -= val//90
            facing %= len(rot)
            
        
    return abs(r) + abs(c)


def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    data = [parse(line) for line in lines]
    DIRS = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W':(0, -1)}
    rot = ['N', 'E', 'S', 'W']
    
    facing = 1
    r, c = -1, 10 #relavitve to the ship
    shipr, shipc = 0, 0
    for d, val in data:
        if d in DIRS:
            dr, dc = DIRS[d]
            r += dr * val
            c += dc * val
        #move the ship
        if d == 'F':
            dr, dc = r, c
            
            shipr += dr * val
            shipc += dc * val
        if d == 'R':
            k = val //90
            if k == 1:
                r, c = c, -r
            if k == 2:
                r, c, = -r, -c
            if k == 3:
                r, c = -c, r
        if d == 'L':
            k = val //90
            if k == 1:
                r, c = -c, r
            if k == 2:
                r, c, = -r, -c
            if k == 3:
                r, c = c, -r
        db(f'Ship {shipr} {shipc} and wp {r} {c}')
        
    return abs(shipr) + abs(shipc)

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,12, p1, p2, cmds)
if stats: print_stats()
#manual()
