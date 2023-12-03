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

def fill(adj, row, col):
    for rr in range(row-1, row+2):
        for cc in range(col -1, col +2):
            rr = max(0, rr)
            rr = min(len(adj), rr)
            cc = max(0, cc)
            cc = min(len(adj[0]), cc)
            adj[rr][cc] = 1

def fillrow(adj, grid, row, col):
    c = col
    while c < len(adj[0]) and '0' <= grid[row][c] <= '9':
        adj[row][c] = 1
        c += 1
    c = col
    while c >= 0 and '0' <= grid[row][c] <= '9':
        adj[row][c] = 1
        c -= 1
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    grid = togrid(lines)
    su = 0
    R = len(grid)
    C = len(grid[0])
    adj = [[0 for c in range(C)] for r in range(R)]
    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            if letter != '.' and not '0' <= letter <= '9':
                fill(adj, r, c)

    db('symbols')
    db(adj)
    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            if adj[r][c]:
                fillrow(adj, grid, r, c)
    db('digits')    
    db(adj)
    num = 0
    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            
            if adj[r][c] == 1 and '0' <= letter <= '9':
                num *= 10
                
                num += int(letter)
            else:
                su += num
                num = 0
        if num:
            su += num
            num = 0
        
    return su


def p2(v):

    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    grid = togrid(lines)
    su = 0
    R = len(grid)
    C = len(grid[0])

    stars = set()
    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            if letter == '*':
                stars.add((r, c))
  
    for star in stars:
        r, c= star
        adj = [[0 for c in range(C)] for r in range(R)] 
       
        fill(adj, r, c)

        for r, row in enumerate(grid):
            for c, letter in enumerate(row):
                if adj[r][c]:
                    fillrow(adj, grid, r, c)
        
        n = []

        num = 0
        for r, row in enumerate(grid):
            for c, letter in enumerate(row):
                
                if adj[r][c] == 1 and '0' <= letter <= '9':
                    num *= 10
                    
                    num += int(letter)
                elif num:
                    n.append(num)
                    num = 0
            if num:
                n.append(num)
                num = 0
        db(n)
        if len(n) == 2:
            su += n[0] * n[1]
        
    return su


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,3, p1, p2, cmds)
if stats: print_stats()

#manual()
