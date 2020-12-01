import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
import sys


def get_day(): return date.today().day
def get_year(): return date.today().year
def db(a):
    if DB: print(a)

def p1(v):
    lines = v.strip().split('\n')
    su = 0
    for line in lines:
        val = int(line)
        
    return su

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
    data = sys.stdin.read()
    print("Part 1: {}".format(p1(data)))
    print("Part 2: {}".format(p2(data)))