import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def get_day(): return 8
def get_year(): return 2015
def db(*a):
    if DB: print(*a)

def diff(v):
    code = len(v)
    v = v[1:-1]
    slashes = re.findall('\\\\\\\\', v)
    
    quotes = re.findall('\\\\"', v)
    
    matches = re.findall('\\\\x[0-9a-f]{2}', v)
    s = code -2 - len(slashes) - len(quotes) - 3 * len(matches) 
    return code - s

def diff2(v):
    code = len(v)
    v = v[1:-1]
    slashes = re.findall('\\\\\\\\', v)
    quotes = re.findall('\\\\"', v)
    
    matches = re.findall('\\\\x[0-9a-f]{2}', v)
    enc = code + 4 +  2 * len(slashes) + 2 * len(quotes) + len(matches)
    db(v, ' code ', code, ' enc ', enc)
    return enc - code

def p1(v):

    lines = v.strip().split('\n')
    cnt = 0
    for line in lines:
        d2 = diff(line)
        cnt += d2
    return cnt

def p2(v):
    lines = v.strip().split('\n')
    cnt = 0
    for line in lines:
        d2 = diff2(line)
        cnt += d2
    return cnt


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
