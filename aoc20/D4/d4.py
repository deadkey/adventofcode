import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: '))
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(*a):
    if DB: print(*a)

def p1(v):
    pap = v.strip().split('\n\n')
    cnt = 0
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for pp in pap:
        li = pp.split()
        m = {}
        for f in li:
            fi, val = f.split(':')
            m[fi] = val
        if check1(m):
            cnt += 1

    return cnt

def check1(m):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for f in fields:
        if f not in m:
            return False
    return True

def check2(m):
    if not check1(m): return False
    ok = True
    ok = ok and inside(m['byr'], 1920, 2002)
    ok = ok and inside(m['iyr'], 2010, 2020)
    ok = ok and inside(m['eyr'], 2020, 2030)
    db('First', ok)
    hu = m['hgt']
    u = hu[-2:]
    h = hu[0:-2]
    if u == 'cm': ok = ok and inside(h, 150, 193)
    elif u == 'in': ok = ok and inside(h, 59, 76)
    else:
        ok = False
    hcl = m['hcl']
    ok = ok and iscol(hcl)
    db('Sec', ok)
    
    acc = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    ecl = m['ecl']
    ok = ok and ecl in acc
    pid = m['pid']
    ok = ok and ispid(pid)
    return ok


def ispid(p):
    return len(p) == 9 and all(x.isdigit() for x in p)    

def iscol(col):
    return col[0] == '#' and all(ord('0') <= ord(asc) <= ord('9') or ord('a') <= ord(asc) <= ord('f') for asc in col[1:])

    
def inside(val, mn, mx):
    return isint(val) and mn <= int(val) <= mx


def p2(v):
    pap = v.strip().split('\n\n')
    cnt = 0
    for pp in pap:
        li = pp.split()
        m = {}
        for f in li:
            fi, val = f.split(':')
            m[fi] = val
        if check2(m):
            cnt += 1

    return cnt


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    res1 = p1(v)
    res2 = p2(v)
    print('part_1: {}'.format(res1))
    print('part_2: {}'.format(res2))

FF = "force fetch"
DB = 0
PR = "print input"
so = 0
io = 0
stats = 0
cmds = []

def get_args():
    global stats, so, io, DB    
    for arg in sys.argv[1:]:
        if arg == 'f':
           cmds.append(FF)
        if arg == 's1' or  arg == '1':
           cmds.append("submit1")
        if arg == 's2' or arg == '2':
           cmds.append("submit2")
        if arg == 'p' or arg == 'pi':
           cmds.append(PR)
        if arg == 'so':
            so = 1
        if arg == 'io':
            io = 1
        if arg == 'db':
            DB = 1
        if arg == 'st' or arg == 'stat' or arg == 'stats':
            stats = 1
        if arg == 'p1' or arg == 'part1':
            cmds.append('p1')
        if arg == 'p2' or arg == 'part2':
            cmds.append('p2')
        

if __name__ == '__main__':
    get_args()
    
    if not io: run_samples(p1, p2, cmds)
    if not so: run(get_year(),  get_day(), p1, p2, cmds)
    if stats: print_stats()
    #manual()
