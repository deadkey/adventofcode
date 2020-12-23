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

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,22, p1, p2, cmds)
if stats: print_stats()
#manual()
