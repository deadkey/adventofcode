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

def get_day(): return 7
def get_year(): return 2015
def db(*a):
    if DB: print(*a)

def AND(x, y):
    return int(x & y)

def OR(x, y):
    return int(x | y)

def NOT(x, y):
    return (2**16-1) ^ x

def LSHIFT(x, y):
    return x << y

def RSHIFT(x, y):
    return x >> y

def cp(x, y):
    return x


def parse(line):

    inss, to = line.split(' -> ')
    ins = inss.split()
    return *ins, to

#returns order so that edges only point forward in partial order
def topsort(g, nodes):
    ps=defaultdict(int)
    for k in g:
        ns = g[k]
        for n in ns:
            ps[n] += 1

    q =[k for k in nodes if ps[k] == 0]
    order = []
    while q:
        q2 = []
        for n in q:
            order.append(n)
            
            for p in g[n]:
                ps[p] -=1
                if ps[p] == 0:
                    q2.append(p)
        q =q2
    
    return order

def getval(x, wires):
    if isint(x):
        return int(x)
    return wires[x]

def p1(v):
    fun ={'AND': AND, 'OR': OR, 'LSHIFT': LSHIFT, 'RSHIFT': RSHIFT, 'NOT': NOT,  'cp': cp}
    lines = v.strip().split('\n')
    wires = defaultdict(int)
    g = defaultdict(list)
    nodes = set()
    
    conn = {}
    for line in lines:
        if 'NOT' in line:
            op, x, to = parse(line)
            conn[to] = (x, op, None)
            g[x].append(to)
            
            nodes |= set([x, to])
        elif 'AND' in line or 'OR' in line:
            x, op, y, to = parse(line)
            conn[to] = (x, op, y)
            
            g[x].append(to)
            g[y].append(to)

            nodes |= set([x,y,  to])
        elif 'LSHIFT' in line or 'RSHIFT' in line:
            x, op, y, to = parse(line)
            conn[to] = (x, op, int(y))
            wires[int(y)] = int(y)
            g[x].append(to)
            nodes |= set([x, to])
        else:
            x, to = parse(line)
            if isint(x):
                wires[to] = int(x)
                db('Added int to ', x, to)
            else:
                conn[to] = (x, 'cp', 2)
                g[x].append(to)
                nodes |= set([x, to])
    
    order = topsort(g, nodes)
    #db('order', order)
    #drawgraph.draw(g, order)
    
    for node in order:
        if node in conn:
            c = conn[node]
            #db(c)
            x, op, y = c
            vx = getval(x, wires)
            vy = getval(y, wires)
            f = fun[op]
            wires[node] = f(vx, vy)
        else:
            db('No conn', node, wires[node])
    db(wires)
    return wires['a']
    

def p2(v):
    resA = 3176
    fun ={'AND': AND, 'OR': OR, 'LSHIFT': LSHIFT, 'RSHIFT': RSHIFT, 'NOT': NOT,  'cp': cp}
    lines = v.strip().split('\n')
    wires = defaultdict(int)
    g = defaultdict(list)
    nodes = set()
    
    conn = {}
    for line in lines:
        if 'NOT' in line:
            op, x, to = parse(line)
            conn[to] = (x, op, None)
            g[x].append(to)
            
            nodes |= set([x, to])
        elif 'AND' in line or 'OR' in line:
            x, op, y, to = parse(line)
            conn[to] = (x, op, y)
            g[x].append(to)
            g[y].append(to)

            nodes |= set([x,y,  to])
        elif 'LSHIFT' in line or 'RSHIFT' in line:
            x, op, y, to = parse(line)
            conn[to] = (x, op, int(y))
            wires[int(y)] = int(y)
            g[x].append(to)
            nodes |= set([x, to])
        else:
            x, to = parse(line)
            if isint(x):
                wires[to] = int(x)
            else:
                conn[to] = (x, 'cp', 2)
                g[x].append(to)
                nodes |= set([x, to])
    
    wires['b'] = resA
    order = topsort(g, nodes)
    db('order', order)
    #drawgraph.draw(g, order)
    
    assert len(order) == len(nodes)
    for node in order:
        if node in conn:
            c = conn[node]
            #db(c)
            x, op, y = c
            vx = getval(x, wires)
            vy = getval(y, wires)
            f = fun[op]
            wires[node] = f(vx, vy)
        else:
            wires[node] = getval(node, wires)
    return wires['a']
    



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
