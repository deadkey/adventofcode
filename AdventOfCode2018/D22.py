from fetch import fetch, fetchlines
from collections import Counter, defaultdict as dd
from heapq import heappush as push, heappop as pop
import sys

CLIMB = 12
TORCH = 13
NEITHER = 14
TOOLS = [CLIMB, TORCH, NEITHER]
GEOTOOLS= {0: [CLIMB, TORCH], 1: [CLIMB, NEITHER], 2: [TORCH, NEITHER]}

def ok(tool, geotype):
    return tool in GEOTOOLS[geotype]

def gen(grid, node):
    nei = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    r, c, curr_tool =node[0], node[1], node[2]
    adj = []
    for cr, cc in nei:
        tr, tc = r + cr, c +cc
        if 0 <= tr < R and 0 <= tc < C:
            if ok(curr_tool, grid[tr][tc]):
                nextnode = (tr, tc, curr_tool)
                adj.append((1, nextnode))
    for other_tool in TOOLS:
        if other_tool != curr_tool and ok(other_tool, grid[r][c]):
            switchnode = (r, c, other_tool)
            adj.append((7, switchnode))

    return adj
# Dijkstra from S to T
def dij(grid):
    from collections import defaultdict as dd
    INF = 10**12
    dist = dd(lambda: INF)
    S = (0, 0, TORCH)
    pq = []
    dist[S] = 0
    push(pq, (0, S))
    while pq:
        (nd, node) = pop(pq)
        for (dd, nn) in gen(grid, node):
            alt = dist[node] + dd
            if dist[nn] > alt:
                dist[nn] = alt
                push(pq, (dist[nn], nn))
    return dist


#depth: 7305
#target: 13,734
TX = 13
TY = 734
DEPTH = 7305

"""
TX = 10
TY = 10
DEPTH = 510
"""

ROCK = '.'
WET = '='
NARROW = '|'
R = TY * 2
C = TX * 3
y0g = 16807
x0g = 48271
eromod = 20183

def printgrid(grid):
    for row in range (len(grid)):
        prow = []
        for col in range(len(grid[0])):
            prow.append(grid[row][col])
        print(''.join(prow))      
    print('')

grid = [[0] * C for _ in range(R)]

gridstr = [['#'] * C for _ in range(R)]
geo = [[-1] * C for _ in range(R)]
ero = [[-1] * C for _ in range(R)]

 # geolocig index
geo[0][0] = 0
geo[TY][TX] = 0
ero[TY][TX] = DEPTH % eromod
for c in range(C):
    geo[0][c] = c * y0g
    ero[0][c] = (geo[0][c]  + DEPTH) % eromod

for r in range(R):
    geo[r][0] = r * x0g
    ero[r][0] = (geo[r][0]  + DEPTH) % eromod
    
for r in range(1, R):
    for c in range(1, C):
        if geo[r][c] == -1 and not (r == TY and c == TX):
            assert(ero[r-1][c]> -1)
            assert(ero[r][c -1]> -1)
            
            geo[r][c] = ero[r-1][c] * ero[r][c-1]
            ero[r][c] = (geo[r][c] +DEPTH) % eromod
            

#erosion level
types = {0: ROCK, 1: WET, 2: NARROW}

for r in range(R):
    for c in range(C):
        gridstr[r][c] = types[(ero[r][c] % 3)]
        grid[r][c] = (ero[r][c] % 3)

#gridstr[TY][TX] = 'T'
gridstr[0][0] = 'M'
#printgrid(gridstr)

def risk(grid, tr, tc):
    risklevel= 0
    for r in range(0, tr + 1):
        for c in range(0, tc + 1):
            risklevel += grid[r][c]
    
    return risklevel
res = risk(grid,TY, TX)
print(res) 

dists = dij(grid)
tnode = (TY, TX, TORCH)
print('best', dists[tnode])
