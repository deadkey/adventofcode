import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return 0 #int(line)

def nxt(no, MULT, MOD):
    return (no * MULT) % MOD

def printgrid(grid):
    for r in range(len(grid)):
        out = []
        for c in range(len(grid[0])):
            value = grid[r][c]
            out.append(f'{value:8d}')
        print(' '.join(out))



def p1(v):
    # Enter the code at row 2978, column 3083.
    no = 20151125
    MULT= 252533
    MOD = 33554393
    #NOT 5920668 too high
    r, c = 0, 0
    D = 1
    while True:
       
        if r ==  2977 and c == 3082:
            return no
        no = nxt(no, MULT, MOD)
        r -= 1
        c += 1
        if c == D:
            
            D += 1
            r = D-1
            c = 0
            db(D, 2978 + 3082)
            

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,25, p1, p2, cmds)
if stats: print_stats()
#manual()
