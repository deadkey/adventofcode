import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
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

def J(n, k):
    r = 0
    for i in range(2, n+1):
        r = (r + k)%i
    return r    


def Jdub(I, K):
    f = 1

    for n in range(2, I+1):
        i = I - n + 1
        k = K * i
        f = (f + k -1)%n +1
        db(f)
        k += 1
    return f    


def Jinc(I):
    f = 1
    k = I + 1
    for n in range(2, I+1):
        f = (f + k -1)%n +1
        
        db(f'n = {n}, k = {k} f = {f}')
        k -= 1
        
    return f    


def J2(I):
    f = 1

    for n in range(2, I+1):
        k = n//2 + 1
        f = (f + k -1)%n + 1
        db(f'n = {n}, k = {k} f = {f}')
    return f    


def simulate(N):
    li = [x+1 for x in range(N)]
    ind = 0
    for i in range(N-1):
        n = len(li)
        elf = li[ind]
        half = (n//2 + ind) % n
        rm = li.pop(half)
        ind= li.index(elf)
        ind += 1
        ind %= len(li)
        #db(len(li))


    return li[0]

def p1(v):
    return J(3004953, 2) +1

def generate(N):
    for n in range(1, N +1):
        rs = simulate(n)
        db(f'n = {n} rs = {rs}')

def testother(ELF_COUNT):
    
    left = deque()
    right = deque()
    for i in range(1, ELF_COUNT+1):
        if i < (ELF_COUNT // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]    

def p2(v):
    #generate(1000)
    #return
    x = int(v)
    return testother(x)
    startlog = int(math.log(x, 3))
    
    res = int(math.pow(3, startlog))
    db(x, startlog, res)
    if x <= 2 * res:
        diff = x - res
        return diff
    else:
        diff = x - 2 * res
        return res + 2 * diff
    #return J2(3004953) +1


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,19, p1, p2, cmds)
if stats: print_stats()
#manual()
