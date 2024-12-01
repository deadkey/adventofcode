import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from util import run
import sys


def get_day(): return date.today().day
def get_year(): return date.today().year
def db(*a):
    if DB: print(*a)


def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    for line in lines:
        pass
    return cnt

def p2(v):
    return p1(v)



DB = 1


if __name__ == '__main__':
    data = sys.stdin.read()
    print("Part 1: {}".format(p1(data)))
    print("Part 2: {}".format(p2(data)))