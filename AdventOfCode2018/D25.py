from fetch import fetch, fetchlines
from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
import sys

def manh(n1, n2):
    return sum([abs(n1[i] - n2[i]) for i in range(4)])
        

def find(x):
    if parents[x][0] != x:
        parents[x][0] = find(parents[x][0])
    return parents[x][0]

def add(a, a_parent, b_parent):

    p,size= parents[b_parent]
    size += parents[a_parent][1]
    parents[b_parent] =  [b_parent, size]
    parents[a_parent][0] = b_parent

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
        return False

    if parents[a_parent][1] < parents[b_parent][1]:
        add(a,a_parent, b_parent)
    else:
        add(b, b_parent,a_parent)
    return True

data = sys.stdin.readlines()
nodes = []
for line in data:
    node = tuple(map(int, line.split(',')))
    nodes.append(node)

parents = [[i, 1] for i in range(len(nodes))]
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if j != i:
            d = manh(nodes[i], nodes[j])
            if d<= 3:
                union(i, j)
roots = set()
for i in range(len(nodes)):
    roots.add(find(i))
print(len(roots))