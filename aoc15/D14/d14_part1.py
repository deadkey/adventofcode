import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    d = line.split()
    name = d[0]
    sp = int(d[3])
    flytime = int(d[6])
    resttime = int(d[-2])
    return name, sp, flytime, resttime

def sim(rd, time):
    _, sp, flytime, resttime = rd
    d = 0
    period = flytime + resttime
    hole = time//period
    distperperiod = flytime * sp
    left = min(time % period, flytime)
    d = hole * distperperiod + left* sp
    return d


def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    time = 2503
    rd = [parse(line) for line in lines]
    dists = [sim(r, time) for r in rd]


    return max(dists)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,14, p1, p2, cmds)
if stats: print_stats()
#manual()
