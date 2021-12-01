import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import math
from collections import defaultdict as dd, Counter

def parse(line):
    return lazy_ints(line.split())


def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 0
    for i in range(len(data)):
        v = data[i]
        su += v
        
    return su
    
def p2(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    return p1(v)

v = open("real.txt", 'r').read().strip('\n')

lines = v.strip().split('\n')
data = [parse(line) for line in lines]
print('part_1: \n{}\npart_2: \n{}'.format(p1(v), p2(v)))