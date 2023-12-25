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
    return lazy_ints(multisplit(line, ' :')) 


 
from collections import defaultdict
 
# This class represents an directed graph
# using adjacency list representation
 
 
class Graph:
 
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
        self.Time = 0
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    '''A recursive function that find finds and prints strongly connected
    components using DFS traversal
    u --> The vertex to be visited next
    disc[] --> Stores discovery times of visited vertices
    low[] -- >> earliest visited vertex (the vertex with minimum
                discovery time) that can be reached from subtree
                rooted with current vertex
     st -- >> To store all the connected ancestors (could be part
           of SCC)
     stackMember[] --> bit/index array for faster check whether
                  a node is in stack
    '''

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
        return flow, self.Seen




def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    g = dd(list)
    nodes = dd(int)
    edges = []

    for i in range(len(data)):
        d = data[i]
        name = d[0]
        li = d[1:]
        g[name] = li
        if name not in nodes:
            nodes[name] = len(nodes)
        for oth in li:
            g[oth].append(name)
            if oth not in nodes:
                nodes[oth] = len(nodes)
            edges.append((name, oth))
    
    N = len(nodes) + 2
    S = N -2
    T = N -1
    li = list(nodes)

    for i in range(len(li)):
        for k in range(i+1, len(li)):
            f = Flow(N)
            for edge in edges:
                n1, n2 = nodes[edge[0]], nodes[edge[1]]
               
                f.add_edge(n1, n2, 1)
                f.add_edge(n2, n1, 1)
            
            f.add_edge(S, i, 10)
            f.add_edge(k, T, 10)
            
            flow, seen = f.max_flow(S, T)
            if flow == 3:
                A =  len(seen) - 1
                B = len(nodes)  - A
                return A * B
     

    return -1

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

if not so: run(2023,25, p1, p2, cmds)
if stats: print_stats()

#manual()
