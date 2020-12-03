import requests
from secret import session
import os, glob, time
from datetime import datetime
import bs4
import logging as log

def is_integer(i):
    try:
        int(i)
        return True
    except:
        return False

def int_convert(s):
    if is_integer(s):
        return int(s)
    return s


def multisplit(s, schars):
    out = []
    curr = ''
    for c in s:
        if c in schars:
            if curr:
                out.append(curr)
                curr = ''
        else:
            curr += c
    if curr: 
        out.append(curr)
    return out
    
def lazy_ints(li):
    return list(map(int_convert, li)) 

def print_stats():

    v = open("real.txt", 'r').read().strip('\n')
    lines = len(v.strip().split('\n'))
    print('Len input: {} lines {} chars'.format(lines, len(v)))
    