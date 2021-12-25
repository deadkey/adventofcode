import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict, Counter
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line = line.replace('#', '')
    return lazy_ints(line.split())
    

import heapq

def gengraph():
    start = [2, 4, 6, 8]
    home = [2, 4, 6, 8]
    N = 11 + 8
    g = [[] for _ in range(N)]
    forbidden = set(start)
    for hallpos in range(11):
        for i, s in enumerate(start):
            if hallpos not in forbidden:
                d = abs(hallpos -s)
                g[11 + i].append((d, hallpos))
                g[hallpos].append((d, 11 + 4 + i))
    return g

def inhall(lt, p):
    return p[0] == 0

def genpath(start, end):
    path = []
    r, c = start
    tr, tc = end
    dc = (tc - c)//abs(tc-c)
    while r > 0:
        r -= 1
        path.append((r, c))
    while c != tc:
        c += dc
        path.append((r, c))
    while r != tr:
        r += 1
        path.append((r, c))
    return path

def gohome(lt, p, t, occ):
    COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    path =  genpath(p, t)
    for p2 in path:
        if p2 in occ:
            return False, None, None
    if (2, t[1]) not in occ:
        path.append((2, t[1]))
    return True, len(path) * COST[lt], path[-1]

def gohall(lt, p, t, occ):
    COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    path =  genpath(p, t)
    for p2 in path:
        if p2 in occ:
            return False, None, None
    return True, len(path) * COST[lt], path[-1]

def tonode(lt, p, t, orig):
    li = []
    #db(f'Change tonode {lt} {p} {t} {orig}')
    for n, r, c in orig:
        if n == lt and (r, c) == p:
            li.append((lt, t[0], t[1]))
        else:
            li.append((n, r, c))
    return frozenset(li)

def cost(lt, p, t):
    COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    steps = abs(t - p)
    return steps * COST[lt]

def ishome(lt, p):
    cols = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
    return cols[lt] == p[1]

def gen(node):
    moves = []
    occ = set()
    for lt, r, c in node:
        occ.add((r, c))

    home_index = {'A': 2, "B": 4, 'C': 6, "D": 8}
    for lt, r, c in node:
        p = r,c
        if True: #if not ishome(lt, (r, c)):
            if inhall(lt,  (r, c)):
                ok, d, p2 =  gohome(lt, p, (1, home_index[lt]), occ)
                if ok:
                    moves.append((d, tonode(lt, p, p2, node)))
            else:
                #startpos
                for hall in [0, 1, 3, 5, 7, 9, 10]:
                    ok, d, p2 =  gohall(lt, p, (0, hall), occ)
                    if ok:
                        moves.append((d, tonode(lt, p, p2, node)))
    return moves
                
            


def dij(S, T):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    INF = 10**30
    dist = defaultdict(lambda: INF)

    pq = []
    dist[S] = 0
    pq.append((0, S))
    heapq.heapify(pq)
    done = False
    cnt = 0
    while pq and not done:
        (nd, node) = heapq.heappop(pq)
        if node == T: return dist[T]
        for (dd, nn) in gen(node):
            #db(f'From {node} to {nn} cost {dd}')
            alt = dist[node] + dd
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn))
        cnt += 1
        db(nd)
        #if cnt > 3:
        #    return None
    return None

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    pos = []
    for i, lt in enumerate(data[2]):
        pos.append((lt, 1, i * 2 + 2))
    for i, lt in enumerate(data[3]):
        pos.append((lt, 2, i * 2 + 2))
    
    pos = frozenset(pos)
    db('Start', pos)
    target = frozenset([('A', 1, 2), ('A', 2, 2), ('B', 1, 4), ('B', 2, 4), ('C', 1, 6), ('C', 2, 6), ('D', 1, 8), ('D', 2, 8)])
    
    dist = dij(pos, target)
    offset = 0
    db('Start', pos)
    
    return dist

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,23, p1, p2, cmds)
if stats: print_stats()
#manual()
