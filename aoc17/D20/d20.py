import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *

from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line = replaceall(line, '=', 'p', 'v', 'a', '<', '>', ',', ' ')
    ints =  lazy_ints(line.split())
    return ints[0:3], ints[3:6], ints[6:] 



def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    data = [parse(line) for line in lines]
    li = [(abs(ax) + abs( ay) + abs(az), i) for i,( _, _, (ax, ay, az)) in enumerate(data)]
    li.sort()
    return li[0][1]

def oned(p1, p2, v1, v2):
    if (v1 - v2) == 0:
        return []

    t1 = (p2 - p1)/(v1-v2)
    #if t1 > 1000:
        #db('Coll time', t1)
    if isint(t1): 
    
        return [int(t1)]
    elif abs(t1 - int(t1)) > 0.999:
        db('WUUUUUUUUUUUUUUT', t1)
    return []

def sign(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0

def solve_bin(p1, p2, v1, v2, a1, a2):
    lo = 0
    hi = 10
    def dx(t):
        return calctime(p1, v1, a1, t) - calctime(p2, v2, a2, t)
    s = sign(dx(0))
    if dx(lo)*dx(hi) > 0: return None
    while lo < hi:
        mid = (lo + hi + 1)//2
        dl = sign(dx(lo))
        dm = sign(dx(mid))
        db(mid, dl, dm)
        if dl == 0: return [lo]
        if dm == 0: return mid
        if dl*dm > 0:
            lo = mid + 1
        else:
            hi = mid - 1
    if dx(lo) == 0: return lo
    return []

def solve(p1, p2, v1, v2, a1, a2):
    
    #db('p1, p2 ...', p1, p2, v1, v2, a1, a2)
    a = (a1 - a2)/2
    if a == 0:
        return oned(p1, p2, v1, v2)
    b = (a1 - a2)/2 + v1 - v2
    c = p1 - p2
    p = b/a
    q = c/a
    if (p/2) **2 - q >= 0:
        v = (p**2 - 4*q) ** (0.5)
        t1 = (- p + v)/2
        t2 = (- p - v)/2
        t1i = int(round(t1))
        t2i = int(round(t2))
        out = []
        if abs(t1 - t1i) < 0.000001: out.append(t1i)
        if abs(t2 - t2i) < 0.000001: out.append(t2i)
        return out
    return []

def calctime(p1, v1, a1, t):
    pt =  p1 + t * v1 + (t * (t +1) * a1) //2
    return pt

def sim(T, D, data, colltimes):
    temppos = [[] for _ in range(D)]
    tempvel = [[] for _ in range(D)]
    for d in range(D):
        temppos[d]  = data[d][0]
        v = data[d][1]
        tempvel[d] = v
    left = set(range(D))
    for t in range(1, T):
        positions = defaultdict(list)
        for d in range(D):
            if d not in left: continue
            poss = []
            for i in range(3):
                poss.append(calctime(data[d][0][i], data[d][1][i], data[d][2][i], t))
            positions[tuple(poss)].append(d)
        dbdie = set()
        for pair in colltimes[t]:
            dbdie |= set(pair)
        
        die = set()
        for k, v in positions.items():
            if len(v) > 1:
                die |= set(v)
                for d in v:
                    if d not in dbdie:
                        poss = []
                        for i in range(3):
                            poss.append(calctime(data[d][0][i], data[d][1][i], data[d][2][i], t))
                        db('Found error ', t, d, k, ' it is at ', poss, ' data ', data[d][0], data[d][1], data[d][2])
                        db(v)
                        exit()
        for d in die:
            left.remove(d)
       
        
    return len(left)


def coll(pa1, pa2, data):
    if data[pa1][0] == data[pa2][0]: return 0
    time = []
    pos = set()
    for coord in range(3):
        p1 = data[pa1][0][coord]
        p2 = data[pa2][0][coord]
        
        v1 = data[pa1][1][coord]
        v2 = data[pa2][1][coord]
        
        a1 = data[pa1][2][coord]
        a2 = data[pa2][2][coord]
        if (p1 == p2) and (v1, a1) == (v2, a2) == (0, 0):
            time.append('HEJ')
        else:
            ti = set(solve(p1, p2, v1, v2, a1, a2))
            #db(p1, p2, v1, v2, a1, a2, 'coord', coord,  ti)
            time.append(ti)
            pos |= ti
    sols = []
    for p in pos:
        if all(t == 'HEJ' or p in t for t in time):
            sols.append(p)
    sols.sort()
    if len(sols) > 0:
        return sols[0]
    return None
    
        

def p2(v):
    #FAILED 433 too high. 432 is also too high. Failed 111 too low
    lines = v.strip().split('\n')
    cnt = 0
    data = [parse(line) for line in lines]
    N = len(data)
    colltimes = dd(list)
    #db(coll(352, 350, data))
    #return
    
    for p1 in range(N):
        for p2 in range(p1 + 1, N):
            if p1 != p2:
                t = coll(p1, p2, data)
                if t != None and t >= 0:
                    colltimes[t].append([p1, p2])
    times = list(colltimes.keys())
    times.sort()
    #db(times)
    #db(colltimes)
    collided = set()
    for t in times:
        colllist = colltimes[t]
        #print(t, colllist)
        died = set()
        for pairs in colllist:
            p1, p2  = pairs
            if p1 not in collided and p2 not in collided:
                died |= set(pairs)
        collided |= died
    #db(collided)
    db('RUnning sim')
    return N - len(collided) #sim(1000, N, data, colltimes)
    


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2017,20, p1, p2, cmds)
if stats: print_stats()
#manual()
