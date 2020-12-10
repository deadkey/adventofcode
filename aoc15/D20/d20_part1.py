import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return int(line)

def getsoll(N):
    soll = [0] * N
    for i in range(2, N):
        if soll[i] == 0:
            #prime
            for k in range(i*i, N, i):
                soll[k] = i
    return soll


def getprimes(i, soll):
    solval = soll[i]
    primes = []
    while solval > 0:
        primes.append(solval)
        i //= solval
        solval = soll[i]
    primes.append(i)
    return primes

def divs(primes):
    if len(primes) == 0: return [1]
    for key in primes.keys(): break
    val = primes.pop(key)
    li = divs(primes)
    li2 = list(li)
    for v in li:
        for mult in range(1, val+1):
            li2.append(v * key ** mult)
    return li2

def presents(h, soll):
    cnt = 0
    pr = Counter(getprimes(h, soll))
    divisors = divs(pr)
    su = sum(divisors)
    return 10 * su



def p1(v):
    val = int(v.strip())
    #val = 130
    N = 4000000
    soll = getsoll(N)
    for h in range(1, 4000000):
        cnt = presents(h, soll)
        
        if h % 100000 == 0: db(h, cnt)

        if cnt > val:
            return h
    return -1

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,20, p1, p2, cmds)
if stats: print_stats()
#manual()

#submitted: 36960