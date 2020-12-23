import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math

from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def flip(grid):
    newgrid = []
    for row in grid:
        newgrid.append(row[::-1])
    return newgrid

def rot(grid):
    newgrid = []
    L = len(grid)
    for c in range(L):
        row = []
        for r in range(L-1, -1, -1):
            row.append(grid[r][c])
        newgrid.append(row)
    return newgrid

def db(*a): 
    if DB: print(*a)

def parse(line):
    left, right = line.split('=>')
    return left.strip(), right.strip()

def grid2str(g):
    out= []
    for row in g:
        out.append(''.join(row))
    return '/'.join(out)

def str2grid(s):
    return togrid(s.split('/'))

def getalt(s):
    grid= str2grid(s)
    alt = [grid]
    rotgrid = grid
    for i in range(3):
        rotgrid = rot(rotgrid)
        alt.append(rotgrid)
    rotgrid = flip(grid)
    alt.append(rotgrid)
    for i in range(3):
        rotgrid = rot(rotgrid)
        alt.append(rotgrid)
    return list(map(grid2str, alt))


def split2(grid):
    k = len(grid)
    out = []
    for r in range(0, k, 2):
        for c in range(0, k, 2):
            newgrid =[grid[r][c:c+2], grid[r+1][c:c+2]]
            out.append(newgrid)
    return out

def split3(grid):
    k = len(grid)
    out = []
    for r in range(0, k, 3):
        for c in range(0, k, 3):
            newgrid =[grid[r][c:c+3], grid[r+1][c:c+3], grid[r+2][c:c+3]]
            out.append(newgrid)
    return out

def apply(grid, rules):
    s = grid2str(grid)
    os = rules[s]

    return str2grid(os)

def merge(li):
    db('In merge ',li)
    R = len(li[0])
    out=[]
    for r in range(R):
        row = []
        for grid in li:
            row.extend(grid[r])
        out.append(row)
    return out


def p1(v):
    # Failed 115, too low
    start_str = open("start.txt", 'r').read().strip('\n').split('\n')
    grid = togrid(start_str)
    db(grid)
    lines = v.strip().split('\n')
    cnt = 0
    init_rules = [parse(line) for line in lines]
    rules = {}
    for left, right in init_rules:
        #db('Left = ',left)
        for alt in getalt(left):
            rules[alt] = right
    #db(rules)
    #db('Len of rules', len(rules))
    N = 5
    for _ in range(N):
        S = len(grid)
        if S % 2 == 0:
            newgrid = []
            li = split2(grid)
            db('Li in 2', li)
            applied = [apply(a, rules) for a in li]
            no_sq = S //2 #per line!

            for r in range(no_sq):
                merged = merge(applied[r * no_sq: (r+1) * no_sq])
                for row in merged:
                    newgrid.append(row)
        else:
            newgrid = []
            li = split3(grid)
            db('Li in 3', li)
            applied = [apply(a, rules) for a in li]
            db('applied ', applied)
            no_sq = S //3 #per line!
            for r in range(no_sq):
                merged = merge(applied[r * no_sq: (r+1) * no_sq])
                db('Merged', merged)
                for row in merged:
                    newgrid.append(row)
        db(newgrid)
        grid = newgrid
    for row in grid:
        cnt+= row.count('#')
    return cnt

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2017,21, p1, p2, cmds)
if stats: print_stats()
#manual()
