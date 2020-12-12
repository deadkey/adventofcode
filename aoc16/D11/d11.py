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
from itertools import combinations 
from heapq import heappush as push, heappop as pop
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return -1 #int(line)

def cp(fmap):
    fmapnew = [list(li) for li in fmap]
    return fmapnew

def legal(li):
    all = set(li)
    generators = set()
    microchips = set()
    for item in all:
        if item[-1] == 'M':
            microchips.add(item)
        else:
            generators.add(item)
    for chip in microchips:
        G = chip[0] + 'G'
        if len(generators)> 0 and G not in generators:
            return False
    return True


def poss(E, fmap):
    #go upp or down
    pb = []
    Eu = E + 1
    Ed = E -1
    levels = [Eu, Ed]
    for level in levels:
        if 0<= level < 4:

            # take one or two items
            for no in range(1, 3):
                comb = combinations(fmap[E], no)
                #comb is list of lists
                for c in list(comb):
                    if legal(c):
                        left = []
                        
                        for item in fmap[E]:
                            if item not in c:
                                left.append(item)
                        merged = list(c) + fmap[level]
                        if legal(merged) and legal(left):
                            fmapnew = cp(fmap)
                            fmapnew[level] =merged
                            fmapnew[E] = left 
                            pb.append((level, fmapnew))
    return pb
                        
    # only leave legal state and enter legal state.
def tostring(E, F):
    out = [str(E)]
    for i, level in enumerate(F):
        out.append(str(i))
        for item in sorted(level):
            out.append(item)
    return ' '.join(out)


def solve(S, end):
    #g list with lists with tuples distance, other node
    # Dijkstra from S. Check t optionally
    q = [S]
    moves = 0
    seen = set()
    st = tostring(S[0], S[1])
    T = tostring(end[0], end[1])
    q = [(S[0], S[1], st)]
    seen.add(st)
    while q:
        q2 = []
        #db('#################################')
        db('Moves', moves)

        for E, state, name in q:
            #db(E, name)
            if name == T: return moves
            for nxtstate in poss(E, state):
                #db(f'Generated possible state: {nxtstate}')
                tup = tostring(nxtstate[0], nxtstate[1])
                if tup not in seen:
                    #db('Not seen')
                    seen.add(tup)
                    q2.append((nxtstate[0], nxtstate[1], tup))
        q = q2

        moves += 1
        

    return 10 ** 10

def p1(v):
    F = [[] for _ in range(4)]
    #F[0] = ['HM', 'LM']
    #F[1] = ['HG']
    #F[2] = ['LG']
    F[0] = ['SG', 'SM', 'PG', 'PM']
    F[1] = ['TG', 'RG', 'RM', 'CG', 'CM']
    F[2] = ['TM']
    END = [[], [], [], []]
    for i, level in enumerate(F):
        for item in level:
            END[3].append(item)
   
    ## Elevator must have something
    # For each microshio there has to be a generator.
    # MAx two things in elevator. 
    E = 0
    startstate = E, F
    endstate = 3, END
    return solve(startstate, endstate)
    

def p2(v):
    F = [[] for _ in range(4)]
    #F[0] = ['HM', 'LM']
    #F[1] = ['HG']
    #F[2] = ['LG']
    F[0] = ['SG', 'SM', 'PG', 'PM', 'EG', 'EM', 'DG', 'DM']
    F[1] = ['TG', 'RG', 'RM', 'CG', 'CM']
    F[2] = ['TM']
    END = [[], [], [], []]
    for i, level in enumerate(F):
        for item in level:
            END[3].append(item)
   
    ## Elevator must have something
    # For each microshio there has to be a generator.
    # MAx two things in elevator. 
    E = 0
    startstate = E, F
    endstate = 3, END
    return solve(startstate, endstate)
    



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,11, p1, p2, cmds)
if stats: print_stats()
#manual()
