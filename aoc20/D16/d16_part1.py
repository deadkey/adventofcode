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

def parserules(line):
    field, ranges = line.split(':')
    li = multisplit(ranges, 'or', '-')

    return field, lazy_ints(li)
    

def parse(line):
    return lazy_ints(line.split(','))

def inone(f, rules):
    for _, (l, h, l2, h2) in rules:
            db((l, h, l2, h2) )
            if l <= f <= h or l2 <= f <= h2:
                return True
    return False
                

def cntinv(ticket, rules):
    cnt = 0
    for f in ticket:
        if not inone(f, rules):
            cnt += f

        
    return cnt

def p1(v):
    ch = chunks(v)
    rules = [parserules(line) for line in ch[0].split("\n")]

    myticket = [parse(line) for line in ch[1].split('\n')]
    nearby = [parse(line) for line in ch[2].split('\n')]
    
    inv = 0
    for ticket in nearby:
        inv += cntinv(ticket, rules)

    return inv

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,16, p1, p2, cmds)
if stats: print_stats()
#manual()
