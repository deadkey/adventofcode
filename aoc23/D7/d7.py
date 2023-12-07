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
    card, bid = multisplit(line, ' ')

    return card, int(bid)

O = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
order = {k: i for i, k in enumerate(O)}


def best(c):
    b =  10
    
    if 'J' in c:
        for oth in O:
            if oth != 'J':
                tmp = c.replace('J', oth)
                alt = gettype(tmp)
                b = min(alt, b)
        return b
    
    return gettype(c)


def getorder(c):
    val = []
    for let in c:
        val.append(order[let])
    return val

def gettype(c):
    cnt = Counter()
    for let in c:
        cnt[let] += 1
    

    for let in c:
        if cnt[let] == 5:
            return 0

    for let in c:
        if cnt[let] == 4:
            return 1
    
    hasthree = False
    for let in c:
        if cnt[let] == 3:
            hasthree = True
    
    pairs = 0
    for let in c:
        if cnt[let] == 2:
            if hasthree:
                return 2
            else:
                pairs += 1
   
    pairs = pairs //2

    if pairs == 1 and hasthree:
        return 2 #full house
    
    if pairs == 0 and hasthree:
        return 3

    if pairs == 2:
        return 4
    
    if pairs == 1:
        return 5
    
    if set(c) == 5:
        return 6
    
    return 7
    
            
## WRONG 250862783 sorting order for J is wrong
    

def p2(v):
    order['J'] = 20
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    cards = []
    for i in range(len(data)):
        c, bid = data[i]
        ss = getorder(c)
        tt = best(c)
        cards.append((tt, ss, c, bid))
        

    cards.sort()
    db(cards)

    bid = cards[0][-1]
    for i, card in enumerate(cards):
        bid = card[-1]
        L = len(cards) - i
        su += bid * L
        db(bid, L)
    return su


def p1(v):
    order['J'] = 3
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    cards = []
    for i in range(len(data)):
        c, bid = data[i]
        ss = getorder(c)
        tt = gettype(c)
        cards.append((tt, ss, c, bid))
        
    cards.sort()
    db(cards)

    bid = cards[0][-1]
    for i, card in enumerate(cards):
        bid = card[-1]
        L = len(cards) - i
        su += bid * L
        db(bid, L)
    return su

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,7, p1, p2, cmds)
if stats: print_stats()

#manual()
