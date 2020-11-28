from fetch import fetch, fetchlines
from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
import sys


def printclay(clay, maxd, minx, maxx):
    grid= []
    for row in range (maxd + 1):
        grid.append([])
        for col in range(minx, maxx+ 1):
            grid[row].append('.')
    for xs, xe, ys, ye in clay:
        for x in range(xs, xe + 1):
            for y in range(ys, ye + 1):
                grid[y][x - minx] = '#'
    grid[0][500 - minx] = '+'
    for row in range (maxd + 1):
        prow = []
        for col in range(minx, maxx+ 1):
            prow.append(grid[row][col - minx])
        print(''.join(prow))

def printgrid(grid):
    for row in range (len(grid)):
        prow = []
        for col in range(len(grid[0])):
            prow.append(grid[row][col])
        print(''.join(prow))



clay = []
data = sys.stdin.readlines()
maxd= 0
INF = 10**12
minx = INF
maxx = -INF
minr = INF
maxr = -INF
for line in data:
    t = line.split(',')
    xin = t[0] if 'x' in t[0] else t[1]
    yin = t[0] if 'y' in t[0] else t[1]
    xin = xin.replace('x=', '').strip().split('..')
    xs = int(xin[0])
    xe = xs
    if len(xin) > 1:
        xe = int(xin[1])
    yin = yin.replace('y=', '').strip().split('..')
    ys = int(yin[0])
    ye = ys
    if len(yin) > 1:
        ye = int(yin[1])
    clay.append((xs,xe,ys, ye))
    maxd = max(maxd, ye)
    minx = min(minx, xs)
    maxx = max(maxx, xe)
    minr = min(minr, ys)
    maxr = max(maxr, ye)
    

grid= []
maxx += 1
minx -= 1
for row in range (maxd + 1):
    grid.append([])
    for col in range(minx, maxx+ 1):
        grid[row].append('.')
for xs, xe, ys, ye in clay:
    for x in range(xs, xe + 1):
        for y in range(ys, ye + 1):
            grid[y][x - minx] = '#'
grid[0][500 - minx] = '|'
#printgrid(grid)


def filldown(r, c):
    global aftercnt
    while r < len(grid) and (grid[r][c] == '|' or grid[r][c] == '.'):
        if grid[r][c] == '.':
            aftercnt += 1    
        grid[r][c] = '|'
        r += 1
    return r - 1


def fillside(r, c, dir):
    global aftercnt
    while (grid[r][c] == '|' or grid[r][c] == '.') and (grid[r+1][c] == '#' or grid[r+1][c] == '~'):
        if grid[r][c] == '.':
            aftercnt += 1
        grid[r][c] = '|'
        c = c + dir

    return c

def fillfrom(grid, r, c):
    #pour down
    tr = filldown(r, c)
    if tr == len(grid) -1:
        return False, []
    #fill left
    sources =[]
    lc = fillside(tr, c, -1)
    blockedL, blockedR = True, True
    if grid[tr][lc] == '.' or grid[tr][lc] == '|':
        sources.append((tr, lc))
        blockedL = False
    # fill right
    rc = fillside(tr, c, 1)
    if grid[tr][rc] == '.' or grid[tr][rc] == '|':
        sources.append((tr, rc))
        blockedR = False
    bothBlocked = blockedL and blockedR
    
    if bothBlocked:
        for col in range(lc +1, rc):
            grid[tr][col] = '~'

    return bothBlocked, sources

precnt = -1
aftercnt = 0

while aftercnt > precnt:
    #print('pre', precnt)
    used = set()

    unpoured = [(0, 500 - minx)]
    precnt = aftercnt
    while unpoured:
        sr, sd = unpoured.pop()

        if (sr, sd) not in used:
            used.add((sr,sd))
            bothBlocked = False
            nsource = []

            bothBlocked, nsource = fillfrom(grid, sr, sd)
            unpoured.extend(nsource)

            while bothBlocked and grid[sr][sd] != '~':
                bothBlocked, nsource = fillfrom(grid, sr, sd)
                if nsource:
                    unpoured.extend(nsource)
             #   print('in cont', sr, sd, aftercnt, nsource)
             #   printgrid(grid)
             #   print('')
        #print('end unpoured')
        
     #   print('cont false', unpoured)

    #print('after',aftercnt)


printgrid(grid)
grid[0][500 - minx] = '+'
cnt = 0
print(minr, maxr, len(grid))
for r in range(minr, min(maxr + 1, len(grid))):
    for c in range(len(grid[0])):
        if grid[r][c] == '|' or grid[r][c] == '~':
            cnt += 1
tildecnt = 0
for r in range(minr, min(maxr + 1, len(grid))):
    for c in range(len(grid[0])):
        if grid[r][c] == '~':
            tildecnt += 1
print(cnt)
print(tildecnt)