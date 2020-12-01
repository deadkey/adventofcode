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

def p1(v, log=False):
    lines = v.strip().split('\n')
    entry = []
    for line in lines:
        val = int(line)
        entry.append(val)
    for i in range(len(entry)):
        a = entry[i]
        for j in range(i+1, len(entry)):
            b = entry[j]
            if a + b == 2020:
                return a * b
    return 0

def p2(v, log=False):
    lines = v.strip().split('\n')
    entry = []
    for line in lines:
        val = int(line)
        entry.append(val)

    for i in range(len(entry)):
        a = entry[i]
        for j in range(i+1, len(entry)):
            b = entry[j]
            for k in range(j, len(entry)):
                c = entry[k]
                if a + b + c == 2020:
                    return a * b * c
    
    return 0


S = "run samples"
SO = "samples only"
IO = "input only"
FF = "force fetch"
DB = 1
PR = "print input"

if __name__ == '__main__':
    cmds = {S}
    #data = sys.stdin.read()
    run(get_year(), get_day(), p1, p2, cmds)
