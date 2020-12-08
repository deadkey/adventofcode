import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(*a):
    if DB: print(*a)

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    ins = []
    cnt = 0

    for line in lines:
        i, val = lazy_ints(line.split())
        ins.append((i, val))
    used = [False] * len(ins)
    db(ins)
    accu = 0
    cont = True
    curr = 0
    while cont:
        i, val = ins[curr]
        if used[curr]:
            return accu
        used[curr] = True
        db(i, val)
        if i == 'acc':
            accu += val
            curr += 1
        elif i == 'jmp':
            curr += val
        elif i == 'nop':
            curr += 1
        

    
    return cnt

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    #print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
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
