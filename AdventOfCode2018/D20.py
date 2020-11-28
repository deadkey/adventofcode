from fetch import fetch, fetchlines
from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
import sys

def bfs(g):
    visited = set()
    dists = dd(int)
    q = [(0, 0)]
    for node in q:
        visited.add(node)
    dist = 0    
    while q:
        q2 = []
        dist += 1
        for node in q:
            for ne in g[node]:
                if ne not in visited:
                    visited.add(ne)
                    dists[ne] = dists[node] + 1
                    q2.append(ne)
        q = q2

    return dist, dists


test1= sys.stdin.read().strip() #'^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'
test = test1.replace('^', '').replace('$', '')
branches = []
graph = dd(list)
curr = (0, 0)
coord = {'E': (1, 0), 'N': (0, 1),'S': (0, -1), 'W': (-1, 0)}
for dir in test:

    print('curr, dir', curr, dir)
    if dir == '(':
        branches.append(curr)
    elif dir == ')':
        curr = branches.pop()
    elif dir == '|':
        curr = branches[-1]
    else:
        walkdir = coord[dir]
        ncurr = (curr[0] + walkdir[0], curr[1] + walkdir[1])
        graph[curr].append(ncurr)
        graph[ncurr].append(curr)
        curr = ncurr
#print(graph)
maxdist, alldists= bfs(graph)
print(maxdist -1) #not nbr of nodes
print('part2:')
cnt = 0
test = 0
for d in alldists.values():
    if d >= 1000:
        cnt += 1
    test = max(test, d)
print(cnt)
print(test)
