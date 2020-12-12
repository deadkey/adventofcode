import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph
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
        vm.used = set()
        vm.running = True
        

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


def exec(vm, op,r, offset = None):
    db(op, r, offset)
    reg = vm.reg
    if op == 'hlf':
        reg[r] //=2
    if op == 'tpl':
        reg[r] *= 3
    if op == 'inc':
        reg[r] += 1
    if op == 'jmp':
        return r
    if op == 'jie':
        if reg[r] % 2 == 0:
            return offset
    if op == 'jio':
        if reg[r] == 1:
            return offset
    return 1
     

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(multisplit(line, ',', ' '))

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    ins = [parse(line) for line in lines]
    p = Program(ins, exec, reg = {'a': 1, 'b': 0})

    p.run()
    return p.reg['b'] 

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,23, p1, p2, cmds)
if stats: print_stats()
#manual()
