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
    return lazy_ints(line.replace(',', ' ').split())

MARKED = -1

def win(board, nbr):
    for r in range(5):
        for c in range(5):
            if board[r][c] == nbr:
                board[r][c] = MARKED

    for r in range(5):
        cnt = 0
        for c in range(5):
            if board[r][c] == MARKED:
                cnt += 1
        if cnt == 5: return True
    for c in range(5):
        cnt = 0
        for r in range(5):
            if board[r][c] == MARKED:
                cnt += 1
        if cnt == 5: return True
    return False

def cnt(board):
    cnt = 0
    for r in range(5):
        
        for c in range(5):
            if board[r][c] != MARKED:
                cnt += board[r][c]
    return cnt



def play1(nbrs, boards):
    for nbr in nbrs:
        for board in boards:
            if win(board, nbr):
                return nbr * cnt(board)
    return 0

def play2(nbrs, boards):
    haswn = set()
    for nbr in nbrs:
        for i, board in enumerate(boards):
            if win(board, nbr):

                haswn.add(i)
                if len(haswn) == len(boards):
                    db(cnt(board), nbr)

                    return cnt(board) * nbr



    return 0

def p1(v):
    chunks = v.strip().split('\n\n')
    nbrs = parse(chunks[0])
    db(nbrs)
    boards = []
    for chunk in chunks[1:]:
        board = []
        lines = chunk.split('\n')
        for line in lines:
            board.append(parse(line))

        boards.append(board)

    db(boards)
    return play1(nbrs, boards)


def p2(v):
    chunks = v.strip().split('\n\n')
    nbrs = parse(chunks[0])
    db(nbrs)
    boards = []
    for chunk in chunks[1:]:
        board = []
        lines = chunk.split('\n')
        for line in lines:
            board.append(parse(line))

        boards.append(board)

    db(boards)
    return play2(nbrs, boards)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,4, p1, p2, cmds)
if stats: print_stats()
#manual()
