import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def check1(pw):
    for i in range(len(pw) -2):
        a, b, c = pw[i], pw[i+1], pw[i+2]
        if a == b -1  == c -2:
            return True
    return False


def check2(pw):
    
    cont = (ord('i') - ord('a')) in pw or (ord('o') - ord('a')) in pw or (ord('l') - ord('a')) in pw
    return not cont

def pair(pw, ch):
    for i in range(len(pw) -1):
        if ch == pw[i] == pw[i+1]:
            return True
    return False

def check3(pw):
    cnt = 0
    for ch in range(0, ord('z') - ord('a')+ 1):
        if pair(pw, ch):
            cnt += 1
    return cnt >= 2

def check(pw):
    #db(check1(pw))

    #db(check2(pw))
    #db(check3(pw))
    return check1(pw) and check2(pw) and check3(pw)    

def asc(ch):
    return ord(ch) - ord('a')

def toch(pw):
    offs = ord('a')
    out = [chr(d + offs) for d in pw]
    return ''.join(out)

def inc(pw):
    rev = pw[::-1]
    MOD = 26
    carry = 1
    for i in range(len(rev)):
        rev[i] += carry
        carry = rev[i]//MOD
        rev[i] %= MOD
    return rev[::-1]

def p1(v):
    lines = v.strip()
    testing = {'hijklmmn', 'abbceffg', 'abbcegjk', 'ghijklmn'}
    tw = ['ghijklmn', 'ghijklmn', 'ghjaabcc']
    cnt = 0

    
    #for t in tw[0:1]:
    ok = False
    pw = [asc(lt) for lt in lines]
    while not check(pw):
        pw = inc(pw)
        #db('Checking {}'.format(pw))
        db('{}'.format(toch(pw)))
    #db('OK {}'.format(toch(pw)))
    
        
    return toch(pw)

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,11, p1, p2, cmds)
if stats: print_stats()
#manual()
