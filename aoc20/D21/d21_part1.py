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

from collections import defaultdict
class Flow:
    def __init__(self, sz):
        self.G = [
            defaultdict(int) for _ in range(sz)
        ] # neighbourhood dict, N[u] = {v_1: cap_1, v_2: cap_2, ...}
        self.Seen = set() # redundant
    
    def add_edge(self, u, v, cap):
        """ Increases capacity on edge (u, v) with cap. 
            No need to add the edge """
        self.G[u][v] += cap
    
    def max_flow(self, source, sink):
        def dfs(u, hi):
            G = self.G
            Seen = self.Seen
            if u in Seen: return 0
            if u == sink: return hi
            
            Seen.add(u)
            for v, cap in G[u].items():
                if cap >= self.min_edge:
                    f = dfs(v, min(hi, cap))
                    if f:
                        G[u][v] -= f
                        G[v][u] += f
                        return f
            return 0

        flow = 0
        self.min_edge = 2**30 # minimal edge allowed
        while self.min_edge > 0:
            self.Seen = set()
            pushed = dfs(source, float('inf'))
            if not pushed:
                self.min_edge //= 2
            flow += pushed
        return flow



def db(*a): 
    if DB: print(*a)

def parse(line):
    line = removeall(line, ')', ',', 'contains')
    if '(' in line:
        ingli, allli = line.split('(')
        ing = ingli.split()
        all = allli.split()
        return ing, all
    return ing, []
    

def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    all2food = dd(list)
    alls = set()
    foods = Counter()
    for ing, all in data:
        alls |= set(all)
        for a in all:
            all2food[a].append(ing)
        for f in ing:
            foods[f] += 1
    used = set()
    for a in alls:
        inall = set(all2food[a][0])
        for li in all2food[a]:
            inall &= set(li)
        used |= inall
    mx = 0
    db(foods)
    db(used)
    for f in foods.keys():
        if f not in used:
            mx += foods[f]
    return mx

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,21, p1, p2, cmds)
if stats: print_stats()
#manual()
