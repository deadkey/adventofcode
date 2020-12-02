import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import run, run_samples
from util import multisplit, lazy_ints

import re

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(a):
    if DB: print(a)

def p1(v):
    lines = v.strip().split('\n')
    print('Len input: {} lines {} chars'.format(len(lines), len(v)))
    
    cnt = 0
    for line in lines:
        lo, hi, lt, pw = lazy_ints(multisplit(line, '-: '))

        ltcnt = 0
        for ch in pw:
            if ch == lt:
                ltcnt += 1
        if lo <= ltcnt <= hi:
            cnt += 1
    
    return cnt

def p2(v):
    lines = v.strip().split('\n')
    cnt = 0
    for line in lines:
        lo, hi, lt, pw = re.split('-| |: ', line)
        lo = int(lo)
        hi = int(hi)
        ltcnt = 0
        if int(pw[lo-1] == lt) + int(pw[hi-1] == lt) == 1:
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
    #'submit2' 
    }
    run_samples(p1, p2)
    run(get_year(), get_day(), p1, p2, cmds)
