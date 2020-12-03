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

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(a):
    if DB: print(a)

def p1(v):
    lines = v.strip().split('\n')
    grid = []
    for line in lines:
        grid.append(list(line))
    cnt = 0
    r = 0
    c = 0
    for row in range(1, len(grid)):
        i = c + 3
        i %= len(grid[0])
        ch = grid[row][i]
        c = i
        if ch == '#':
            cnt += 1
    return cnt

def slope(v, dc, dr):
    lines = v.strip().split('\n')
    grid = []
    for line in lines:
        grid.append(list(line))
    cnt = 0
    r = 0
    c = 0
    for row in range(dr, len(grid), dr):
        i = c + dc
        i %= len(grid[0])
        ch = grid[row][i]
        c = i
        if ch == '#':
            cnt += 1
    return cnt

def p2(v):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res = []
    for dc, dr in slopes:
        r = slope(v, dc, dr)
        db(r)
        res.append(r)
    cnt = 1
    for r in res:
        cnt *= r
    return cnt


def manual():
    v = open("1.in", 'r').read().strip('\n')
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
    
    if not io: run_samples(p1, p2)
    if not so: run(get_year(),  get_day(), p1, p2, cmds)
    if stats: print_stats()
    #manual()
