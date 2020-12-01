import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
from fetch import answer

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(a):
    if DB == "debug": print(a)

def p1(v):
    lines = v.strip().split('\n')
    posx, posy = 0, 0
    dirIndx = 0
    print(lines)
    DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    moves = []
    for line in lines:
        moves.extend(line.split(', '))
    for move in moves:
        if move[0] == 'L':
            dirIndx -= 1
        else:
            dirIndx += 1
        
        dirIndx %= 4
        dx, dy = DIRS[dirIndx]    
        steps = int(move[1:])
        DX = dx * steps
        DY = dy * steps
        posx += DX
        posy += DY

    return abs(posx) + abs(posy)


def p2(v):
    lines = v.strip().split('\n')
    posx, posy = 0, 0
    vis = set()
    vis.add((posx, posy))
    dirIndx = 0
    DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    moves = []
    for line in lines:
        moves.extend(line.split(', '))
    print('Len moves', len(moves))
    for move in moves:
        if move[0] == 'L':
            dirIndx -= 1
        else:
            dirIndx += 1
        
        dirIndx %= 4
        dx, dy = DIRS[dirIndx]    
        steps = int(move[1:])
        for step in range(steps):
            DX = dx
            DY = dy
            posx += DX
            posy += DY
            if (posx, posy) in vis:
                return abs(posx) + abs(posy)
            vis.add((posx, posy))
    

    return abs(posx) + abs(posy)


def fuel(n):
    s = 0
    f = (n//3) -2
    while f > 0:
        s+= f
        f = (f//3) -2
    return s


S = "run samples"
SO = "samples only"
IO = "input only"
FF = "force fetch"
DB = "debug"
tosubmit = 1

if __name__ == '__main__':
    filename = sys.argv[1]
    d = open(filename).read()
    
    y = 2016
    day = 1
    cmds = {S, 
    #'submit1',
    'submit2' 
    }
    run(y, day, p1, p2, cmds)
