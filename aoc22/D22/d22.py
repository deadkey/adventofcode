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
    return lazy_ints(multisplit(line, ' ')) 

LEFT = 2
RIGHT = 0
UP = 3
DOWN = 1

def findtoprow(grid, c):
    for row in range(len(grid)-1, -1, -1):
        #db('Find top', row, len(grid), grid[row], c, len(grid[row]), len(grid[0]))
        if grid[row][c] != ' ':
            return row
    assert False
    return -1

def findbottomrow(grid, c):
    for row in range(len(grid)):
        if grid[row][c] != ' ':
            return row
    assert False
    return -1


def findleftcol(grid, r):
    for col in range(len(grid[0])):
        #db('Find top', row, len(grid), grid[row], c, len(grid[row]), len(grid[0]))
        if grid[r][col] != ' ':
            return col
    assert False
    return -1

def findrightcol(grid, r):
    for col in range(len(grid[0]) -1, -1, -1):
        if grid[r][col] != ' ':
            return col
    assert False
    return -1



def wrap(grid, r, c, dr, dc):
    #db('wrapping', r, c, dr, dc)
    if dr != 0:
        if dr < 0:
            #db('find top')
            nr = findtoprow(grid, c)
            if grid[nr][c] != '#':
                return nr, c
            else:
                return r, c
        #db('find btm')
        nr = findbottomrow(grid, c)
        if grid[nr][c] != '#':
            return nr, c
        else:
            return r, c
    if dc < 0:
        nc = findrightcol(grid, r)
        if grid[r][nc] != '#':
            return r, nc
        return r, c
    nc = findleftcol(grid, r)
    if grid[r][nc] != '#':
        return r, nc
    return r, c

    
def step(grid, r, c, dr, dc):
    nr, nc = r + dr, c + dc
    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]): return wrap(grid, r, c, dr, dc) 
    if grid[nr][nc] == '#': return r, c
    if grid[nr][nc] == ' ': return wrap(grid, r, c, dr, dc)
    return nr, nc

def move(path, grid):
    deb = copygrid(grid)
    r = 0
    c = grid[0].index('.')
    dir = 0
    rot = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    draw = ['>', 'v', '<', '^']
    deb[r][c] = draw[dir]
    for m in path:
        if m == 'R':
            dir += 1
            dir %= 4
            deb[r][c] = draw[dir]
        elif m == 'L':
            dir -= 1
            dir %= 4
            deb[r][c] = draw[dir]
        else:
            dr, dc = rot[dir]
            for s in range(m):
                r, c = step(grid, r, c, dr, dc)
                #db('afterstep', r, c)
                deb[r][c] = draw[dir]
                
    #db('_____________________')  
    #printgrid(deb)

    return r, c, dir


def p1(v):
    # Guess 35368
    # Guess 2: 20324
    lines = v.split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]

    su = 0
    map = chunks[0]

    path = chunks[1][0]
    path = path.replace('R', ' R ').replace('L', ' L ')
    path = parse(path)
    grid = []
    for line in map:
        if len(line) < len(map[0]):
            line = line + " " * (len(map[0]) - len(line))
        grid.append(line)
    #printgrid(grid)
    pos = move(path, grid)


    return (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + pos[2]


def flipped(old, new):
    if old == LEFT and new == RIGHT: return True
    if old == LEFT and new == UP: return True
    if old == RIGHT and new == LEFT: return True
    if old == RIGHT and new == DOWN: return True
    if old == UP and new == LEFT: return True
    if old == UP and new == DOWN: return True
    if old == DOWN and new == RIGHT: return True
    if old == DOWN and new == UP: return True
    

    return False

def wrap2(faces, face, MAP, SIZE, r, c, dir):
    f = face + 1
    

    nface, ndir = MAP[f, dir]
    nface -= 1
    MX = SIZE -1

    offset = 0

    if dir == UP or dir == DOWN:
        offset = c
    if dir == LEFT or dir == RIGHT:
        offset = r
    
    if flipped(dir, ndir):
        offset = SIZE -1 - offset


    if ndir == LEFT:
        nr, nc = offset, MX

    if ndir == RIGHT:
        nr, nc = offset, 0
    
    if ndir == DOWN:
        nr, nc = 0, offset

    if ndir == UP:
        nr, nc = MX, offset
    
    '''
    
    if dir == LEFT and ndir == LEFT:
        nr, nc, ndir, nface =  r, SIZE - 1, ndir, nface

    if dir == LEFT and ndir == RIGHT:
        nr, nc, ndir, nface = SIZE - 1 - r, 0, ndir, nface
    
    if dir == LEFT and ndir == DOWN:
        nr, nc, ndir, nface = 0, r, ndir, nface

    if dir == LEFT and ndir == UP:
        nr, nc, ndir, nface = SIZE -1, SIZE - 1 - r, ndir, nface


    if dir == RIGHT and ndir == RIGHT:
        nr, nc, ndir, nface = r, 0, ndir, nface

    if dir == RIGHT and ndir == LEFT:
        nr, nc, ndir, nface = SIZE - 1 - r, SIZE -1, ndir, nface
    

    if dir == RIGHT and ndir == DOWN:
        nr, nc, ndir, nface = 0, SIZE - 1 - r, ndir, nface

    if dir == RIGHT and ndir == UP:
        nr, nc, ndir, nface = SIZE -1, r, ndir, nface


    if dir == UP and ndir == UP:
        nr, nc, ndir, nface = SIZE -1, c, ndir, nface

    if dir == UP and ndir == DOWN:
        nr, nc, ndir, nface = 0, SIZE - 1 - c, ndir, nface


    if dir == UP and ndir == LEFT:
        nr, nc, ndir, nface = SIZE - 1 - c, SIZE -1, ndir, nface

    if dir == UP and ndir == RIGHT:
        nr, nc, ndir, nface = c, 0, ndir, nface

    if dir == DOWN and ndir == LEFT:
        nr, nc, ndir, nface = c, SIZE -1, ndir, nface

    if dir == DOWN and ndir == RIGHT:
        nr, nc, ndir, nface = SIZE - 1 - c, 0, ndir, nface
    
    if dir == DOWN and ndir == DOWN:
        nr, nc, ndir, nface = 0, c, ndir, nface

    if dir == DOWN and ndir == UP:
        nr, nc, ndir, nface = SIZE -1, SIZE - 1 - c, ndir, nface
    '''


    grid = faces[nface]
    if grid[nr][nc] == '.':
        return nr, nc, ndir, nface
    return r, c, dir, face





    
def step(grid, r, c, dr, dc):
    nr, nc = r + dr, c + dc
    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]): return wrap(grid, r, c, dr, dc) 
    if grid[nr][nc] == '#': return r, c
    if grid[nr][nc] == ' ': return wrap(grid, r, c, dr, dc)
    return nr, nc

def step2(faces, face, MAP, SIZE, r, c, dir):
    dr, dc = rot[dir]
    nr, nc = r + dr, c + dc
    grid = faces[face]
    if nr < 0 or nc < 0 or nr >= SIZE or nc >= SIZE: return wrap2(faces, face, MAP, SIZE, r, c, dir) 
    if grid[nr][nc] == '#': return r, c, dir, face
    return nr, nc, dir, face

def move(path, grid):
    deb = copygrid(grid)
    r = 0
    c = grid[0].index('.')
    dir = 0
    rot = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    draw = ['>', 'v', '<', '^']
    deb[r][c] = draw[dir]
    for m in path:
        if m == 'R':
            dir += 1
            dir %= 4
            deb[r][c] = draw[dir]
        elif m == 'L':
            dir -= 1
            dir %= 4
            deb[r][c] = draw[dir]
        else:
            dr, dc = rot[dir]
            for s in range(m):
                r, c = step(grid, r, c, dr, dc)
                #db('afterstep', r, c)
                deb[r][c] = draw[dir]
                
    db('_____________________')  
    printgrid(deb)

    return r, c, dir


rot = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def move2(path, faces, MAP, SIZE):
    r = 0
    c = 0 #faces[0][0].index('.')
    face = 0
    dir = 0
    #draw = ['>', 'v', '<', '^']
    #deb[r][c] = draw[dir]
    for m in path:
        if m == 'R':
            dir += 1
            dir %= 4
            
        elif m == 'L':
            dir -= 1
            dir %= 4
        else:
            for s in range(m):
                r, c, dir, face = step2(faces, face, MAP, SIZE, r, c, dir)
                #db('afterstep', r, c)
                r
                
                
    return r, c, dir, face

def p2(v):
    # 70378
    # 1048 too low
    # 168111 to high
    samples = False
    MAP = {(1, RIGHT):(2, RIGHT), (1, UP): (6, RIGHT), (1, LEFT):(5, RIGHT), (1, DOWN): (3, DOWN), 
        (2, RIGHT):(4, LEFT), (2, UP): (6, UP), (2, LEFT):(1, LEFT), (2, DOWN): (3, LEFT), 
        (3, RIGHT):(2, UP), (3, UP): (1, UP), (3, LEFT):(5, DOWN), (3, DOWN): (4, DOWN), 
        (4, RIGHT):(2, LEFT), (4, UP): (3, UP), (4, LEFT):(5, LEFT), (4, DOWN): (6, LEFT), 
        (5, RIGHT):(4, RIGHT), (5, UP): (3, RIGHT), (5, LEFT):(1, RIGHT), (5, DOWN): (6, DOWN), 
        (6, RIGHT):(4, UP), (6, UP): (5, UP), (6, LEFT):(1, DOWN), (6, DOWN): (2, DOWN), 
        }
    SIZE = 50


    START = [(0, 1), (0, 2), (1, 1), (2, 1), (2, 0), (3, 0)]

    if samples:
        db('Running samples!!!!!!')
        SIZE = 4

        START = [(0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]
        MAP = {(1, RIGHT):(6, LEFT), (1, UP): (2, DOWN), (1, LEFT):(3, DOWN), (1, DOWN): (4, DOWN), 
        (2, RIGHT):(3, RIGHT), (2, UP): (1, DOWN), (2, LEFT):(6, UP), (2, DOWN): (5, UP), 
        (3, RIGHT):(4, RIGHT), (3, UP): (1, RIGHT), (3, LEFT):(2, LEFT), (3, DOWN): (5, RIGHT), 
        (4, RIGHT):(6, DOWN), (4, UP): (1, UP), (4, LEFT):(3, LEFT), (4, DOWN): (5, DOWN), 
        (5, RIGHT):(6, RIGHT), (5, UP): (4, UP), (5, LEFT):(3, UP), (5, DOWN): (2, UP), 
        (6, RIGHT):(1, LEFT), (6, UP): (4, LEFT), (6, LEFT):(5, LEFT), (6, DOWN): (2, RIGHT), 
        }
    s = set(MAP.values())
    assert(len(s) == len(MAP))

    lines = v.split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]

    su = 0
    map = chunks[0]

    path = chunks[1][0]
    path = path.replace('R', ' R ').replace('L', ' L ')
    path = parse(path)
    grid = []
    faces = []
    for line in map:
        if len(line) < len(map[0]):
            line = line + " " * (len(map[0]) - len(line))
        grid.append(line)
    for i, (R, C) in enumerate(START):
        startrow = R * SIZE
        startcol = C * SIZE
        face = []
        for row in range(startrow, startrow + SIZE):
            face.append([])
            for col in range(startcol, startcol + SIZE):
                
                face[-1].append(grid[row][col])
        faces.append(face)

    #printgrid(grid)
    pos = move2(path, faces, MAP, SIZE)
    db('Pos', pos)
    R, C = START[pos[-1]]
    startrow = R * SIZE
    startcol = C * SIZE
    r = startrow + pos[0] 
    c = startcol + pos[1]
    db('Recalc', r, c, pos[2])

    return (r + 1) * 1000 + (c + 1) * 4 + pos[2]


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,22, p1, p2, cmds)
if stats: print_stats()

#manual()
