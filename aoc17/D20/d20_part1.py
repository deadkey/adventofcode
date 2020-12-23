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
    line = replaceall(line, '=', 'p', 'v', 'a', '<', '>', ',', ' ')
    ints =  lazy_ints(line.split())
    return ints[0:3], ints[3:6], ints[6:] 



def p1(v):
    #FAILED 730, too high
    lines = v.strip().split('\n')
    cnt = 0
    data = [parse(line) for line in lines]
    li = [(abs(ax) + abs( ay) + abs(az), i) for i,( _, _, (ax, ay, az)) in enumerate(data)]
    li.sort()
    return li[0][1]

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2017,20, p1, p2, cmds)
if stats: print_stats()
#manual()
