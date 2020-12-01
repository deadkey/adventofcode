import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from util import run

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(a):
    if DB: print(a)

def p1(v):
    lines = v.strip().split('\n')
        
    return 0

def p2(v):
    lines = v.strip().split('\n')
    
    return 0


S = "run samples"
SO = "samples only"
IO = "input only"
FF = "force fetch"
DB = 1
PR = "print input"


if __name__ == '__main__':
    cmds = {S, 
    #'submit1',
    #'submit2' 
    }
    run(get_year(), get_day(), p1, p2, cmds)
