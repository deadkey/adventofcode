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

def merge(li, sep = ''):
    return sep.join(map(str, li))

def removeall(s, arg):
    for a in arg:
        s = s.replace(a, ' ')
    return s


def int_convert(s):
    if isint(s):
        return int(s)
    return s

INF = 10**30
def multisplit(s, schars):
    out = [s]
    for delim in schars:
        newout = []
        for word in out:
            spl = word.split(delim)
            newout.extend(spl)
        out = newout
    #reg = '|'.join(schars)
    #out =  re.split(reg, s)
    out = list(map(lambda x: x.strip(), out))
    out = filter(lambda x: len(x.strip())> 0, out)

    return out

def tochunks(v):
    ch = v.split('\n\n')
    lines = []
    for c in ch:
        lines.append(c.split('\n'))
    return lines


def lazy_ints(li):
    li = list(map(int_convert, li)) 
    if len(li) == 1:
        return li[0]
    return li

def mul(li):
    p = 1
    for v in li:
        p *= v
    return p

def add(li):
    ints = filter(lambda x: isint(x), li)
    return sum(ints)


def print_stats():

    v = open("real.txt", 'r').read().strip('\n')
    lines = len(v.strip().split('\n'))
    print('Len input: {} lines {} chars'.format(lines, len(v)))
    