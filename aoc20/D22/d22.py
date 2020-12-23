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
    
def sim(decks):
    turn = 0
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        t1 = decks[0].popleft()
        t2 = decks[1].popleft()
        if t1 > t2:
            decks[0].append(t1)
            decks[0].append(t2)
        else:
            decks[1].append(t2)
            decks[1].append(t1)
        turn += 1
    db(turn)
    db(decks)
    if len(decks[0]) > 0: return decks[0]
    return decks[1]

def p1(v):
    pl = chunks(v)
    decks = []

    for p in pl:
        cards = [parse(c) for c in p.split('\n')]
        d = deque()
        for card in cards[1:]:
            d.append(card)
        decks.append(d)

    db(decks)
    winner = list(sim(decks))
    score = 0
    for i, c in enumerate(winner[::-1]):
        score += (i + 1) * c
    return score

def score(winner):
    winner = list(winner)
    sc = 0
    for i, c in enumerate(winner[::-1]):
        sc += (i + 1) * c
    return sc

def check(decks, dp):
    pl1 = '0 ' + ''.join(map(str, decks[0])) + ' 1 ' + ''.join(map(str, decks[1]))
    if pl1 in dp: return True

    dp.add(pl1)
    return False

def rec(decks):
    
    dp = set()
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        t1 = decks[0].popleft()
        t2 = decks[1].popleft()
        if check(decks, dp): return decks[0], []

        if t1 <= len(decks[0]) and t2 <= len(decks[1]):
            newdecks= []
            d1 = deque()
            for c in range(t1):
                d1.append(decks[0][c])
            d2 = deque()
            for c in range(t2):
                d2.append(decks[1][c])

            d1, d2 = rec([d1, d2])
            if len(d1) > 0:
                decks[0].append(t1)
                decks[0].append(t2)
            else:
                decks[1].append(t2)
                decks[1].append(t1)
        else:

            if t1 > t2:
                decks[0].append(t1)
                decks[0].append(t2)
            else:
                decks[1].append(t2)
                decks[1].append(t1)
    return decks

def p2(v):
    pl = chunks(v)
    decks = []

    for p in pl:
        cards = [parse(c) for c in p.split('\n')]
        d = deque()
        for card in cards[1:]:
            d.append(card)
        decks.append(d)
    dp = set()
    p1, p2 = rec(decks)
    db(p1, p2)
    winner = p1 if p1 else p2
    return score(winner)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,22, p1, p2, cmds)
if stats: print_stats()
#manual()
