import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from util import run

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(a):
    if DB: print(a)

def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    for line in lines:
        li = list(map(int, line.split()))
        li.sort()
        a, b, c = li
        if a + b > c:
            cnt += 1

    return cnt

def p2(v):
    lines = v.strip().split('\n')
    grid = []
    for line in lines:
        li = list(map(int, line.split()))
        grid.append(li)

    k = len(lines)//3
    cnt = 0
    for c in range(3):
        for start in range(k):
            i = 3 * start
            A = grid[i][c]
            B = grid[i+1][c]
            C = grid[i+2][c]
            A, B, C = sorted([A, B, C])
            if A + B > C:
                cnt += 1

    return cnt


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
    run(2016, 3, p1, p2, cmds)
