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
    return lazy_ints(multisplit(line, ' ')) 


def bfs(q, grid, letter):
    visited = set()
    for node in q:
        visited.add(node)
    while q:
        q2 = []
        for node in q:
            for ne in get4nb(node[0], node[1], 0, len(grid), 0, len(grid[0])):

                if ne not in visited and grid[ne[0]][ne[1]] == letter:
                    visited.add(ne)
                    q2.append(ne)
        q = q2
    return visited

def calcarea(r, c, grid, letter):
    return bfs([(r, c)], grid, letter)


def calcperim(r, c, grid, area, letter):
    perims = 0
    for r, c in area:
        perims += 4
        for ne in get4nb(r, c, 0, len(grid), 0, len(grid[0])):
            nr, nc = ne
            if grid[nr][nc] == letter:
                perims -= 1
    return perims

def calcperim2(r, c, grid, area, letter):
    
    edges = set()
    for r, c in area:
        for ne in get4nb(r, c):
            nr, nc = ne
            if (nr, nc) not in area:
                edges.add(((r, c), ne))
    return edges

def calcsides(edges):
    su = 0
    for e in edges:
        e1, e2 = e
        r, c = e1
        r2, c2 = e2
        alt1 = (r-1, c), (r2-1, c2)
        alt2 = (r, c-1), (r2, c2-1)
        if alt1 in edges: continue
        if alt2 in edges: continue
        su += 1
    return su

def calc(grid, letters, part1 = True):
    areas = []
    perims = []
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) in visited: continue
            letter = grid[r][c]
            area = calcarea(r, c, grid, letter)
            visited |= area
            if part1:
                perim = calcperim(r, c, grid, area, letter)
                perims.append(perim)
            else:
                edges = calcperim2(r, c, grid, area, letter)
                sides = calcsides(edges)
                perims.append(sides)
            areas.append(len(area))
            
    return areas, perims



def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    letters = set()

    su = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            letters.add(grid[r][c])

    areas, perims = calc(grid, letters, part1 = False)
    
    db('perims', perims)

    for a, p in zip(areas, perims):
        su += a * p
    return su

def p1(v):

    lines = v.strip().split('\n')
    chunks = tochunks(v)
    grid = togrid(lines)
    letters = set()

    su = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            letters.add(grid[r][c])

    areas, perims = calc(grid, letters, part1 = True)
    
    db('area', areas)
    db('perims', perims)

    for a, p in zip(areas, perims):
        su += a * p
    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,12, p1, p2, cmds)
if stats: print_stats()

#manual()
