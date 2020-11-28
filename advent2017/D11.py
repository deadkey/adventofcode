from collections import defaultdict as dd
from collections import deque
import sys
lines = sys.stdin.readlines()
adj = dd(set)
for line in lines:
    i, li = line.split('<->')
    to = list(map(int, li.split(',')))
    for t in to:
        adj[int(i)].add(t)
        adj[t].add(int(i))

def bfs(f):
    visited = set()
    q = deque()
    q.append(f)
    while len(q) > 0:
        c = q.popleft()
        visited.add(c)
        for child in adj[c]:
            if child not in visited:
                q.append(child)
    return visited
a = set()
groups = 0
for key in adj:
    if key not in a:
        vis = bfs(key)
        if len(vis) > 0:
            groups += 1
        a |= vis
print(groups)
#print(len(visited))
