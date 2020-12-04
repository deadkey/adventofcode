import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: '))
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def get_day(): return 8 #date.today().day
def get_year(): return 2016#date.today().year
def db(*a):
    if DB: print(*a)

def p1(v):
    lines = v.strip().split('\n')
    grid = [[' '] * 50 for _ in range(6)]
    for cmd in lines:
        if cmd.startswith('rotate row'):
            y, B = stripall(cmd)
            
            rotrow(y, B, grid)
        if cmd.startswith('rotate column'):
            y, B =stripall(cmd)
            rotcol(y, B, grid)
        if cmd.startswith('rect'):
            A, B = stripall(cmd)
            rect(A, B, grid)
        
        
    cnt = 0
    for r in range(len(grid)):
        cnt += grid[r].count('#')
    return cnt

def rect(A, B, grid):
    for r in range(B):
        for c in range(A):
            grid[r][c] = '#'


def rotrow(r, B, grid):
    orig = list(grid[r])
    for i, ch in enumerate(orig):
        ni = (i + B) % len(grid[0])
        grid[r][ni] = ch

def rotcol(c, B, grid):
    orig = list(grid[r][c] for r in range(0, len(grid)))
    for i, ch in enumerate(orig):
        ni = (i + B) % len(grid)
        grid[ni][c] = ch

def stripall(s):
    li = removeall(s, ['rotate row', 'rotate column', 'x=', 'y=', 'x', 'by', 'rect']).split()
    return lazy_ints(li)
    


def p2(v):
 
    lines = v.strip().split('\n')
    grid = [[' '] * 50 for _ in range(6)]
    for cmd in lines:
        if cmd.startswith('rotate row'):
            y, B = stripall(cmd)
            
            rotrow(y, B, grid)
        if cmd.startswith('rotate column'):
            y, B =stripall(cmd)
            rotcol(y, B, grid)
        if cmd.startswith('rect'):
            A, B = stripall(cmd)
            rect(A, B, grid)
        
  
    printgrid(grid)
    return 0


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    res1 = p1(v)
    res2 = p2(v)
    print('part_1: {}'.format(res1))
    print('part_2: {}'.format(res2))

FF = "force fetch"
DB = 0
PR = "print input"
so = 0
io = 0
stats = 0
cmds = []

def get_args():
    global stats, so, io, DB    
    for arg in sys.argv[1:]:
        if arg == 'f':
           cmds.append(FF)
        if arg == 's1' or  arg == '1':
           cmds.append("submit1")
        if arg == 's2' or arg == '2':
           cmds.append("submit2")
        if arg == 'p' or arg == 'pi':
           cmds.append(PR)
        if arg == 'so':
            so = 1
        if arg == 'io':
            io = 1
        if arg == 'db':
            DB = 1
        if arg == 'st' or arg == 'stat' or arg == 'stats':
            stats = 1
        if arg == 'p1' or arg == 'part1':
            cmds.append('p1')
        if arg == 'p2' or arg == 'part2':
            cmds.append('p2')
        

if __name__ == '__main__':
    get_args()
    
    if not io: run_samples(p1, p2, cmds)
    if not so: run(get_year(),  get_day(), p1, p2, cmds)
    if stats: print_stats()
    #manual()
