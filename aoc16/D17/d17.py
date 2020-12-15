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
import hashlib
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())

def getdoors(s):

    op = set(['b', 'c', 'd', 'e', 'f'])
    ha = hashlib.md5(s.encode()).hexdigest()
    doors = [1 if ch in op else 0 for ch in ha[0:4]]
    return doors

def gen(ne, path, init):
    r, c, u, d, l, ri = ne
    ne = []
    if u == 1:
        rr, cc = r -1, c
        if 0<= rr < 4 and 0 <= cc < 4:
            s = init + path + 'U'
            uu, dd, ll, rt = getdoors(s)
            ne.append((rr, cc, uu, dd, ll, rt, path + 'U'))
    if d == 1:
        rr, cc = r +1, c
        if 0<= rr < 4 and 0 <= cc < 4:
            s = init + path + 'D'
            uu, dd, ll, rt = getdoors(s)
            ne.append((rr, cc, uu, dd, ll, rt, path + 'D'))
    
    if l == 1:
        rr, cc = r, c -1
        if 0<= rr < 4 and 0 <= cc < 4:
            s = init + path + 'L'
            uu, dd, ll, rt = getdoors(s)
            ne.append((rr, cc, uu, dd, ll, rt, path + 'L'))
    
    if ri == 1:
        rr, cc = r, c +1
        if 0<= rr < 4 and 0 <= cc < 4:
            s = init + path + 'R'
            uu, dd, ll, rt = getdoors(s)
            ne.append((rr, cc, uu, dd, ll, rt, path + 'R'))
    return ne
    


def bfs(init):
    u, d, l, r = getdoors(init)
    node = 0, 0, u, d, l, r
    q = [(node, '')]
    while q:
        q2 = []
        for node, pa in q:
            #db(node, pa)
            if node[0] == 3 and node[1] == 3: return pa

            for rr, cc, uu, dd, ll, rt, path in gen(node, pa, init):
                ne = (rr, cc, uu, dd, ll, rt)
               
                q2.append((ne, path))
        q = q2
        #db(len(pa))
        #if len(pa) > 7:
        #    return
    #db(visited)
    return 'Error'



def longest(init):
    u, d, l, r = getdoors(init)
    node = 0, 0, u, d, l, r
    q = [(node, '')]
    moves = 0
    best = 0
    while q:
        q2 = []
        for node, pa in q:
            #db(node, pa)
            if node[0] == 3 and node[1] == 3:
                best = moves
             
            else:
                for rr, cc, uu, dd, ll, rt, path in gen(node, pa, init):
                    ne = (rr, cc, uu, dd, ll, rt)
                
                    q2.append((ne, path))
        q = q2
        moves += 1
        #db(len(pa))
        #if len(pa) > 7:
        #    return
    #db(visited)
    return best

def p1(v):
    lines = v.strip().split('\n')
    init = lines[0]
    path = bfs(init)
    return path

def p2(v):
    lines = v.strip().split('\n')
    init = lines[0]
    path = longest(init)
    return path



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,17, p1, p2, cmds)
if stats: print_stats()
#manual()
