import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict as dd
import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split('/'))

def walk(a, ids_on_path, g, comp2id):
    best = 0
    for b in g[a]:
        edge_id = comp2id[(a, b)]
        if edge_id not in ids_on_path:
            ids_on_path.add(edge_id)
            alt = a + b + walk(b, ids_on_path, g, comp2id)

            best = max(best, alt)
            ids_on_path.discard(edge_id)
    
    return best


def walk2(a, ids_on_path, g, comp2id):
    best = 0, 0
    for b in g[a]:
        edge_id = comp2id[(a, b)]
        if edge_id not in ids_on_path:
            ids_on_path.add(edge_id)
            altL, alt =  walk2(b, ids_on_path, g, comp2id)
            #alt, altL =  walk2(b, ids_on_path, g, comp2id)
            alt += a + b
            altL += 1
            best = max(best, (altL, alt))
            #best = max(best, (alt, altL))
            
            ids_on_path.discard(edge_id)
    #db(best, a)
    return best


def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    g = dd(list)
    comp2id = {}
    for i, (a, b) in enumerate(data):
        comp2id[a, b] = i
        comp2id[b, a] = i
        g[a].append(b)
        g[b].append(a)
    
    ids_on_path = set()
    return walk(0,  ids_on_path, g, comp2id)


def p2(v):
    #Failed 1853, too low
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    g = dd(list)
    comp2id = {}
    for i, (a, b) in enumerate(data):
        comp2id[a, b] = i
        comp2id[b, a] = i
        g[a].append(b)
        g[b].append(a)
    #db(g)
    ids_on_path = set()
    return walk2(0, ids_on_path, g, comp2id)[1]



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2017,24, p1, p2, cmds)
if stats: print_stats()
#manual()
