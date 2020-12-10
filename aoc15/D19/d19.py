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

def solve(L, seen, reac, mx, BEST):
    if BEST == 0: return 0
    if L in seen:
        return seen[L]
    best = BEST
    
    for i in range(len(L)):
        for k in range(2, mx+1):
            testkey = L[i:i+ k]
            if testkey in reac:
                for alt in reac[testkey]:
                    st = L[0:i] + alt + L[i + k:]
                    best = min(best, 1+ solve(st, seen, reac, mx, best-1))
    
    seen[L] = best
    if len(seen) % 10000 == 0: print(len(seen), len(L))
    
    return best

def bfs(LL, reac, mx):
    q = [LL]
    seen = set(q)
    cnt = 0
    while q:
        q2 = []
        for L in q:
            if L == 'e': return cnt
            for i in range(len(L)):
                for k in range(2, mx+1):
                    testkey = L[i:i+ k]
                    if testkey in reac:
                        for alt in reac[testkey]:
                            st = L[0:i] + alt + L[i + k:]
                            if st not in seen:
                                seen.add(st)
                                q2.append(st)
        q = q2
        cnt += 1
        db(cnt)

def elems(s):
    els = []
    curr = []
    for ch in s:
        if ch.islower():
            curr.append(ch)
            if len(curr) > 0: els.append(''.join(curr))
            curr = []
        else:
            if len(curr) > 0: els.append(''.join(curr))
            curr = [ch]
    if len(curr) > 0: els.append(''.join(curr))     
    return els          

def p2(v):
    forbStart = {'Rn', 'F', 'Ar', 'Y', 'Mg', 'Al'}
    forbEnd = {'Rn', 'F', 'Y', 'C', 'N'}
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    vals = [parse(line) for line in lines]
    reac = defaultdict(list)
    mx = 0
    total = []
    start = set()
    end = set()
    for l, r in vals:
        el = elems(r)
        
        start.add(el[0])
        total.extend(el)
        end.add(el[-1])
        reac[r].append(l)
        mx = max(len(r), mx)
    cntR = Counter(total)
    print(start, end)
    print(set(cntR.keys()) - start)
    print(set(cntR.keys()) - end)
    
    print(len(cntR), len(start), len(end))
    db(cntR)
    test = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
    el = elems(test)
    cntEl = Counter(el)

    #test = ['HOH', 'HOHOHO','H2O' ]
    #test = 'HOH'
    seen = {}
    exit()
    return bfs(test, reac, mx)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,19, p1, p2, cmds)
if stats: print_stats()
#manual()
