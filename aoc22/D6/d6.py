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
    #return lazy_ints(line.split())
    return lazy_ints(multisplit(line, ' ')) 
    
def pbot(datastream):
    #datastream = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

# initialize the last four characters to empty strings
    last_four = ["", "", "", ""]

    # initialize the index to 0
    i = 0

    # loop until a start-of-packet marker is found
    while True:
        # get the next character from the datastream
        char = datastream[i]

        # add the character to the list of last four characters
        last_four = last_four[1:] + [char]

        # check if the last four characters are all different
        if len(set(last_four)) == 4 and last_four[0] != "": #had to add: and last_four[0]
            # if so, print the index and break out of the loop
            return i + 1 #wrong by one
            break

        # increment the index
        i += 1


def p1(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    txt = data[0]
    for start in range(3, len(txt)):
        s = set(txt[start-3: start + 1])
        if len(s) == 4:
            return start + 1

def p2(v):
    lines = v.strip().split('\n')
    chunks = tochunks(v)
    data = [parse(line) for line in lines]
    su = 0
    txt = data[0]
    for start in range(13, len(txt)):
        s = set(txt[start-13: start + 1])
        if len(s) == 14:
            return start + 1

    return su

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(pbot(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)
if not io: run_samples(p1, p2, cmds)

if 'manual' in cmds: 
    manual()
    exit()

if not so: run(2022,6, p1, p2, cmds)
if stats: print_stats()

#manual()
