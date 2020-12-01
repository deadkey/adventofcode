import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from util import run

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(a):
    if DB: print(a)

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
grid2 = {(0, 2): '1',
(1, 1): '2',
(1, 2): '3',
(1, 3): '4',
(2, 0): '5',
(2, 1): '6',
(2, 2): '7',
(2, 3): '8',
(2, 4): '9',
(3, 1): 'A',
(3, 2): 'B',
(3, 3): 'C',
(4, 2): 'D'
}
def p1(v):
    lines = v.strip().split('\n')
    posr = 1
    posc = 1
    code = []
    dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    for line in lines:
        for ch in line:
            dr, dc = dirs[ch]
            if 0 <= posr + dr < 3: posr += dr
            if 0 <= posc + dc < 3: posc += dc
        code.append(str(grid[posr][posc]))
    return ''.join(code)

def p2(v):
    lines = v.strip().split('\n')
    posr = 2
    posc = 0
    code = []
    dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    for line in lines:
        for ch in line:
            dr, dc = dirs[ch]
            if (posr + dr, posc + dc) in grid2:
                posr, posc = posr+dr, posc + dc
        code.append(str(grid2[posr, posc]))
    return ''.join(code)
    


S = "run samples"
SO = "samples only"
IO = "input only"
FF = "force fetch"
DB = 1
PR = "print input"


if __name__ == '__main__':
    cmds = {S, 
    #'submit1',
    'submit2' 
    }
    run(2016, 2, p1, p2, cmds)
