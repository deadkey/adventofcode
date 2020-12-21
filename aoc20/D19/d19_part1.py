import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *

from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parserule(line):
    line = removeall(line, '"')
    ruleno, rest = line.split(':')
    ruleno = int(ruleno)
    alts = rest.split('|')
    altli = []
    for alt in alts:
        il = lazy_ints(alt.split())
        if isint(il):
            il = [il]
        altli.append(il)
    
    return ruleno, altli

#returns order so that edges only point forward in partial order
def topsort(g):
    ps=[0] * len(g)
    for ns in g:
        for n in ns:
            ps[n] += 1
    q =[i for i,v in enumerate(ps) if v == 0]
    order = []
    while q:
        q2 = []
        for n in q:
            order.append(n)
            for p in g[n]:
                ps[p] -=1
                if ps[p] == 0:
                    q2.append(p)
        q =q2
    return order

def getmatches(li, rules):
    matches = []
    for ruleno, alts in rules:
        for alt in alts:
            L = len(alt)
            if len(li) < L:
                continue
            if alt == li[0:L]:
                matches.append((ruleno, L))
    return matches

def onelevel(s, rules):
    #this is one level

    poss = s
    changed = True
    db(poss)
    while changed:
        poss2 = []
        changed = False
        
        for li in poss:
            db(poss, li)
            used, p, ind = li
            rest = p[ind:]
            matches = getmatches(rest, rules)
            for no, endind in matches:
                used.append(no)
                newind = ind + endind
                poss2.append((used, p, newind))
                changed = True

        poss = poss2

    valid = []
    for used, p, newind in poss2:
        if newind == len(m) -1:
            valid.append(([], used, 0))
    return valid
    

def check(m,leaves,  order, rules):
    pos = 0
    used = []
    for ch in m:
        leave = leaves[ch]
        used.append(leave)
    valid = [([], used, 0)]
    changed = True
    while changed:
        changed = False
        valid = onelevel(valid, rules)
        if len(valid) > 0:
            changed = True
            for _, p, ind in valid:
                if p[0] == 0:
                    return True
    return False 
        

def gen(node, rules, leaves):
    ways = set()
    if node in leaves:
        return set([leaves[node]])
    
    db(node, rules[node])
    for alt in rules[node]:
        found = set([''])
        db(alt)
        for d in alt:
            nf = set()
            pos = gen(d, rules, leaves)
            for f in found:
                for p in pos:
                    s = f + p
                    nf.add(s)
            found = nf
        ways |= found

    return ways

def p1(v):
    lines = v.strip().split('\n')
    rules = {}
    leaves = {}
    for line in lines:
        if ':' in line:
            #rules.append(parserule(line))
            ruleno, altli = parserule(line)
            rules[ruleno] = altli
            if "a" in line or 'b' in line:
                leaves[ruleno] = altli[0]
                
    msg = []
    for line in lines:
        if not ':' in line and len(line) > 0:
            msg.append(line)
    #db(leaves)
    N = len(rules)
    '''
    g = [[] for _ in range(N)]
    for i, alt in rules:
        #db(rules)
        for li in alt:
            
            for d in li:
                if isint(d):
                    g[d].append(i)
    order = topsort(g)
    '''
    #db(order)
    db(rules)
    ways = gen(0, rules, leaves)
    #db('WAYS', ways)
    cnt = 0
    for m in msg:
        if m in ways: cnt += 1

    return cnt

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,19, p1, p2, cmds)
if stats: print_stats()
#manual()
