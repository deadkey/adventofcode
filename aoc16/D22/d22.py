import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *

from collections import defaultdict as dd
import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line = line.replace('-', ' ')
    line = removeall(line,'T','%','/dev/grid/node', 'x','y')
    return lazy_ints(line.split())
    

def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    data = [parse(line) for line in lines]
    nodes = data[2:]
    pairs = 0
    N= len(nodes)
    for i in range(N):
        for j in range(N):
            if i != j:
                iused = nodes[i][3]
                java = nodes[j][4]
                if iused > 0 and iused <= java:
                    pairs += 1
    return pairs

def oktomove(hole_node, move_node):
    sz, used, ava = hole_node[2:-1]
    _, moveused, _ = move_node[2:-1]
    db(sz-used, moveused)
    return sz - used >= moveused
    

def move(move_node, hole_node):
    sz, used, ava = hole_node[2:-1]
    _, moveused, _ = move_node[2:-1]
    hole_node[3] += moveused
    move_node[3] = 0


def p2(v):
    lines = v.strip().split('\n')
    cnt = 0
    data = [parse(line) for line in lines]
    nodes = data[2:]
    N= len(nodes)
    G = 36, 24
    #G = 0, 2
    Gi = 0
    color_map = []
    g = [[] for _ in range(N)]
    nds = [i for i in range(N)]
    labels = {}
    for i in range(N):
        iused = nodes[i][3]
        ix, iy = nodes[i][0:2]
        labels[i] = f'Node {i}\n {iused}/{nodes[i][2]}'
        if iused > 200:
            color_map.append('blue')
        else:
            color_map.append('red')
        for j in range(N):

            jx, jy = nodes[j][0:2]
            if i != j and (abs(ix - jx) + abs(jy - iy))<= 1:
                java = nodes[j][4]
                if iused <= java:
                    g[i].append(j)
        x, y = nodes[i][0:2]
        if y == G[1] and x == G[0]:
            Gi = i

    coord = {}
    for node in nodes:
        x, y = node[0:2]
        coord[x, y] = node
    
    draw(g, nodes, labels, color_map)
    
import networkx as nx
import matplotlib.pyplot as plt

def draw(g, nodes, labels, color_map):
    G=nx.DiGraph()
    N = len(nodes)
    nds = [i for i in range(N)]
    
    G.add_nodes_from(nds)
    pos = {}
    for n, node in enumerate(nodes):
        x, y = node[0:2]
        G.nodes[n]['pos'] = x, y
        pos[n] = x,y

    for node in nds:
        ns = g[node]
        for nb in ns:
            G.add_edge(node, nb)
    print('Nodes of graph', G.nodes())

    print('Efges of graph', G.edges())
    nx.draw_networkx(G,labels = labels, node_color=color_map, with_labels=True, pos = pos)
    plt.show()


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,22, p1, p2, cmds)
if stats: print_stats()
#manual()
