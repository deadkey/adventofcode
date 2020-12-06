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

def get_day(): return 10
def get_year(): return 2016
def db(*a):
    if DB: print(*a)

def kv(line):
    line = removeall(line, 'value', 'goes to')
    line = line.replace('bot ', 'bot').replace('output ', 'output')
    vals =lazy_ints(line.split())
    return vals[0], vals[1]

def blohi(line):
    line = removeall(line, 'gives low to', 'and high to')

    line = line.replace('bot ', 'bot').replace('output ', 'output')
    vals =lazy_ints(line.split())
    return vals[0], vals[1], vals[2]

def p1(v):
    lines = v.strip().split('\n')
    instr = lines.sort(reverse = True)
    direct = {}
    botrules = {}
    has = defaultdict(list)
    for line in lines:
        #db(line)
        if line.startswith('value'):
            k, v = kv(line)
            direct[k] = v
            has[v].append(k)
        else:
            b, lo, hi = blohi(line)
            #db(b, lo, hi)
            botrules[b] = (lo, hi)
            
            
    
    targetlo = 17
    targethi = 61
    #targetlo = 2
    #targethi = 5
    
    #simulate
    db('No bots', len(has))
    
    
    
    while True:
        has2 = defaultdict(list)
        for b in has:
            if len(has[b]) == 2:

                lo, hi = min(has[b]), max(has[b])
                db('Process ', b, lo, hi, has[b])
                has[b] = []
                b1 =botrules[b][0]
                b2 = botrules[b][1]
                has2[b1].append(lo)
                has2[b2].append(hi)
                db(b1, b2)
                if targetlo == lo and targethi == hi and b.startswith('bot'):
                    id = int(b.replace('bot', ''))
                    return id
                
            else:
                has2[b].append(has[b][0])
        has = has2
            
                

                
                


    
    return 0

def p2(v):
    lines = v.strip().split('\n')
    instr = lines.sort(reverse = True)
    direct = {}
    botrules = {}
    has = defaultdict(list)
    for line in lines:
        #db(line)
        if line.startswith('value'):
            k, v = kv(line)
            direct[k] = v
            has[v].append(k)
        else:
            b, lo, hi = blohi(line)
            #db(b, lo, hi)
            botrules[b] = (lo, hi)
    q = []        
    for b in has:
        if len(has[b]) == 2:q.append(b)
    while q:
        change = False
        b = q.pop()

        lo, hi = min(has[b]), max(has[b])
        db('Process ', b, lo, hi)
        has[b] = []
        b1 =botrules[b][0]
        b2 = botrules[b][1]
        has[b1].append(lo)
        if len(has[b1]) == 2: q.append(b1) 
        has[b2].append(hi)

        if len(has[b2]) == 2: q.append(b2)
        db(b1, b2)
        

    su = 1
    for v in range(0, 3):
        nm = 'output' + str(v)
        db(nm, has[nm])
        for val in has[nm]:
            su *= val
    return su
                
            

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
