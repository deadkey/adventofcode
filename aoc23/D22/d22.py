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
    line = removeall(line, '~,')
    return lazy_ints(multisplit(line, ' ')) 

def allp2(c, g, p):  
    for ch in g[c]:
        if p[ch] == 1:
            return False
    return True 

def order(x1, x2):
    return  min(x1, x2), max(x1, x2)

def inside(x, y, a1, b1, a2, b2):
    return a1 <= x <= a2 and b1 <= y <= b2

def inside3d(x, y, z, a1, b1, c1, a2, b2, c2):
    return a1 <= x <= a2 and b1 <= y <= b2 and c1 <= z <= c2


def under(low, cube):
    x1, y1, z1, x2, y2, z2 = low
    a1, b1, c1, a2, b2, c2 = cube

    x1, x2 = order(x1, x2)
    y1, y2 =order(y1, y2)

    coord1 = set()
    for x in range(x1, x2+1):
        for y in range(y1, y2 + 1):
            coord1.add((x, y))



    a1, a2 = order(a1, a2)
    b1, b2 =order(b1, b2)

    coord2 = set()
    for x in range(a1, a2+1):
        for y in range(b1, b2 + 1):
            coord2.add((x, y))
    return len(coord1 & coord2)

def placeon(low, cube):
    x1, y1, z1, x2, y2, z2 = low
    a1, b1, c1, a2, b2, c2 = cube
    newz = z2 + 1
    diff = c1 - newz
    assert diff >= 0
    c2 -= diff
    return a1, b1, newz, a2, b2, c2 

def findmax(alt):
    z = -INF
    best = []
    for cube in alt:
        if cube[-1] > z:
            z = cube[-1]
            best = cube
    return best

def overlapall(low, cube):
    x1, y1, z1, x2, y2, z2 = low
    a1, b1, c1, a2, b2, c2 = cube

    for x, y, z in [[x1, y1, z1], [x1, y1, z2], [x1, y2, z1], [x1, y2, z2], [x2, y1, z1], [x2, y1, z2], [x2, y2, z1], [x2, y2, z2]]:
        if inside3d(x, y, z, a1, b1,c1,  a2, b2, c2):
            return True
    
    for x, y, z in [[a1, b1, c1], [a1, b1, c2], [a1, b2, c1], [a1, b2, c2], [a2, b1, c1], [a2, b1, c2], [a2, b2, c1], [a2, b2, c2]]:
        if inside3d(x, y, z, x1, y1,z1,  x2, y2, z2):
            return True
    


    return False

def getcoord(cube):
    x1, y1, z1, x2, y2, z2 = cube
    x1, x2 = order(x1, x2)
    y1, y2 =order(y1, y2)
    z1, z2 =order(z1, z2)
    coord = set()

    for x in range(x1, x2 + 1):
        for y in range(y1, y2+1):
            for z in range(z1, z2 + 1):
                coord.add((x, y, z))
    return coord


def touching(low, cube):
    x1, y1, z1, x2, y2, z2 = low
    a1, b1, c1, a2, b2, c2 = cube
    return c1 == z2 + 1

def touch3d(top, under):
    a1, b1, c1, a2, b2, c2 = top
    c1 -= 1
    c2 -= 1

    coord1 = getcoord(under)
    coord2 = getcoord([a1, b1, c1, a2, b2, c2 ])
    return  len(coord1 & coord2) > 0





def fall(byz):
    '''
    mans = set()
    with open('bricks.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = removeall(line, '()')
            d = parse(line)
            mans.add(tuple(d))
    '''

    g = dd(list)
    p = dd(int)
    N = len(byz)
    newpos = []
    for i in range(N):
        alt = []
        other = []
        
        for cube in newpos:
            if under(cube, byz[i]):
                pos = placeon(cube, byz[i])
                alt.append(pos)
                other.append(cube)
        if len(alt) > 0:
            pos = findmax(alt)
        else:
            newz = 1
            a1, b1, c1, a2, b2, c2 = byz[i]
            diff = c1 - newz
            c2 -= diff
            pos = a1, b1, newz, a2, b2, c2

    
        newpos.append(pos)
       
    ###########################
    #find supporting!
    
    for i in range(N):
        for k in range(i + 1, N):
            if overlapall(newpos[i], newpos[k]):
                db('OVERLPAS', i, k, newpos[i], newpos[k])
                exit()
    

    for i in range(N):
        istouching = False
        a1, b1, c1, a2, b2, c2 = newpos[i]
        if c1 == 1: continue

        for k in range(i):
            if touch3d(newpos[i], newpos[k]):
                istouching = True
        if not istouching:
            db('NOT TOUCHING', i, newpos[i])

   
    
    
    gp = dd(list)
    for i in range(N):
        for k in range(i + 1, N):
            if touch3d(newpos[k], newpos[i]):
                g[i].append(k)
                p[k] += 1
                gp[k].append(i)
    return g, p, gp
#### WRONG 595
### 591
## 550 too hi this is close
## 504 no info ????
### Måns får 492!!!!

def remove(n, g, gp):
    gone = set([n])
    q = g[n]
    while len(q) > 0:

        q2 = []
        for node in q:
            if node in gone: continue
            
            parents = set(gp[node])
            if len(parents & gone) == len(parents):
                q2.extend(g[node])
                gone.add(node)
        q = q2
    return len(gone) -1

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    cubes = []
    for i in range(len(data)):
        d = data[i]
        start = d[0:3]
        end = d[3:]
        if start[-1] > end[-1]:
            start, end = end, start
        cubes.append([start[0], start[1], start[2], end[0], end[1], end[2]])

    byz = sorted(cubes, key = lambda x: x[2])
   
    g, p, pg = fall(byz)
    db('CHECKING IT NOW')
    for c in range(len(byz)):
        db(c, remove(c, g, pg))
        su += remove(c, g, pg)

    return su

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,22, p1, p2, cmds)
if stats: print_stats()

#manual()
