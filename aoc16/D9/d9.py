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

def get_day(): return 9
def get_year(): return 2016
def db(*a):
    if DB: print(*a)

def nxt(s, i):
    for ii in range(i, len(s)):
        if s[ii] == ')':
            return ii
    return len(s)

def label(s):
    s = removeall(s, '(', ')')
    no, ti = lazy_ints(s.split('x'))
    return no, ti


def p1(v):
    lines = v
    print(lines)
    change = True
    
    while change:
        o = []
        change = False
        i = 0
        while i < len(lines):
            ch = lines[i]
            if ch == '(':
                
                end = nxt(lines, i)
                no, x = label(lines[i:end])
                chunk = lines[end+1: min(end +1 +  no, len(lines))]
                for i in range(x):
                    o.append(chunk)
                print(no, x, chunk)

                i = end +  no
            else:
                o.append(ch)
            i += 1
        lines = ''.join(o)
        print(lines)

                

    return len(lines)

def expand(chunk):
    i = 0
    su = 0
    while i < len(chunk):
        ch = chunk[i]
        if ch == '(':
            
            end = nxt(chunk, i)
            no, x = label(chunk[i:end])
            inner = chunk[end+1: min(end +1 +  no, len(chunk))]
            su += x * expand(inner)

            i = end +  no + 1
        else:
            i += 1
            su += 1
    return su

def p2(v):
    
    lines = v
    return expand(lines)
        


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
