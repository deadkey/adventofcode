import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import drawgraph
from program import Program
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a):
    if DB: print(*a)

def p1(v):
    lines = v.strip().split('\n')
    ins = [lazy_ints(line.split()) for line in lines]
    p = Program(ins, exec_ins)
    ok = p.run() 
    
    return p.reg['acc']

def exec_ins(vm, op, val): 
    reg = vm.reg
    if vm.i in vm.used:
        vm.running = False
        return 0
    vm.used.add(vm.i)
    if op == 'acc':
        reg['acc'] += val
        return 1
    elif op == 'jmp':
        return val
    elif op == 'nop':
        return 1
    return 0

def p2(v):
    lines = v.strip().split('\n')
    ins = [lazy_ints(line.split()) for line in lines]
    for i, (op, val) in enumerate(ins):
        if op == 'nop': continue

        iins = list(ins)
        if op == 'jmp':
            iins[i] = ('nop', val)
            
        if op == 'nop':
            iins[i] = ('jmp', val)
            
        p = Program(iins, exec_ins)
        ok = p.run() 
        if ok:
            return p.reg['acc']
        
    return -999



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
    

cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(get_year(),  get_day(), p1, p2, cmds)
if stats: print_stats()
#manual()
