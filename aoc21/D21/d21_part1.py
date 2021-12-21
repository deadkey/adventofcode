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

def play(pos):
    turn = 0
    die = 1
    points = [0, 0]
    no = 0
    while True:
        steps = die * 3 + 1 + 2
        die += 3

        pos[turn] = (pos[turn] + steps)
        while pos[turn] > 10:
            pos[turn] -= 10
        points[turn] += pos[turn]

        no += 3
        if points[turn] >= 1000:
            return min(points), no
        #db(points)

        turn += 1
        turn %= 2

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    players = [data[0][-1], data[1][-1]]
    los, no = play(players)
    db(los, no)
    return los * no

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,21, p1, p2, cmds)
if stats: print_stats()
#manual()
