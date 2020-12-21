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


def gen(node, rules, leaves):
    ways = set()
    if node in leaves:
        return set([leaves[node]])
    
    #db(node, rules[node])
    for alt in rules[node]:
        found = set([''])
        #db(alt)
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
    #db(rules)
    ways = gen(0, rules, leaves)
    #db('WAYS', ways)
    cnt = 0
    for m in msg:
        if m in ways: cnt += 1

    return cnt

def check(matches, m, fr):
    for match in matches: break
    L = len(match)
    steps = 0
    for s in range(fr, len(m), L):
        sub = m[s:s+L]
        if sub not in matches:
            return steps, s
        steps += 1
    return steps, len(m)

def p2(v):
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
    ways = gen(42, rules, leaves)

    ways2 = gen(31, rules, leaves)
    #db('WAYS 42', ways)
    #db('WAYS 31', ways2)
            
    
    cnt = 0
    for m in msg:

        c42, end = check(ways, m, 0)
        db('c42 ', c42, ' end ', end)
        if c42 > 0:

            for match in ways: break
            L = len(match)

            for i in range(2, c42+1):    
                fr = i * L 
                c31, end2 = check(ways2, m, fr)
                db(c31, fr, end2)
                if c31 > 0 and c31 < i and end2 == len(m):
                    cnt += 1
                    break
                
    return cnt


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,19, p1, p2, cmds)
if stats: print_stats()
#manual()
