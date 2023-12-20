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
 #88 not correct

def db(*a): 
    if DB: print(*a)

#crazy input, use multisplit? 
def parse(line):
    return lazy_ints(multisplit(line, ',')) 

def hash(word):
    val = 0
    for letter in word:
        
        asc  = ord(letter)
        val += asc
        val *= 17
        val %= 256
    return val


def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    box = dd(list)
    for  word in data[0]:
        if '=' in word:
            h, val = word.split('=')
            val = int(val)
            place = hash(h)
            li = box[place]
            placed = False
            for i, p in enumerate(li):
                if li[i][0] == h:
                    li[i] = h, val
                    placed = True
            if not placed:
                li.append((h, val))
            

        if '-' in word:
            h = word.replace('-', '')
            place = hash(h)
            li = box[place]
            placed = False
            li = list(filter(lambda x: x[0] != h, li))
            box[place] = li


    for i in range(256):
        for k, v in enumerate(box[i]):
            su += (i + 1) * (k+1) * v[1]

        
    return su


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    val = 0
    for  word in data[0]:
        
        val = 0
        for letter in word:
            
            asc  = ord(letter)
            val += asc
            val *= 17
            val %= 256
        db(word, val)
        su += val
        
    return su




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2023,15, p1, p2, cmds)
if stats: print_stats()

#manual()
