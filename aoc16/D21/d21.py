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
    return lazy_ints(line.split())

def revswap(ins, pw):
    return swap(ins, pw)

def swap(ins, pw):
    if ins[1]== 'position':
        p1 = ins[2]
        p2 = ins[-1]
        pw[p1], pw[p2] = pw[p2], pw[p1]
        return pw
    else:
        lt1 = ins[2]
        lt2 = ins[-1]
        for i, ch in enumerate(list(pw)):
            if ch == lt1:
                pw[i] = lt2
            elif ch == lt2:
                pw[i] = lt1
            
        return pw

def rotateletter(pw, lt):
    ind = pw.index(lt)
    n = len(pw)
    add = (1 if ind >= 4 else 0)
    le = (1 + ind + add) % n
    return rotateright(pw, le)

def revrotate(ins, pw):
    le = ins[2]
    n = len(pw)
    db(ins, le)
    
    if ins[1] == 'right':
        return rotateleft(pw, le)
    if ins[1] == 'left':
        return rotateright(pw, le)
    
    lt = ins[-1]
    for le in range(0, n + 2):
        tmp=rotateleft(pw,le)
        testpw = rotateletter(tmp, lt)
        if testpw == pw:
            return tmp
    assert False

def rotateright(pw, le):
    n = len(pw)
    if le == 0:
        return pw
    return pw[-le:] + pw[0:n - le]
    
def rotateleft(pw, le):
    n = len(pw)
    if le == 0:
        return pw

    return pw[le:] + pw[0:le]
    


def rotate(ins, pw):
    le = ins[2]
    n = len(pw)
    db(ins, le)
    
    if ins[1] == 'right':
        return rotateright(pw, le)
    if ins[1] == 'left':
        return rotateleft(pw, le)
    
    lt = ins[-1]
    ind = pw.index(lt)
    add = (1 if ind >= 4 else 0)
    le = (1 + ind + add) % n
    db(le)
    return rotateright(pw, le)

def revreverse(ins, pw):
    return reverse(ins, pw)    


def reverse(ins, pw):
    a = ins[2]
    b = ins[-1]
    sub = pw[a:b+1][::-1]
    return pw[0:a] + sub + pw[b+1:]

def revmove(ins, pw):
    fr = ins[2]
    to = ins[-1]
    rm = pw.pop(to)
    pw.insert(fr, rm)
    return pw


def move(ins, pw):
    fr = ins[2]
    to = ins[-1]
    rm = pw.pop(fr)
    pw.insert(to, rm)
    return pw

def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    T = 'abcdefgh'
    pw = list(T)
    data = [parse(line) for line in lines]
    for ins in data:
        op = ins[0]
        if op == 'swap':
            pw = swap(ins, pw)
        
        if op == 'rotate':
            pw = rotate(ins, pw)

        if op == 'reverse':
            pw = reverse(ins, pw)

        if op == 'move':
            pw = move(ins, pw)
        db(''.join(pw))
    return ''.join(pw)



def p2(v):
    T = 'fbgdceah' #'agcebfdh' #'fbgdceah'
    lines = v.strip().split('\n')
    cnt = 0
    pw = list(T)
    data = [parse(line) for line in lines]
    for ins in data[::-1]:
        op = ins[0]
        if op == 'swap':
            pw = revswap(ins, pw)
        
        if op == 'rotate':
            pw = revrotate(ins, pw)

        if op == 'reverse':
            pw = revreverse(ins, pw)

        if op == 'move':
            pw = revmove(ins, pw)
        db(''.join(pw))
    return ''.join(pw)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,21, p1, p2, cmds)
if stats: print_stats()
#manual()
