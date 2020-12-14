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
    return lazy_ints(multisplit(line, '[', ']', '='))

def tobin(val, mask):
    bval = bin(int(val))[2:]
    bval = '0' * (len(mask) - len(bval)) + bval
    return bval

def apply(bval ,mask):
    out = []
    db('bval', bval)
    for i, b in enumerate(mask):
        if b == '0': 
            out.append(bval[i])
        elif b == '1':
            out.append('1')
        else: out.append(mask[i])
    db('out', ''.join(out))
    return ''.join(out)  

def tomasks(mask):
    oneMask = int(mask.replace('X', '0'), 2)
    zeroStr = mask.replace('X', '1')
    zeroMask = (2 ** len(mask) -1) ^ int(zeroStr, 2)
    return [zeroMask, oneMask]

def apply1(val ,masks):
    zm = masks[0]
    om = masks[1]
    db(val, zm, om)
    val = val | om
    val = (val | zm) ^ zm
    return val

def exec_p1(mem, masks, op, val1, val2 = None):
    if op == 'mem':
    
        mem[val1] = apply1(val2, masks)
    else:
        
        masks = tomasks(val1)
    return masks

def exec_p2(mem, masks, op, val1, val2 = None):
    if op == 'mem':
        for adr in gen(val1, masks):
            db(f'Setting {adr} to {val2}')
            mem[adr] = val2

    else:
        masks = tomasks(val1)
    return masks
           
def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    data = [parse(line) for line in lines]
    mask = data[0][1]
    masks = tomasks(mask)
    mem = defaultdict(int)
    for i, line in enumerate(data):
        masks = exec_p1(mem, masks, *line)
    return sum(mem.values())
    

def gen(val, masks):
    zm, om = masks
    val |= om
    x = (2 ** 36 -1) ^ zm ^ om
    xind = []
    bs = []
    alt = []
    for i in range(36):
        if (1 << i) & x:
            xind.append(i)
    for i in range(2 ** len(xind)):
        add = 0
        rem = 0
        for k in range(len(xind)):
            if (1 << k) & i:
                add |= (1 << xind[k])
            else:
                rem |= (1 << xind[k])
        alt.append((val | add |rem) ^ rem)
   
    return alt

def p2(v):
    lines = v.strip().split('\n')
    cnt = 0
    data = [parse(line) for line in lines]
    mask = data[0][1]
    masks = tomasks(mask)
    mem = defaultdict(int)
    for i, line in enumerate(data):
        masks = exec_p2(mem, masks, *line)

    return sum(mem.values())

    '''
    lines = v.strip().split('\n')
    mask = lines[0].split('=')[-1].strip()
    
    #db(mask)
    cnt = 0
    data = [parse(line) for line in lines[1:]]
    #db(data)
    mem = defaultdict(int)
    for i, line in enumerate(data):
        if len(line) < 3:
            db(i, line)
            mask = line[-1].strip()
            db('mask', mask)
        else:
            _, m, val = line
            val = int(val)
            bval = tobin(val, mask)
            bm = tobin(m, mask)
            am = apply(bm, mask)

            for s in SU(am):
                mem[s] = val
    su = 0
    for key, val in mem.items():
        su += val
    return su
    '''


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,14, p1, p2, cmds)
if stats: print_stats()
#manual()
