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


class Program:
    def __init__(vm, ins, exec_func, reg = None):
        vm.ins = ins
        if reg == None: reg = defaultdict(int)
        vm.reg = reg
        vm.exec_func = exec_func
        vm.i = 0
        vm.used = set()
        vm.running = True
        vm.counter = Counter()
        vm.steps = 0
    
        
    #Wite a function that returns the offset!
    #def exec(vm, op,r, offset = None): 
    def step(vm):
        ins = vm.ins
        vm.i += vm.exec_func(vm, *ins[vm.i])
        vm.counter[vm.i] += 1
        if vm.steps % 10000== 0 :
            db(vm.i, 'a', vm.reg['a'], ', ', 'b', vm.reg['b'],', ',  'c', vm.reg['c'], ', ', 'd', vm.reg['d'])
        if vm.i >= len(ins):
            print("Terminated")
            vm.running = False
        
        
    def run(vm):
        ins = vm.ins
        reg = vm.reg
        vm.running = True
        MAX = 10000
        
        while vm.running:
            vm.step()
            vm.steps += 1
        res = max(vm.counter, key = lambda x: vm.counter[x])
        #db(f'MOST COMMON STEP {res}')
            
        return vm.i >= len(ins)




def exec(vm, op, val1, val2 = None):
    reg = vm.reg
    def val(v):
        return v if isint(v) else reg[v]
    if op == 'cpy':
        r = val2
        reg[r]  = val(val1)
        #db(r, reg[r])
    if op == 'inc':
        reg[val1] += 1
        #db(val1, reg[val1])
    if op == 'add':
        reg[val1] += val(val2)
        #db(val1, reg[val1])
    if op == 'set':
        reg[val1] = val(val2)

    if op == 'dec':
        reg[val1]   -= 1

        #db(val1, reg[val1])
    if op == 'jnz':
        x = val(val1)
        
        if x != 0: return val(val2)
    if op == 'mul':
        reg[val1] *= val(val2)

    if op == 'tgl':
        x = val(val1)
        if 0 <= vm.i + x < len(vm.ins):
            oth_op = vm.ins[vm.i + x][0]
            new_op = {'inc':'dec', 'dec': 'inc','jnz': 'cpy', 'cpy': 'jnz', 'add': 'jnz', 'set': 'jnz', 'tgl': 'inc'}
            #db(vm.i, x, vm.ins)
            #db(vm.ins[vm.i + x], new_op[oth_op])
            vm.ins[vm.i + x][0] = new_op[oth_op]

    return 1


def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())
    

def p1(v):
    lines = v.strip().split('\n')
    reg = dd(int)
    reg['a'] = 7
    ins = [parse(line) for line in lines]
    p = Program(ins, exec, reg)
    p.run()
    return p.reg['a']

def p2(v):
    lines = v.strip().split('\n')
    reg = dd(int)
    reg['a'] = 12
    ins = [parse(line) for line in lines]
    p = Program(ins, exec, reg)
    p.run()
    return p.reg['a']

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,23, p1, p2, cmds)
if stats: print_stats()
#manual()
