import requests
from secret import session
import os, glob, time
from datetime import datetime
import bs4
import logging as log
import re


from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def isint(i):
    try:
        int(i)
        return True
    except:
        return False


def removeall(s, *arg):
    for a in arg:
        s = s.replace(a, '')
    return s


def int_convert(s):
    if isint(s):
        return int(s)
    return s

INF = 10**30
def togrid(lines): 
    grid = [list(line) for line in lines]
    return grid, len(grid), len(grid[0])

def tointgrid(lines): 
    grid = [list(map(int, line.split())) for line in lines]
    return grid, len(grid), len(grid[0])


def copygrid(grid):
    R = len(grid)
    nxt =[]
    for r in range(R):
        nxt.append(list(grid[r]))
    return nxt

def emptygrid(R, C, val):
    return [[val] * C for r in range(R)]

def cntgrid(grid, val):
    return sum(grid[r].count(val) for r in range(len(grid)))


def get4nb(r, c, rmin = -INF, rmax = INF, cmin = -INF, cmax = INF):
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb     

def get8nb(r, c, rmin = -INF, rmax = INF, cmin = -INF, cmax = INF):
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb     

def printgrid(grid):
    for r in range(len(grid)):
        out = ''.join(map(str, grid[r]))
        print(out)

def multisplit(s, *schars):
    reg = '|'.join(schars)
    out =  re.split(reg, s)
    return list(map(lambda x: x.strip(), out))


def lazy_ints(li):
    return list(map(int_convert, li)) 

def print_stats():

    v = open("real.txt", 'r').read().strip('\n')
    lines = len(v.strip().split('\n'))
    print('Len input: {} lines {} chars'.format(lines, len(v)))
    