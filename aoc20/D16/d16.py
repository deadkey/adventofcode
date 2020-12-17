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
# used in mincut @ Kattis
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

def parserules(line):
    field, ranges = line.split(':')
    li = multisplit(ranges, 'or', '-')

    return field, lazy_ints(li)



def parse(line):
    return lazy_ints(line.split(','))

def inone(f, rules):
    for _, (l, h, l2, h2) in rules:
            #db((l, h, l2, h2) )
            if l <= f <= h or l2 <= f <= h2:
                return True
    return False

def cntinv(ticket, rules):
    cnt = 0
    for f in ticket:
        if not inone(f, rules):
            cnt += f
        
    return cnt


def isinv(ticket, rules):
    cnt = 0
    for f in ticket:
        if not inone(f, rules):
            return True
        
    return False

def p1(v):
    ch = chunks(v)
    rules = [parserules(line) for line in ch[0].split("\n")]

    myticket = [parse(line) for line in ch[1].split('\n')]
    nearby = [parse(line) for line in ch[2].split('\n')]
    
    inv = 0
    for ticket in nearby:
        inv += cntinv(ticket, rules)

    return inv

def checkfield(i, tickets, l, h, l2, h2):
    #db(i, l, h, l2, h2)
    for ticket in tickets:
        f = ticket[i]
        if not( l <= f <= h or l2 <= f <= h2):
            #db(f,  'false')
            return False
    return True

def p2(v):
    ch = chunks(v)
    rules = [parserules(line) for line in ch[0].split("\n")]

    myticket =parse(ch[1])
    nearby = [parse(line) for line in ch[2].split('\n')]
    #nearby.append(myticket)
    valid = []
    for ticket in nearby:
        if not isinv(ticket, rules):
        
            valid.append(ticket)
    db(rules)
    V = len(valid[0])
    possible = dd(list)
    val2field = dd(list)
    for field, ranges in rules:
        #db(field, ',',ranges)
        for pos in range(V):
            if checkfield(pos, valid, *ranges):
                #db('ok')
                possible[field].append(pos)
                val2field[pos].append(field)
                
    matches =  {}
    used= set()
    
    while len(matches) < V:
        for field, _ in rules:
            if field not in matches:
                if len(possible[field]) == 0:
                    db('Failed')
                    return
                if len(possible[field]) == 1:
                    val = possible[field][0]
                    matches[field] = val
                    
                    for oth in val2field[val]:
                        if val in possible[oth]:
                            possible[oth].remove(val)
                
    # Failed 48551226272641, 739664849089
    su = 1
    db('Running greedy matching')
    for m, val in matches.items():
        if 'departure' in m:
            su *= myticket[val]
    return su





def p2_old(v):
    ch = chunks(v)
    rules = [parserules(line) for line in ch[0].split("\n")]

    myticket =parse(ch[1])
    nearby = [parse(line) for line in ch[2].split('\n')]
    #nearby.append(myticket)
    valid = []
    for ticket in nearby:
        if not isinv(ticket, rules):
        
            valid.append(ticket)
    db(rules)
    V = len(valid[0])
    possible = dd(list)
    used= set()
    val2field = {}
    for field, ranges in rules:
        #db(field, ',',ranges)
        for pos in range(V):
            if checkfield(pos, valid, *ranges):
                #db('ok')
                possible[field].append(pos)
                used.add(pos)
    for p in range(V):
        if p not in used:
            db('NOT FOUND ', p)
    db(possible)     
    matches =  {}
    P = len(possible)
    S = len(possible) + V
    T = S + 1
    F = Flow(T+1)
    for i, (field, _) in enumerate(rules):
        F.add_edge(S, i, 1)
    for i, (field, _) in enumerate(rules):
        for p in possible[field]:
            ni = p + P
            F.add_edge(i, ni, 1)
            F.add_edge(ni, i, 0)
            
    for i in range(V):
        ni = i + P
        F.add_edge(ni, T, 1)
    flow = F.max_flow(S, T)

    db(flow, V, len(rules))
    for i in range(len(valid[0])):
        p = i + P
        edges = F.G[p]
        db(edges)
        for edge, flow in edges.items():

            if edge < P and flow > 0:
                matches[rules[edge][0]] = i
    db(matches)
    ind = 0
    
    # Failed 48551226272641, 739664849089
    su = 1
    for m, val in matches.items():
        if 'departure' in m:
            su *= myticket[val]
    return su




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,16, p1, p2, cmds)
if stats: print_stats()
#manual()
