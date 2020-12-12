import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    l, r = line.split(' => ')
    return l, r

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    vals = [parse(line) for line in lines]
    reac = defaultdict(list)
    for l, r in vals:
        reac[l].append(r)
    
    test = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
    #test = ['HOH', 'HOHOHO','H2O' ]
    #test = 'HOHOHO'
    res = set()
    for key in reac.keys():
        
        matches = re.finditer(key, test)
        for m in matches:
            s = m.start()
            e = m.end()
            for alt in reac[key]:
                st = test[0:s] + alt + test[e:]
                res.add(st)

            
    return len(res)

def solve(L, cas, reac, seen, BEST):
    if BEST <= 0 or L == 'e':
        return 0
    if L in seen:
        return seen[L]
    '''    
    for ca in cas:
        if ca in L:
            
            oldL = len(L)
            nxtL = L.replace(ca, cas[ca])
            newL = len(nxtL)
            k = (oldL - newL)//2
            
            res =  k + solve(nxtL, cas, reac,seen,  BEST - k)
            BEST = min(res, BEST)
            seen[L] = res
            return res
    '''
    for r, l in reac:
        if r in L:
             
            k = L.count(r)
            nxtL = L.replace(r, l)
            
            
            res =  k + solve(nxtL, cas, reac, seen, BEST - k)
            return res
            #BEST = min(res, BEST)
    #seen[L] = BEST

    return BEST

def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    vals = [parse(line) for line in lines]
    reac = []
    #mx = 0
    cas = {}
    for l, r in vals:
        #el = elems(r)
        reac.append((r, l))
        if 'Ca' in r:
            cas[r] = l
    reac.sort(reverse = True, key = lambda x: len(x[0]) - len(x[1]))
    seen = {}
    test = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
    return solve(test, cas, reac, seen, 10**10)
    

def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,19, p1, p2, cmds)
if stats: print_stats()
#manual()
