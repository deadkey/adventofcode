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
        op, val = ins[vm.i]
        vm.i += vm.exec_func(vm, op, val)
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

