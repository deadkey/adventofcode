import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

def p1(v, log=False):
    lines = v.split('\n')
    grid = [line for line in lines]
    

    letters = []

    return 0

def p2(v, log=False):
    return 0

def get_day():
    return 19

def get_year():
    return 2017

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, samples_only = True)
