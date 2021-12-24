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

def unpack(data):
    if len(data) == 2:
        return data[0], data[1], None
    else:
        return data[0], data[1], data[2]

def solve(data, values = None, cnt= 1):
    if values == None:
        values = {'w': 0, 'x': 0, 'y': 0, 'z': 0, None: 0}

    inpcnt = cnt
    for i in range(len(data)):
        d = data[i]

        op, var, val = unpack(d)
        
        if not isint(val):
            val = values[val]

        if op == 'inp':
            values[var] = 'inp' + str(inpcnt)
            inpcnt += 1
        if op == 'mul':
            if values[var] != 0:
                
                if val == 0:
                    values[var] = 0
                else:
                    old = values[var]
                    
                    if not isint(old):
                        old =  '(' + str(old) + ')'

                    values[var] = str(old) + ' * ' + str(val)
        if op == 'add':
            old = values[var]
            
            if not isint(old):
                old =  '(' + str(old) + ')'
            if old == 0:
                values[var] = val
            elif val != 0:
                values[var] = '(' + str(old) + ' + ' + str(val) + ')'
        if op == 'div':
            if values[var] != 0:
                old = values[var]
                if not isint(old):
                    old =  '(' + str(old) + ')'
                values[var] = str(old) + '/' + str(val)
        if op == 'mod':
            if values[var] != 0:
                
                old = values[var]
                if not isint(old):
                    old =  '(' + str(old) + ')'
                values[var] = '(' + str(old) + ' % ' + str(val) + ')'
        if op == 'eql':
            old = values[var]
            if not isint(old):
                old =  '(' + str(old) + ')'
            values[var] = '(' + str(old) + ' == ' + str(val) +')'
        
    for var, val in values.items():
        db(f'{var} =  {val}')

def runprog(data, modelno):
    values = {'w': 0, 'x': 0, 'y': 0, 'z': 0, None: 0}

    inpcnt = 0
    for i in range(len(data)):
        d = data[i]

        op, var, val = unpack(d)
        
        if not isint(val):
            val = values[val]

        if op == 'inp':
            values[var] = modelno[inpcnt]
            inpcnt += 1
        if op == 'mul':
            
            old = values[var]
            if not isint(val):
                val = values[val]
            
            values[var] = old * val
        if op == 'add':
            old = values[var]
            if not isint(val):
                val = values[val]

            values[var] =  old + val
        if op == 'div':
            old = values[var]
            if not isint(val):
                val = values[val]

            values[var] =  old // val
        if op == 'mod':
            old = values[var]
            if not isint(val):
                val = values[val]

            values[var] =  old % val
        if op == 'eql':
            old = values[var]
            if not isint(val):
                val = values[val]

            values[var] = 1 if old == val else 0
        
    for var, val in values.items():
        db(f'{var} =  {val}')    

def byhand(data):
    test = [0, 1, 2, 3, 5, 6, 8]
    match = {0:(13, 7), 1:(12, -3), 2:(11,-5), 3:(4, -8), 5:(10, -1), 6:(7, -6), 8:(9, 3)}
    modelno = [0] * 14
    
    modelno[0] = 1
    modelno[13] = 8
    
    modelno[1] = 4
    modelno[12] = 1

    modelno[2] = 6
    modelno[11] = 1

    modelno[3] = 9
    modelno[4] = 1

    modelno[5] = 2
    modelno[10] = 1

    modelno[6] = 7
    modelno[7] = 1

    modelno[8] = 1
    modelno[9] = 4
    db(modelno)
    runprog(data, modelno)
    return ''.join(map(str, modelno))
    
def byhand2(data):
    test = [0, 1, 2, 3, 5, 6, 8]
    match = {0:(13, 7), 1:(12, -3), 2:(11,-5), 3:(4, -8), 5:(10, -1), 6:(7, -6), 8:(9, 3)}
    modelno = [0] * 14
    
    modelno[0] = 2
    modelno[13] = 9
    
    modelno[1] = 9
    modelno[12] = 6

    modelno[2] = 9
    modelno[11] = 4

    modelno[3] = 9
    modelno[4] = 1

    modelno[5] = 9
    modelno[10] = 8

    modelno[6] = 9
    modelno[7] = 3

    modelno[8] = 6
    modelno[9] = 9
    db(modelno)
    runprog(data, modelno)
    return ''.join(map(str, modelno))

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    su = 0
    values = {'w': 'inp2', 'x': 1, 'y': 'inp2 + 1', 'z': 'inp1 + 9', None: 0}
    #modelno = [9] *14


    #db('Running program')
    return byhand(data)
    #solve(data, values, 3)




def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2021,24, p1, p2, cmds)
if stats: print_stats()
#manual()
