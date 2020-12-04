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

def get_day(): return 7 #date.today().day
def get_year(): return 2016 #date.today().year
def db(a):
    if DB: print(a)

def check(chunk):
    
    for s in range(0, len(chunk)-3):
        chars = chunk[s:s+4]
        no = set(chars)
        if len(no) == 2 and chars[0] == chars[3] and chars[1] == chars[2]:
            return True
    return False

def p1(v):
    lines = v.strip().split('\n')
    tot = 0
    for line in lines:
        chunks = [[]]
        inside = [[]]
        cnt = 0
        for ch in line:
            if ch == '[':
                inside.append([])
                
                cnt += 1
            elif ch == ']':
                cnt -= 1
                if cnt == 0:
                    chunks.append([])
            elif cnt == 0:
                chunks[-1].append(ch)
            else:
                inside[-1].append(ch)
        ok = False
        for chunk in chunks:
            if check(chunk):
                ok = True
        notok = False
        for chunk in inside:
            if check(chunk):
                notok = True
        
        if ok and not notok:
            tot += 1
                

    return tot


def check2(chunk):
    abas = set()
    for s in range(0, len(chunk)-2):
        chars = chunk[s:s+3]
        no = set(chars)
        if len(no) == 2 and chars[0] == chars[2]:
            abas.add(''.join(chars))
    return abas

def verify(aba, bab):

    for a in aba:
        b = a[1] + a[0] + a[1]
        if b in bab:
            return True
    return False

def p2(v):
    lines = v.strip().split('\n')
    tot = 0
    for line in lines:
        chunks = [[]]
        inside = [[]]
        cnt = 0
        for ch in line:
            if ch == '[':
                inside.append([])
                
                cnt += 1
            elif ch == ']':
                cnt -= 1
                if cnt == 0:
                    chunks.append([])
            elif cnt == 0:
                chunks[-1].append(ch)
            else:
                inside[-1].append(ch)
        aba = set()
        for chunk in chunks:
            aba |= (check2(chunk))
        bab = set()        
        for chunk in inside:
            bab |= (check2(chunk))
        if verify(aba, bab): tot += 1 

    return tot


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
