import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
from gridutil import *
import math
from collections import defaultdict as dd, Counter
from itertools import chain, combinations, permutations
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
    return lazy_ints(multisplit(line, ', ')) 
    

def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    tiles = [parse(line) for line in lines]
    biggest = 0
    areas = []
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            dr = abs(tiles[i][0] - tiles[j][0]) + 1
            dc = abs(tiles[i][1] - tiles[j][1]) + 1
            
            area = dr * dc
            
            areas.append(area)

    return max(areas)

def parallel(sideA, sideB):
    ax = abs(sideA[0][0] - sideA[1][0])
    ay = abs(sideA[0][1] - sideA[1][1])

    bx = abs(sideB[0][0] - sideB[1][0])
    by = abs(sideB[0][1] - sideB[1][1])
    return ax == bx == 0 or ay == by == 0

def getintersection(sideA, sideB):
    ax = abs(sideA[0][0] - sideA[1][0])
    ay = abs(sideA[0][1] - sideA[1][1])

    bx = abs(sideB[0][0] - sideB[1][0])
    by = abs(sideB[0][1] - sideB[1][1])

    X, Y = 0, 0

    if ax == 0:    
        X = sideA[0][0]
    else:
        X = sideB[0][0]
    if ay == 0:
        Y = sideA[0][1]
    else:
        Y = sideB[0][1]
    return X, Y 

def intersects(sq_side, side):
    if parallel(sq_side, side): return False, (0, 0)
    sq_a, sq_b = sq_side
    sq_a, sq_b = min(sq_a, sq_b ),max(sq_a, sq_b) #sorted by x
    p1, p2 = side
    p1, p2 = min(p1, p2), max(p1, p2)

    overlapsX = sq_a[0] <= p1[0] <= sq_b[0] or sq_a[0] <= p2[0] <= sq_b[0] or p1[0] <= sq_a[0] <= p2[0] or p1[0] <= sq_b[0] <= p2[0]
    sq_a, sq_b = min(sq_a, sq_b, key=lambda x: x[1]) ,max(sq_a, sq_b, key=lambda x: x[1]) #sorted by x
    
    p1, p2 = min(p1, p2, key=lambda x: x[1]), max(p1, p2, key=lambda x: x[1])
    overlapsY = sq_a[1] <= p1[1] <= sq_b[1] or sq_a[1] <= p2[1] <= sq_b[1] or p1[1] <= sq_a[1] <= p2[1] or p1[1] <= sq_b[1] <= p2[1]
    #Find point of overlap too.
    if overlapsX and overlapsY:
        point = getintersection(sq_side, side)
        return True, point
    return False, (0, 0)

# Area of polygon
def polygonArea(P):
  n = len(P)
  X = [x for x, _ in P]
  Y  = [y for _, y in P]
  area = 0.0
  
  # Calculate value of shoelace formula
  j = n - 1
  for i in range(0,n):
    area += (X[j] + X[i]) * (Y[j] - Y[i])
    j = i   # j is previous vertex to i
    
  return abs(area / 2.0)

def sign(val):
    if val > 0: return 1
    if val < 0: return -1
    return 0

def getoutside(side, point, allowed):
    OUTSIDE = {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}
    a, b = side
    dx = sign(b[0] - a[0])
    dy = sign(b[1] - a[1])
    dxo, dyo = OUTSIDE[(dx, dy)]
    outside_point = point[0] + dxo, point[1] + dyo
    if outside_point not in allowed:
        return outside_point
    return None

def getadj(p, side):
    x, y = p
    a, b = side
    dx = sign(b[0] - a[0])
    dy = sign(b[1] - a[1])
    
    if dx == 0:
        cand = []
        #vertical line
        miny = min(a[1], b[1])
        maxy = max(a[1], b[1])
        for px, py in [(x, y-1), (x, y), (x, y + 1)]:
            if miny <= py <= maxy:
                cand.append((px, py))
        return cand
    else:

        cand = []
        #horizontal line
        minx = min(a[0], b[0])
        maxx = max(a[0], b[0])
        for px, py in [(x-1, y), (x, y), (x+1, y)]:
            if minx <= px <= maxx:
                cand.append((px, py))
        return cand
        
    

#True if outside
def intersects_and_outside(sq_side, side, allowed):
    overlaps, point = intersects(sq_side, side)
    
    outside = getoutside(side, point, allowed)
    '''
    if overlaps:
        db('Sq side', sq_side, 'side', side)
        db('overlaps', overlaps, 'in point', point)
        db('outside point', outside)
    '''
    if overlaps and outside != None:
        adjacent = getadj(point, sq_side)
        #db('adjacent', adjacent)
        for p in adjacent:
            if p == outside: 
                #db('Outside')
                return True
        #db('inside')
    return False


def inside(a, b, sides, allowed):
    left = min(a[0], b[0])
    right = max(a[0], b[0])
    bottom = min(a[1], b[1])
    top = max(a[1], b[1])
    corners = [(left, bottom), (right, bottom), (right, top), (left, top)]
    sq_sides = list(zip(corners, corners[1:] + [corners[0]]))

    for sq_side in sq_sides:
        for side in sides:
            if intersects_and_outside(sq_side, side, allowed):
                #db('RETURNS FALSE')
                return False
    #db('RETURNS TRUE')
    return True

def getallowed(sides):
    allowed = set()
    for start, end in sides:
        start = tuple(start)
        end = tuple(end)
        allowed.add(tuple(start))
        dx = sign(end[0] - start[0])
        dy = sign(end[1] - start[1])
        curr = start
        while curr != end:
            
            curr = curr[0] + dx, curr[1] + dy
            allowed.add(curr)
        allowed.add(tuple(end))
    return allowed

def p2(v):
    
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    tiles = [parse(line) for line in lines]
    biggest = 0
    parea = polygonArea(tiles)
    if parea < 0:
        tiles = tiles[::-1]
    areas = []
    
    sides = list(zip(tiles, tiles[1:] + [tiles[0]]))
    allowed = getallowed(sides)
    #db('Generated allowed')
    #db(allowed)
    #inside([9,5], [2, 3], sides, allowed)

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            a = tiles[i]
            b = tiles[j]
            #db('Tiles', a, b)
            if inside(a, b, sides, allowed):
                
                dr = abs(tiles[i][0] - tiles[j][0]) + 1
                dc = abs(tiles[i][1] - tiles[j][1]) + 1
                area = dr * dc
                #db('inside', area)
                areas.append(area)

    return max(areas)



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2025,9, p1, p2, cmds)
if stats: print_stats()

#manual()
