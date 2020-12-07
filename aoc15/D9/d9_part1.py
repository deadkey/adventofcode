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

def get_day(): return 9
def get_year(): return 2015
def db(*a):
    if DB: print(*a)

def travel(x, left, dists):
    best = 0

    if not left: return 0
    for nx in left:
        alt = dists[x, nx]
        new_left = set(left)
        new_left.discard(nx)
        alt_rest = travel(nx, new_left, dists)
        alt += alt_rest
        best = max(best, alt)
    return best

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    g = defaultdict(list)
    dists = {}
    for line in lines:
        fr, to, di = lazy_ints(multisplit(line, 'to', '='))
        g[fr].append((to, di))
        g[to].append((fr, di))
        dists[(fr, to)] = di
        dists[(to, fr)] = di
        
    
    nodes = g.keys()
    best = 0
    for node in nodes:
        left = set(nodes)
        left.discard(node)
        alt = travel(node, left, dists)
        best = max(best, alt)

    return best

def p2(v):
    return p1(v)


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
