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

def parse(s):
    li = []
    for b in s:
        if 'no other' in b:
            continue
        b = b.strip()
        data = b.split()
        no = int(data[0])
        name = ' '.join(data[1:-1])
        li.append((no, name.strip()))
    return li


def p1(v):
    mybag = 'shiny gold'
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    g = defaultdict(list)
    parent = defaultdict(list)
    nodes = set()
    for line in lines:
        out, inner = line.split('contain')
        out = ' '.join(out.split()[0:2])
        inner = inner.split(',')
        inside = parse(inner)
        #db(out, inside)
        g[out].append(inside)
        for no, b in inside:
            parent[b].append(out)
    #db(parent)
    ps = set()
    q = list(parent[mybag])
    seen = set()
    while q:
        q2 = []
        for b in q:
            ps.add(b)
            if b not in seen:
                seen.add(b)
                for par in parent[b]:
                    q2.append(par)
        q = q2

    return len(ps)

def count(bag, seen, g):
    q = list(g[bag])
    c = 1
    #db('q', q)
    
    for no, b in q:
        #db('List', no, 'b', b, 'q', g)
        if not b in seen:
            
            res = count(b, seen, g)
            c += no * res
            seen[b] = res
        else:
            c += no * seen[b]
        
    return c

def p2(v):
    mybag = 'shiny gold'
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    g = defaultdict(list)
    parent = defaultdict(list)
    nodes = set()
    for line in lines:
        out, inner = line.split('contain')
        out = ' '.join(out.split()[0:2])
        inner = inner.split(',')
        inside = parse(inner)
        #db(out, inside)
        g[out].extend(inside)
        for no, b in inside:
            parent[b].append(out)
    #db(parent)
    seen = {}
    cnt = count(mybag, seen, g)

    return cnt -1


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
