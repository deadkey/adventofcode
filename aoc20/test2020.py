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
    su = 0
    for line in lines:
        n = int(line)
        su += (n//3) -2
    return su


def p2(v, log=False):
    lines = v.strip().split('\n')
    su = 0
    for line in lines:
        n = int(line)
        su += fuel(n)
    return su


def fuel(n):
    s = 0
    f = (n//3) -2
    while f > 0:
        s+= f
        f = (f//3) -2
    return s

def pp(*v):
    if PP:
        print(v) 


S = "run_samples"
SO = "samples only"
IO = "input only"
FF = "force fetch"
DB = "debug"

if __name__ == '__main__':
    db("hej")
    cmds = {S}
    run(2019, 1, p1, p2, cmds)
   
