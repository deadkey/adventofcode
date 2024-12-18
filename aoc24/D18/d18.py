import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict as defdict, Counter
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
    return lazy_ints(multisplit(line, ',')) 

def printpath(path, grid, end):
    node = end
    while node:
        r, c = node
        grid[r][c] = 'O'
        node = path[node]
    printgrid(grid)



def bfs(start, grid, end):
    q = [start]
    visited = set()
    for node in q:
        visited.add(node)
    steps = 0
    path = defdict(lambda: None)
    while q:
        q2 = []

        for node in q:
            r, c = node
            if node == end:
                #printpath(path, grid, end)
                return steps
            for ne in get4nb(r, c, rmin = 0, rmax = len(grid), cmin = 0, cmax = len(grid[0])):
                if grid[ne[0]][ne[1]] == '#':
                    continue
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
                    path[ne] = node
        q = q2
        steps += 1
    #printpath(path, grid, end)
    return -1

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    N = 71
    grid = emptygrid(N, N, '.')

    su = 0
    start = (0, 0)
    end = (N-1, N-1)
    for i in range(len(data)):
        c, r = data[i]
        grid[r][c] = '#'
        steps = bfs(start, grid, end)
        if steps == -1:
            return f'{c},{r}'
            

    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    N = 71
    grid = emptygrid(N, N, '.')

    su = 0
    for i in range(1024):
        c, r = data[i]
        grid[r][c] = '#'
    start = (0, 0)
    end = (N-1, N-1)


    return bfs(start, grid, end)



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2024,18, p1, p2, cmds)
if stats: print_stats()

#manual()
