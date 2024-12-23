import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
import networkx as nx
import matplotlib.pyplot as plt
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
    return lazy_ints(multisplit(line, '-')) 
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    g = dd(list)
    nodes = set()
    su = 0

    '''
    # Very slow
    G=nx.Graph()
    
    
    for a, b in data:
        G.add_edge(a, b)
    
    comps = set()
    for node in G.nodes:
        cc = set([node]) | set(G.neighbors(node))
        cliques = nx.algorithms.clique.enumerate_all_cliques(G.subgraph(cc))
        for c in cliques:
            if len(c) == 3:
                comps.add(tuple(sorted(c)))
    '''
    
    for i in range(len(data)):
        a, b = data[i]
        g[a].append(b)
        g[b].append(a)
        nodes.add(a)
        nodes.add(b)
    
    comps = set()
    for node in nodes:
        li1 = g[node]
        seen = set(li1)
        for n in li1:
            for n2 in g[n]:
                if n2 != node and n2 in seen:
                    key = sorted([node, n, n2])
                    comps.add(tuple(key))
    
    
    
    for c in comps:
        ccc = 0
        for x in c:
            if 't' == x[0]:
                ccc = 1
        su += ccc

    
    return su
    



def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    
    G=nx.Graph()
    
    for a, b in data:
        G.add_edge(a, b)
        
    cliques = nx.algorithms.clique.find_cliques(G)
    best = max(cliques, key = len)
    
    s= sorted(best)
    return ','.join(s)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,23, p1, p2, cmds)
if stats: print_stats()

#manual()
