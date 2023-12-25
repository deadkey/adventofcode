import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from z3 import *
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
    line = removeall(line, '@')
    return lazy_ints(multisplit(line, ' ,')) 

# intersects two lines.
# if parallell, returnes False.
def inters(l1, l2):
  a1,b1,c1 = l1
  a2,b2,c2 = l2
  cp = a1*b2 - a2*b1 
  if cp != 0:
    return float(b1*c2 - b2*c1)/cp, float(a2*c1 - a1*c2)/cp
  else:
    return False

# Converts two points to a line (a, b, c), 
# ax + by + c = 0
# if p == q, a = b = c = 0 
def pts2line(p, q):
  return (-q[1] + p[1], 
          q[0] - p[0], 
          p[0]*q[1] - p[1]*q[0]) 

def infuture(x, y, pp):
   p, vx, vy = pp
   dx = x - p[0]
   dy = y - p[1]
   return vx * dx > 0 and dy * vy > 0

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    a = 200000000000000
    b = 400000000000000
    #a = 7
    #b = 27
    rocks = []
    future = []
    for i in range(len(data)):
        d = data[i]
        p1 = d[0], d[1]
        p2 = d[0] + d[3], d[1] + d[4]
        eq = pts2line(p1, p2)
        rocks.append(eq)
        future.append((p1, d[3], d[4]))

    N = len(rocks)
    
    for i in range(N):
       for k in range(i+1, N):
          vals = inters(rocks[i], rocks[k])
          if vals != False:
            x, y = vals
            
            if a <= x <= b and a <= y <= b:
               if infuture(x, y, future[i]) and infuture(x, y, future[k]):
                su += 1

    return su


def solve(items):
    s = Solver()
    x0 = Int('x0')
    vx0 = Int('vx0')
    y0 = Int('y0')
    vy0 = Int('vy0')
    z0 = Int('z0')
    vz0 = Int('vz0')
    for i, (x, y, z, vx, vy, vz) in enumerate(items):
        ti = Int(f't_{i}')
        s.add(x0 + vx0*ti == x + vx*ti)
        s.add(y0 + vy0*ti == y + vy*ti)
        s.add(z0 + vz0*ti == z + vz*ti)
    print(s.check())
    model = s.model()
    print('x0:', model.evaluate(x0))
    print('y0:', model.evaluate(y0))
    print('z0:', model.evaluate(z0))
    return model.evaluate(x0).as_long() + model.evaluate(y0).as_long() + model.evaluate(z0).as_long()

def p2(v):
    lines =  v.strip().split('\n')
    chunks = v.split('\n\n')
    ans = 0
    items = []
    for line in lines:
        item = parse(line)
        items.append(item)
    '''
    N = len(items)
    for i in range(N):
        for j in range(i+1, N):
            ok, x, y = collide(items[i], items[j])
            if testBox(x) and testBox(y):
                ans += 1
    '''
    ans = solve(items)


    return ans


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,24, p1, p2, cmds)
if stats: print_stats()

#manual()
