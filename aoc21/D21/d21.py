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
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())

univ = {}
pos = [0] * 10
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            su = i + j + k
            pos[su] += 1

def solve(turn, pos1, pos2, score1, score2):
    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1

    t = turn, pos1, pos2, score1, score2
    if t in univ:
        return univ[t]
    
    tot = [0, 0]
    for steps, cnt in enumerate(pos):
        if cnt == 0: continue


        if turn == 0:
            new1 = (pos1 + steps -1) % 10 + 1
            newscore1 = score1 + new1

            w1, w2 = solve(1, new1, pos2, newscore1, score2)
            tot[0] += cnt * w1
            tot[1] += cnt * w2
        if turn == 1:
            new2 = (pos2 + steps -1) % 10 + 1
            newscore2 = score2 + new2

            w1, w2 = solve(0, pos1, new2, score1, newscore2)
            tot[0] += cnt * w1
            tot[1] += cnt * w2
    
    univ[t] = tot

    return tot

def play2(start):
    startt = 0, start[0], start[1], 0, 0
    univ = dd(int)
    univ[startt] =  1
    wins = [0, 0]
    while len(univ):
        new_univ = dd(int)
       
        for t, univ_cnt in list(univ.items()):
            turn, pos1, pos2, score1, score2 = t
            for steps, cnt in enumerate(pos):
                if cnt == 0: continue


                if turn == 0:
                    new1 = (pos1 + steps -1) % 10 + 1
                    newscore1 = score1 + new1

                    if newscore1 >= 21:
                        wins[0] += univ_cnt * cnt
                    else:
                        tu = 1, new1, pos2, newscore1, score2
                        new_univ[tu] += univ_cnt * cnt
                    
                    
                if turn == 1:
                    new2 = (pos2 + steps -1) % 10 + 1
                    newscore2 = score2 + new2
                    if newscore2 >= 21:
                        wins[1] += univ_cnt * cnt
                    else:
                        tu = 0, pos1, new2, score1, newscore2
                        new_univ[tu] += univ_cnt * cnt
                
        univ = new_univ
    
    return max(wins)    




def play(pos):
    turn = 0
    die = 1
    points = [0, 0]
    no = 0
    while True:
        steps = die * 3 + 1 + 2
        die += 3

        pos[turn] = (pos[turn] + steps)
        while pos[turn] > 10:
            pos[turn] -= 10
        points[turn] += pos[turn]

        no += 3
        if points[turn] >= 1000:
            return min(points), no
        #db(points)

        turn += 1
        turn %= 2

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    players = [data[0][-1], data[1][-1]]
    los, no = play(players)
    db(los, no)
    return los * no


def p2_rec(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    players = [data[0][-1], data[1][-1]]
    w1, w2 = solve(0, data[0][-1], data[1][-1], 0, 0)
    mx = max(w1, w2)
    mn = min(w1, w2)
    return mx

def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    players = [data[0][-1], data[1][-1]]
    return play2(players)
   


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,21, p1, p2, cmds)
if stats: print_stats()
#manual()
