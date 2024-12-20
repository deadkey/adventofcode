import re
from itertools import chain, combinations
from collections import defaultdict as defdict, Counter

INF = 10**30

def togrid(lines): 
    grid = [list(line) for line in lines]
    return grid

def togoneintrid(lines): 
    grid = [[int(x) for x in list(line)] for line in lines]
    return grid

def tointgrid(lines): 
    grid = [list(map(int, line.split())) for line in lines]
    return grid, len(grid), len(grid[0])


def copygrid(grid):
    R = len(grid)
    nxt =[]
    for r in range(R):
        nxt.append(list(grid[r]))
    return nxt

def emptygrid(R, C, val):
    return [[val] * C for r in range(R)]

def cntgrid(grid, val):
    return sum(grid[r].count(val) for r in range(len(grid)))


def get4nb(r, c, rmin = -INF, rmax = INF, cmin = -INF, cmax = INF):
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb 

def grid4nb(r, c, grid):
    rmin = 0
    cmin = 0
    rmax = len(grid)
    cmax = len(grid[0])
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb     

def get8nb(r, c, rmin = -INF, rmax = INF, cmin = -INF, cmax = INF):
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb  


def grid8nb(r, c, grid):
    rmin = 0
    cmin = 0
    rmax = len(grid)
    cmax = len(grid[0])
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb     

def printgrid(grid):
    for r in range(len(grid)):
        out = ''.join(map(str, grid[r]))
        print(out)

def gridfind(grid, val):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == val:
                return r, c
    return -1, -1

def gridfindall(grid, val):
    all = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == val:
                all.append((r, c))
    return all

#### TURNS ####
# dir = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
# cw = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# ccw = [(0, 1), (-1, 0), (0, -1), (1, 0)]
def turnleft(dir):
    ccw = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(4):
        if ccw[i] == dir:
            return ccw[(i + 1) % 4]
        
def turnright(dir):
    cw = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(4):
        if cw[i] == dir:
            return cw[(i + 1) % 4]
        


def printdictxy(grid):
    INF = 10**12
    minx = min(grid.keys())[0]
    maxx = max(grid.keys())[0]
    
    miny = min(grid.keys(), key = lambda x: x[1])[1]
    maxy = max(grid.keys(), key = lambda x: x[1])[1]
   
    for y in range(miny, maxy + 1):
        out = []
        for x in range(minx, maxx + 1):   
            p = '#' if grid[x, y] == 1 else ' '
            out.append(p) 
        print(''.join(out))

def printdictrc(grid):
    INF = 10**12
    minx = min(grid.keys())[0]
    maxx = max(grid.keys())[0]
    
    miny = min(grid.keys(), key = lambda x: x[1])[1]
    maxy = max(grid.keys(), key = lambda x: x[1])[1]
   
    for x in range(minx, maxx + 1):
        out = []
        for y in range(miny, maxy + 1):   
            p = '#' if grid[x, y] == 1 else ' '
            out.append(p) 
        print(''.join(out))

def gridbfs(start, grid, target = None):

    if type(start) == list:
        q = start
    else:
        q = [start]
    dist = {}
    for start in q:
        dist[start] = 0
    
    while q:
        q2 = []
        for node in q:
            if target != None and node == target: return dist[node]
            r, c = node
            for ne in get4nb(r, c, rmin = 0, rmax = len(grid), cmin = 0, cmax = len(grid[0])):
                if grid[ne[0]][ne[1]] == '#': continue 
                if ne not in dist:
                    dist[ne] = dist[node] + 1
                    q2.append(ne)
        q = q2
    return dist   
