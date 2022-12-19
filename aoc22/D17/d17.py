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

s = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""   

def put(pos, block, grid):
    x, y = pos
    mx = 0
    for dy, line in enumerate(block[::-1]):
        for dx, ch in enumerate(line):
            if ch == '#':
                xx = x+dx
                yy = y + dy
                grid[xx, yy] = 1
                mx = max(yy, mx)

    return mx

def collide(newpos, block, grid):
    #walls
    x, y = newpos
    L = 0
    for line in block:
        L = max(L, len(line))
    x = max(x, 0)
    x = min(x, 7 - L)
    
    if x != newpos[0]: return True
    if y == -1: return True
    
    for dy, line in enumerate(block[::-1]):
        for dx, ch in enumerate(line):
            if ch == '#':
                xx = x + dx
                yy = y + dy
                space = grid[xx, yy]
                if space == 1:
                    return True
    return False



def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    moves = data[0]
    blocks = []
    ss = s.split('\n\n')
    for ch in ss:
        l = ch.split('\n')
        blocks.append([])
        for line in l:
            blocks[-1].append(line)
    #db(blocks)

    N = 1000000000000
    time = 0
    cnt = 0
    mx = 0
    pos = 2, 3
    grid = dd(int)
    grid[0, 0] = 0
    grid[6, 0] = 0

    reps = {}
    tot = 0
    CNT, MX = 0, 0
    

    while cnt < N:
        #each move one push and one fall
        block = blocks[cnt % len(blocks)]
        '''
        db(f'Pos before anything {pos}')
        db(f'_____________Time {time}__________________')    
        printdictxy(grid, pos, block)
        '''
        dx = 1 if moves[time % len(moves)] == '>' else -1
        
        alt = pos[0] + dx, pos[1]
        
        if not collide(alt, block, grid):
            pos = alt
        
        '''
        db(f'Pos before falling {pos}')
        db(f'_____________Time {time}__________________')    
        printdictxy(grid, pos, block)
        '''   
        #down
        


        if collide((pos[0], pos[1] -1), block, grid):
            #stop block
            altmx = put(pos, block, grid)
            mx = max(altmx, mx)
            '''
            db(f'Block no {cnt} stopped after {time} moves at pos {pos}')

            db(f'Pos after move {pos}')
            db(f'_____________Time {time}__________________')    
            printdictxy(grid, pos, block)
            '''
            key = cnt% len(blocks), time % len(moves)
            
            if key in reps:
                oldmx, oldcnt = reps[key]
                dh = mx - oldmx
                dc = cnt - oldcnt
                tot += 1
                db('dh dc', dh, dc)

            
            reps[key] = (mx, cnt)

            if tot >= 1000:
                CNT = cnt
                MX = mx
                left = N - cnt -1
                if left % dc == 0:
                    break

            
            cnt += 1
            pos = 2, mx + 4
            block = blocks[cnt % len(blocks)]

        else:
            pos = pos[0], pos[1] -1
            '''
            db(f'Pos after move {pos}')
            db(f'_____________Time {time}__________________')    
            printdictxy(grid, pos, block)
            '''
        time += 1

    left = N - CNT
    k = left // dc
    mx += k * dh
    

    return mx + 1


def printdictxy(orig, pos, block):
    from copy import copy

    grid = copy(orig)
    INF = 10**12
    minx = min(grid.keys())[0]
    maxx = max(grid.keys())[0]
    put(pos, block, grid)

    
    miny = min(grid.keys(), key = lambda x: x[1])[1]
    maxy = max(grid.keys(), key = lambda x: x[1])[1]
    all = []
   
    for y in range(miny, maxy + 1):
        out = []
        for x in range(minx, maxx + 1):   
            p = '#' if grid[x, y] == 1 else '.'
            out.append(p) 
        all.append((''.join(out)))
    db('\n'.join(all[::-1]))



def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    moves = data[0]
    blocks = []
    ss = s.split('\n\n')
    for ch in ss:
        l = ch.split('\n')
        blocks.append([])
        for line in l:
            blocks[-1].append(line)
    #db(blocks)

    N = 2022
    time = 0
    cnt = 0
    mx = 0
    pos = 2, 3
    grid = dd(int)
    grid[0, 0] = 0
    grid[6, 0] = 0
    

    while cnt < N:
        #each move one push and one fall
        block = blocks[cnt % len(blocks)]
        '''
        db(f'Pos before anything {pos}')
        db(f'_____________Time {time}__________________')    
        printdictxy(grid, pos, block)
        '''
        dx = 1 if moves[time % len(moves)] == '>' else -1
        
        alt = pos[0] + dx, pos[1]
        
        if not collide(alt, block, grid):
            pos = alt
        
        '''
        db(f'Pos before falling {pos}')
        db(f'_____________Time {time}__________________')    
        printdictxy(grid, pos, block)
        '''   
        #down
        


        if collide((pos[0], pos[1] -1), block, grid):
            #stop block
            altmx = put(pos, block, grid)
            mx = max(altmx, mx)
            '''
            db(f'Block no {cnt} stopped after {time} moves at pos {pos}')

            db(f'Pos after move {pos}')
            db(f'_____________Time {time}__________________')    
            printdictxy(grid, pos, block)
            '''
            
            cnt += 1
            pos = 2, mx + 4
            block = blocks[cnt % len(blocks)]

        else:
            pos = pos[0], pos[1] -1
            '''
            db(f'Pos after move {pos}')
            db(f'_____________Time {time}__________________')    
            printdictxy(grid, pos, block)
            '''
        time += 1

    return mx + 1




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,17, p1, p2, cmds)
if stats: print_stats()

#manual()
