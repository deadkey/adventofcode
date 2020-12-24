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

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())

def walk2(grid, r, c, di):
    WEAK= 'W'
    CLEAN = '.'
    INF = '#'
    FLAG= 'F'
    DIR = [(-1, 0), (0,1), (1, 0), (0, -1)]
    
    state = grid[r, c]
    if state == CLEAN: di -= 1
    if state == INF: di += 1
    if state == FLAG: di += 2
    di %= 4

    if state == CLEAN: grid[r, c] = WEAK
    if state == WEAK: grid[r, c] = INF
    if state == INF: grid[r, c] = FLAG
    if state == FLAG: grid[r, c] = CLEAN
    wasinf =  int(grid[r, c] == INF)
    r = r + DIR[di][0]
    c = c + DIR[di][1]
    return r, c, di, wasinf



def walk(grid, r, c, di):
    DIR = [(-1, 0), (0,1), (1, 0), (0, -1)]
    if grid[r,c] == '#':
        di += 1
    else:
        di -= 1
    di %= 4
    grid[r, c] = '#' if grid[r,c] == '.' else '.'
    r = r + DIR[di][0]
    c = c + DIR[di][1]
    return r, c, di, grid[r, c] == '.'


def ch(): return '.'

def p1(v):
    lines = v.strip().split('\n')
    gg = togrid(lines)
    grid = defaultdict(ch)
    for r in range(len(gg)):
        for c in range(len(gg[0])):
            grid[r,c] = gg[r][c]

    midR, midC = len(gg)//2, len(gg[0])//2
    N = 10000
    cuR, cuC = midR,midC

    inf= 0
    di = 0
    mnR, mxR = 0, len(gg)
    mnC, mxC = 0, len(gg[0])
    
    for _ in range(N):
        cuR, cuC, di, newinf = walk(grid,cuR, cuC , di)
        inf += newinf
        mnR = min(mnR,cuR)
        mnC = min(mnC,cuC)
        mxR = max(mxR,cuR)
        mxC = max(mxC,cuC)
    '''
    grid[cuR, cuC] = 'X'
    for r in range(mnR, mxR + 1):
        out =[]
        for c in range(mnC, mxC + 1):
            out.append(grid[r, c])
        db(''.join(out))
    '''

    return inf

def p2(v):
    lines = v.strip().split('\n')
    gg = togrid(lines)
    grid = defaultdict(ch)
    for r in range(len(gg)):
        for c in range(len(gg[0])):
            grid[r,c] = gg[r][c]

    midR, midC = len(gg)//2, len(gg[0])//2
    N = 10000000
    cuR, cuC = midR,midC

    inf= 0
    di = 0
    mnR, mxR = 0, len(gg)
    mnC, mxC = 0, len(gg[0])
    
    for _ in range(N):
        cuR, cuC, di, newinf = walk2(grid,cuR, cuC , di)
        inf += newinf
        mnR = min(mnR,cuR)
        mnC = min(mnC,cuC)
        mxR = max(mxR,cuR)
        mxC = max(mxC,cuC)
    '''
    grid[cuR, cuC] = 'X'
    for r in range(mnR, mxR + 1):
        out =[]
        for c in range(mnC, mxC + 1):
            out.append(grid[r, c])
        db(''.join(out))
    '''

    return inf



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2017,22, p1, p2, cmds)
if stats: print_stats()
#manual()
