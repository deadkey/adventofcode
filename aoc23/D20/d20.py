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
    line = line.replace('->', ' ')
    return lazy_ints(multisplit(line, ' ,')) 

FF = 2
AND = 1

lo = 0
hi = 0
'''
from bp 3823
from xc 3847
from pd 3877
from th 4001
from bp 7646
from xc 7694
from pd 7754
from th 8002
'''

def p2(v):
    global hi, lo
    hi = 0
    lo = 0
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    
    g = {}
    sent = dd(list)
    state = dd(bool)

    t = dd(int)
    inc = dd(dict)
    steps = 0

    for i in range(len(data)):
        d = data[i]
        name = d[0]
        if name[0] == '%' or name[0] == '&':
            t[name[1:]] = AND if name[0] == '&' else FF
            name = name[1:]


        g[name] = []
        for con in d[1:]:
             
            g[name].append(con)
            inc[con][name] = 0
            
    
    def get(node):
        out, fr = sent[node][0]
        sent[node].pop(0)

        if node == 'zh' and out == 1:
            db('from', fr, steps)

        return out, fr
    
    def put(to, node, val):
        global hi, lo
        sent[to].append((val, node))
        if val == 1:
            hi += 1
        else:
            lo += 1

    def all1(node):
        for con, val in inc[node].items():
            if val == 0: return False
        return True
    
    N = 10000
    g['output'] = []
    
    g['rx'] = []

    for i in range(N):
        steps = i + 1

        q = ['broadcaster']
        put('broadcaster', 'button', 0)

        for node in q:
            #db('node', node, t[node])
            if t[node] == FF:
                val, _ = get(node)
                #db('val', val)
                if val == 0:
                    send = 0 if state[node] else 1
                    state[node] = not state[node]
                    for con in g[node]:
                        put(con, node, send)
                        q.append(con)
                    

            elif t[node] == AND:
                #rember previous
                val, fr = get(node)
                #db('val', val)
                inc[node][fr] = val
                send = 0 if all1(node) else 1
                #db('SENDS', send)
                for con in g[node]:
                    put(con, node, send)
                    q.append(con)
            else:
                #broadcoaster
                send, _ = get(node)
                #db('val', send)
                for con in g[node]:
                    put(con, node, send)
                    q.append(con)
                
    db('lo', lo)
    db('hi', hi)
    '''
    from bp 3823
from xc 3847
from pd 3877
from th 4001
from bp 7646
from xc 7694
from pd 7754
from th 8002
'''
    l = 1
    import math
    for val in [3823, 3847, 3877, 4001]:
        l = math.lcm(l, val)



    return l



def p1(v):
    global hi, lo
    hi = 0
    lo = 0
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    
    g = {}
    sent = dd(list)
    state = dd(bool)

    t = dd(int)
    inc = dd(dict)

    for i in range(len(data)):
        d = data[i]
        name = d[0]
        if name[0] == '%' or name[0] == '&':
            t[name[1:]] = AND if name[0] == '&' else FF
            name = name[1:]


        g[name] = []
        for con in d[1:]:
                
            g[name].append(con)
            inc[con][name] = 0
            
    
    def get(node):
        out, fr = sent[node][0]
        sent[node].pop(0)
        return out, fr
    
    def put(to, node, val):
        global hi, lo
        sent[to].append((val, node))
        if val == 1:
            hi += 1
        else:
            lo += 1

    def all1(node):
        for con, val in inc[node].items():
            if val == 0: return False
        return True
    
    N = 1000
    g['output'] = []
    g['rx'] = []

    for i in range(N):

        q = ['broadcaster']
        put('broadcaster', 'button', 0)

        for node in q:
            db('node', node, t[node])
            if t[node] == FF:
                val, _ = get(node)
                #db('val', val)
                if val == 0:
                    send = 0 if state[node] else 1
                    state[node] = not state[node]
                    for con in g[node]:
                        put(con, node, send)
                        q.append(con)
                    

            elif t[node] == AND:
                #rember previous
                val, fr = get(node)
                #db('val', val)
                inc[node][fr] = val
                send = 0 if all1(node) else 1
                db('SENDS', send)
                for con in g[node]:
                    put(con, node, send)
                    q.append(con)
            else:
                #broadcoaster
                send, _ = get(node)
                #db('val', send)
                for con in g[node]:
                    put(con, node, send)
                    q.append(con)
                
    db('lo', lo)
    db('hi', hi)
    
    


    return lo * hi



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,20, p1, p2, cmds)
if stats: print_stats()

#manual()
