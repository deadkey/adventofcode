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
    #return lazy_ints(line.split())
    line = line.replace('Valve', '')
    line = line.replace('has flow rate=', '')
    line = line.replace('tunnels lead to', '')
    line = line.replace('tunnel leads to', '')
    line = line.replace('valves', '')
    line = line.replace('valve', '')

    
    
    return lazy_ints(multisplit(line, ' ;,')) 


def bfs(q, g):
    visited = set()
    dists = {}
    for node in q:
        visited.add(node)
        dists[node] = 0
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
                    dists[ne] = 1 + dists[node]
        q = q2
    return dists    

def tobit(li, good):
    s = ['0'] * len(good)
    
    for v in li:
        s[v] = '1'
    return ''.join(s)

def rem(index, li):
    li2 = []
    for v in li:
        if v != index:
            li2.append(v)
    return li2

dp = {}

def test(left, prev, good, dists, press, timeleft):
    if timeleft <= 0: return 0
    mx = 0
    #order = ['DD', 'BB', 'JJ', 'HH', 'EE', 'CC']
    #return calc(order, dists, press)
    bt = (tuple(left), prev, timeleft)#tobit(left, good)

    if bt in dp: return dp[bt]
    '''
    if len(left) == 1: 
        d = dists[good[prev]][good[i]]
        timeleft -= d
        timeleft -= 1
        return timeleft * press[good[left[0]]]
    '''

    for i in left:
        nxt = rem(i, left)
        d = dists[good[prev]][good[i]]
        tmp = timeleft - d - 1
        if tmp > 0:
            alt = tmp * press[good[i]]
            alt += test(nxt, i, good, dists, press, tmp)
        
            mx = max(mx, alt)
    dp[bt] = mx
    #db('Best order', list(p))
    return mx



def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    good = set()
    g = dd(list)
    press = {}
    for i in range(len(data)):
        d = data[i]
        valve = d[0]
        flow = d[1]
        if flow > 0:
            good.add(valve)
        press[valve] = flow
        for other in d[2:]:
            g[valve].append(other)
            g[other].append(valve)
    
    dists = {}
    
    start= bfs(['AA'], g)
    dists['AA'] = start

    for node in good:
        di = bfs([node], g)
        dists[node] = di

    mx = 0
    good = ['AA'] + list(good)
    left = [i for i in range(1, len(good))]
    
    timeleft = 30
    #{v : k for k, v in enumerate(good)}['DD']
    mx = test(left, 0, good, dists, press, timeleft)
        
    
    #db('Best order', list(p))
    return mx

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,16, p1, p2, cmds)
if stats: print_stats()

#manual()
