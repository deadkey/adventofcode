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
    line = removeall(line, ':', ',')
    data = lazy_ints(line.split())
    table = {}
    for i in range(0, len(data), 2):
        key = data[i]
        val = data[i +1]
        table[key] = val
    return table

def parseclue(line):
    line = removeall(line, ':', ',')
    return lazy_ints(line.split())

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    sues = [parse(line) for line in lines]
    with open('clue.txt', 'r') as clue:
        for line in clue.read().split('\n'):
            key, val = parseclue(line)
            filtered = []
            for table in sues:
                if key in table:
                    if val == table[key]:
                        filtered.append(table)
                else:
                    filtered.append(table)
            sues = filtered
    assert len(sues) == 1
    sue = sues[0]
    return sue['Sue']


def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,16, p1, p2, cmds)
if stats: print_stats()
#manual()
