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
    #return lazy_ints(line.split())
    return lazy_ints(multisplit(line, ' ')) 

N= 0
S = 1
W = 2
E = 3

def empty(grid, elf, d):
    nr, nc = elf
    if d == N:
        nr = elf[0] -1
        return grid[nr,nc-1] + grid[nr,nc] + grid[nr,nc+1] == 0 
    if d == S:
        nr = elf[0] +1
        return grid[nr,nc-1] + grid[nr,nc] + grid[nr, nc+1] == 0 

    if d == W:

        nc = elf[1] -1
        return grid[nr-1,nc] + grid[nr,nc] + grid[nr+1,nc] == 0 
    if d == E:

        nc = elf[1] +1
        return grid[nr-1,nc] + grid[nr,nc] + grid[nr+1,nc] == 0 
    return False

def count(grid, elf):
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    cnt = 0
    r, c = elf
    for dr, dc in diff:
        cnt += grid[r+dr, c + dc]
    return cnt 

def findpos(grid, elf, order):
    if count(grid, elf) == 0: 
        db('elf', elf, 'stays')
        return elf

    for dir in range(4):
        d = (order + dir) % 4
        db('First direction ', d, order)
        if d == N:
            if empty(grid, elf, d): 
                db('elf', elf, 'goes N')
                nr, nc = elf
                nr -= 1
                db('Count',  grid[nr,nc-1] + grid[nr,nc] + grid[nr,nc+1])
                return elf[0] - 1, elf[1]
        if d == S:
            if empty(grid, elf, d): 
                
                db('elf', elf, 'goes S')
                return elf[0] + 1, elf[1]
        if d == W:
            if empty(grid, elf, d): 
                
                db('elf', elf, 'goes W')
                nr, nc = elf
                nc = elf[0] -1
                db('Count', grid[nr-1,nc] + grid[nr,nc] + grid[nr+1,nc])
                return elf[0], elf[1] -1
        if d == E:
            if empty(grid, elf, d): 
                
                db('elf', elf, 'goes E')
                return elf[0], elf[1] + 1
    
    db('elf', elf, 'goes stays')
    return elf
        

def play(n, grid, elves):

    order = N

    for step in range(n):
        decide = dd(list)
        
        for elf in elves:
            ch = findpos(grid, elf, order)
            decide[ch].append(elf)

        nxt = dd(int)
        move = {}
        newpos = set()
        for key, li in decide.items():
            if len(li) == 1:
                move[li[0]] = key
                
        for elf in elves:
            if elf in move:
                nxt[move[elf]] = 1
                newpos.add(move[elf])
            else:
                nxt[elf] = 1
                newpos.add(elf)
        grid = nxt
        elves = newpos
        order += 1
        order %= 4


    return elves, grid



def play2(grid, elves):

    order = N

    step = 0
    while True:
        decide = dd(list)
        no = 0
        for elf in elves:
            ch = findpos(grid, elf, order)
            if ch != elf:
                no += 1
            decide[ch].append(elf)

        nxt = dd(int)
        move = {}
        newpos = set()
        for key, li in decide.items():
            if len(li) == 1:
                move[li[0]] = key
                
        for elf in elves:
            if elf in move:
                nxt[move[elf]] = 1
                newpos.add(move[elf])
            else:
                nxt[elf] = 1
                newpos.add(elf)
        grid = nxt
        elves = newpos
        order += 1
        order %= 4
        step += 1
        if no == 0:
            return step


    return -1


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = dd(int)
    elves = set()
    for i in range(len(data)):
        d = data[i]
        for k in range(len(d)):
            grid[i, k] = 1 if d[k] == '#' else 0
            if d[k] == '#': elves.add((i, k))
    
    elves, nxt = play(10, grid, elves)


    minx = min(elves)[0]
    maxx = max(elves)[0]

    miny = min(elves, key = lambda x: x[1])[1]
    maxy = max(elves, key = lambda x: x[1])[1]
   
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):   
            if grid[x, y] == 0: su += 1    

    return su



def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    grid = dd(int)
    elves = set()
    for i in range(len(data)):
        d = data[i]
        for k in range(len(d)):
            grid[i, k] = 1 if d[k] == '#' else 0
            if d[k] == '#': elves.add((i, k))
    
    return play2(grid, elves)




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,23, p1, p2, cmds)
if stats: print_stats()

#manual()
