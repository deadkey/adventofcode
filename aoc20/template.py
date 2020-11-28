import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(a):
    if DB == "debug": print(a)

def p1(v, log=False):
    lines = v.strip().split('\n')
        
    return 0

def p2(v, log=False):
    lines = v.strip().split('\n')
    
    return 0


S = "run_samples"
SO = "samples only"
IO = "input only"
FF = "force fetch"
DB = "debug"

if __name__ == '__main__':
    cmds = {S, DB}
    run(get_year(), get_day(), p1, p2, cmds)
