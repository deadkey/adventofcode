import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

from collections import *

class Program:
    def __init__(vm, ins, exec_func, reg = None):
        vm.ins = ins
        if reg == None: reg = defaultdict(int)
        vm.reg = reg
        vm.exec_func = exec_func
        vm.i = 0
        vm.cnt = 0
        vm.used = set()
        vm.running = True
        
    #Wite a function that returns the offset!
    #def exec(vm, op,r, offset = None): 
    def step(vm):
        ins = vm.ins
        vm.i += vm.exec_func(vm, *ins[vm.i])
        if vm.i >= len(ins):
            print("Terminated")
            vm.running = False
        
        
    def run(vm):
        ins = vm.ins
        reg = vm.reg
        vm.running = True
        
        while vm.running:
            vm.step()
            
        return vm.i >= len(ins)

def exec(vm, op, val1, val2 = None):
    def val(v): 
        if isint(v): return v
        else: return vm.reg[v]
    if op == 'set':
        y = val(val2)
        vm.reg[val1] = y
    if op == 'sub':
        y = val(val2)
        vm.reg[val1] -= y
    if op == 'mul':
        vm.cnt += 1
        y = val(val2)
        vm.reg[val1] *=y
    if op == 'jnz':
        x = val(val1)
        if x!= 0: return val(val2)
    return 1
    
    


def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())
    

def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    data = [parse(line) for line in lines]
    p = Program(data, exec)
    p.run()
    return p.cnt

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2017,23, p1, p2, cmds)
if stats: print_stats()
#manual()
