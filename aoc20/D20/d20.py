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
    line = line.replace(':', '')
    return lazy_ints(line.split())

def rotate(grid, R, C, k):
    assert R == C
    if k == 0:
        return grid

    newgrid = emptygrid(R, C, '')
    for r in range(R):
        for c in range(C):
            nc = C - r -1
            nr = c
            newgrid[nr][nc] = grid[r][c]
    return rotate(newgrid, R, C, k-1)

def rotate2(grid):

    R, C = len(grid), len(grid[0])
    newgrid = []
    for c in range(C):
        col = []
        for r in range(R):
            
            col.append(grid[r][c])
        newgrid.append(col)
    return newgrid

def flip(grid, R,  C):
    newgrid = []
    for r in range(R):
        newgrid.append(grid[r][::-1])
    return newgrid

def getsides(grid, R,  C):
    up = [grid[0][c] for c in range(C)]
    right = [grid[r][C-1] for r in range(R)]
    down = [grid[R-1][c] for c in range(C-1, -1, -1)]
    left = [grid[r][0] for r in range(R-1, -1, -1)]
    return [up, right, down, left]

def samesides(sides1, sides2):
    for side in sides1:
        for side2 in sides2:
            if side == side2 or side == side2[::-1]:
                return 1
    return 0

def same(side, matchside, altgrid):
    altsides = getsides(altgrid, len(altgrid), len(altgrid[0]))
    s = altsides[matchside]
    if side == s[::-1]:
        return True, altsides

    return False, []


def allgrids(grid, R, C):

    all = [grid]
    for i in range(1, 4):
        rot = rotate(grid, R, C, i)
        all.append(rot)
    flipped = flip(grid, R, C)
    all.append(flipped)
    for i in range(1, 4):
        rot = rotate(flipped, R, C, i)
        all.append(rot)
    return all


def allgrids2(grid, R, C):

    all = [grid]
    rot = grid
    for i in range(1, 4):
        rot = rotate2(rot)
        all.append(rot)
    flipped = flip(grid, R, C)
    all.append(flipped)
    rot = flipped
    for i in range(1, 4):
        rot = rotate2(rot)
        all.append(rot)
    return all


def p1(v):
    imgs = chunks(v)
    grids = []
    corners = []
    for img in imgs:
        lines = img.split('\n')
        _, id = parse(lines[0])

        grid, R, C = togrid(lines[1:])
        
        #printgrid(grid)
        #db('')

        sides = getsides(grid, R, C)
        grids.append((id, grid, sides))
    N = len(grids)
    for i in range(N):

        myid, mygrid, mysides = grids[i]
        cnt = 0
        for j in range(N):
            if j != i: 

                oid, ogrid, osides = grids[j]
                cnt += samesides(mysides, osides)  
        if cnt == 2:
            corners.append(myid)
        else:
            db(myid)


    db(corners)
    return mul(corners)

def getnxt(prevside, matchside, gridmap, R, C, VIS):
    for id, (grid, sides) in gridmap.items():
        if id not in VIS:
            for alt in allgrids(grid, R, C):
                ok, altsides = same(prevside, matchside, alt)
                if ok:
                    return id, alt, altsides
    return -1

def checkmonster(r, c, big, pos):
    out = set()
    for dr in range(len(pos)):
        for dc in range(len(pos[0])):
            monstch = pos[dr][dc]
            ch = big[r + dr, c + dc]
            if monstch == '#' and ch != '#':
                return set()
            if monstch == '#' and ch == '#':
                out.add((r+dr, c + dc))
    for rr, cc in out:
        big[rr, cc] = 'O'           
    return out

def p2(v):
    imgs = chunks(v)
    grids = []
    gridmap = {}
    corners = []
    S = int(len(imgs) ** (0.5))
    db('Side', S)
    for img in imgs:
        lines = img.split('\n')
        _, id = parse(lines[0])

        grid, R, C = togrid(lines[1:])
        
        #printgrid(grid)
        #db('')

        sides = getsides(grid, R, C)
        grids.append((id, grid, sides))
        gridmap[id] = grid, sides
    N = len(grids)
    for i in range(N):

        myid, mygrid, mysides = grids[i]
        cnt = 0
        for j in range(N):
            if j != i: 

                oid, ogrid, osides = grids[j]
                cnt += samesides(mysides, osides)  
        if cnt == 2:
            corners.append(myid)
    
    corner1 = corners[0]
    db(corner1)
    SQ = {}
    all = allgrids(gridmap[corner1][0], R, C)
    SWITCH = 0
    
    SQ[0, 0] = corner1, gridmap[corner1][0], gridmap[corner1][1]
    VIS = set([corner1])
    prev = gridmap[corner1][1]
    #firstrow
    for bc in range(1, S):
        nxt, nxtgrid, nxtsides = getnxt(prev[1], 3, gridmap, R, C, VIS)
        if nxt > 0:
            #db('In row', nxt)
            VIS.add(nxt)
            SQ[0, bc] = nxt, nxtgrid, nxtsides
            prev = nxtsides
    
    prev = gridmap[corner1][1]
    for br in range(1, S):
        s1, s2 = 2, 0
        if SWITCH:
            s1, s2 = 0, 2
        nxt, nxtgrid, nxtsides = getnxt(prev[s1], s2, gridmap, R, C, VIS)
        if nxt > 0:

            #db('In col', nxt)
            VIS.add(nxt)
            BR = br
            if SWITCH: BR = -br
            SQ[BR, 0] = nxt, nxtgrid, nxtsides
            prev = nxtsides
    
    #db(SQ)

    for br in range(1, S):
        BR = br
        if SWITCH: BR = -br
            
        _, _, prev = SQ[BR, 0]
        for bc in range(1, S):
            nxt, nxtgrid, nxtsides = getnxt(prev[1], 3, gridmap, R, C, VIS)
            if nxt > 0:
                BR = br
                VIS.add(nxt)
                if SWITCH: BR = -br 
                SQ[BR, bc] = nxt, nxtgrid, nxtsides
                prev = nxtsides
    def CHR():
        return ' '
    big = dd(CHR)
    mnR, mxR = 0, 0
    mnC, mxC = 0, 0
    for r, c in SQ.keys():
        db(r, c, SQ[r, c][0])
    for br in range(S):
        for bc in range(S):
            BR = br
            if SWITCH: BR = -br
            
            id, nextgrid, nxtsides = SQ[BR, bc]
            
            roffs = R -2
            coffs = C -2
            for r in range(1, R-1):
                for c in range(1, C-1):
                    rr = roffs * BR + r -1
                    cc = c + coffs * bc -1
                    big[rr, cc] = nextgrid[r][c]
                    mnR = min(mnR, rr)
                    mxR = max(mxR, rr)
                    mnC = min(mnC, cc)
                    mxC = max(mxC, cc)
    db(mnR, mxR, mnC, mxC)
    tots = []
    for r in range(mnR, mxR + 1):
        out = []
        for c in range(mnC, mxC + 1):
            out.append(big[r, c])
        tots.extend(out)
        db(''.join(out))

    #####################
    # FIND MONSTER
    mv = open("monster.txt", 'r').read().strip('\n').split('\n')
    monster, MR, MC = togrid(mv)
    allpos = allgrids2(monster, MR, MC)
    inmonst = set()
    for pos in allpos:
        printgrid(pos)
        
    for r in range(mnR, mxR + 1):
        for c in range(mnC, mxC + 1):
            for pos in allpos:
                monst = checkmonster(r, c, big, pos)
                inmonst |= monst

    tot = ''.join(tots)
    # FAILDED 2661
    db('')
    for r in range(mnR, mxR + 1):
        out = []
        for c in range(mnC, mxC + 1):
            out.append(big[r, c])
        db(''.join(out))


    return tot.count('#') - len(inmonst)
    '''
    unmatched = []
    def sidelist(): return [()] *4
    g = dd(sidelist)

    for i, side in enumerate(csides):
        for j in range(N):

            oid, ogrid, osides = grids[j]
            if oid != corner1: 
                for k, oside in enumerate(osides):
                    if oside == side:
                        g[corner1][i] = (oid, k, 0)
                    if oside == side[::-1]:
                        g[corner1][i] = (oid, k, k)
    
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  
    big = dd(CHR)
    cgrid = gridmap[corner1][0]
    for r in range(R):
        for c in range(C):
            big[r, c] = cgrid[r][c]
    
    mnR, mxR = 0, 0
    mnC, mxC = 0, 0
    db(corner1)


    for i in range(4):
        r = g[corner1][i]
        if len(r)> 0:
            gr, _ = gridmap[r[0]]
            nextgrid = rotate(gr,R, C, r[-1])
            db(r[0], dirs[i], i)
            dr, dc = dirs[i]
            roffs = (R + 1) * dr
            coffs = (C + 1) * dc
            for r in range(R):
                for c in range(C):
                    rr = roffs + r
                    cc = c + coffs
                    big[rr, cc] = nextgrid[r][c]
                    mnR = min(mnR, rr)
                    mxR = max(mnR, rr)
                    mnC = min(mnC, cc)
                    mxC = max(mxC, cc)
                    
    for r in range(mnR, mxR + 1):
        out = []
        for c in range(mnC, mxC + 1):
            out.append(big[r, c])
        db(''.join(out))

    '''
    

                    


    return -1



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,20, p1, p2, cmds)
if stats: print_stats()
#manual()
