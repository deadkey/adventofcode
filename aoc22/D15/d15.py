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
    #return lazy_ints(line.split())
    line = line.replace('Sensor at', ' ').replace('closest beacon is at', ' ')
    return lazy_ints(multisplit(line, ' =,:xy')) 

def dist(x, ax, y, ay):
    return abs(x - ax) + abs(y - ay)

def add(grid, sensor, Y):
    sx, sy, bx, by = sensor
    d = dist(sx, bx, sy, by)
    for xx in range(sx - d, sx + d + 1):
        if dist(xx, sx, Y, sy) <= d:
            grid[xx, Y] = 1


def fill(grid, sensors, Y):
    for sensor in sensors:
        add(grid, sensor, Y)

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    sensors = []

    used = set()
    for i in range(len(data)):
        sx, sy, bx, by = data[i]
        sensors.append((sx, sy, bx, by))
        
        used.add((sx, sy))
        used.add((bx, by))
        
    #db(minx, maxx, miny, maxy)
    grid = dd(int)
    #sensors = [sensors[6]]
    #db(sensors)
    Y = 2000000
    fill(grid, sensors, Y)
    #printdictxy(grid)
    minx = min(grid.keys())[0]
    maxx = max(grid.keys())[0]
    
    for xx in range(minx, maxx + 1):
        if grid[xx, Y] == 1 and (xx, Y) not in used: 
            su += 1

    return su


def get(sensor, x):
    sx, sy, bx, by = sensor
    d = dist(sx, bx, sy, by)
    dy = d - abs(x - sx)
    return sy - dy, sy + dy

def intervals(sensors, start, end):
    ints = []
    for x in range(start, end + 1):
        li= []
        for sensor in sensors:
            ys, ye = get(sensor, x)
            li.append((ys, ye))
        ints.append(li)
    return ints

def hasempty(li, X):
    li.sort()
    cnt = 0
    curr = 0
    for s,e in li:
        if curr + 1 < s:
            return True, curr + 1
        curr = max(curr, e)
        if curr >= X: break
    return False, -1

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    sensors = []
 
    used = set()
    for i in range(len(data)):
        sx, sy, bx, by = data[i]
        sensors.append((sx, sy, bx, by))
        used.add((sx, sy))
        used.add((bx, by))
        
    X = 4000000
    overlaps = intervals(sensors, 0, X)
    
    for x, li in enumerate(overlaps):
        if x % 1000 == 0: db(x)
        ok, Y  = hasempty(li, X)
        if ok: 
            #db('Line ', x, Y)
            return x * 4000000 + Y

    return su



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,15, p1, p2, cmds)
if stats: print_stats()

#manual()
