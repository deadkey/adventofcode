from fetch import fetch, fetchlines
from collections import Counter, defaultdict as dd
from heapq import heappush as push, heappop as pop
import sys

def digits(s):
    d = []
    while s > 9:
        d.append(s % 10)
        s = s //10
    d.append(s)
    return d[::-1]

def check():
    if next[(-len(my) -1):-1] == myl:
        return len(next) - len(my) - 1
    if next[-len(my):] == myl:
        return len(next) - len(my)
    return -1


my = '190221'
myl = [int(ch) for ch in my]
du = 9
elf1 = 3
elf2 = 7
next = [3, 7]
i1 = 0
i2 = 1
cnt = 0
while True:
    cnt += 1
    ssum = elf1 + elf2
    digs = digits(ssum)
    next.extend(digs)
    i1 = (i1 + 1 + elf1)% len(next)
    i2 = (i2 + 1 + elf2)% len(next)
    elf1 =next[i1]
    elf2 =next[i2]
    ind = check()
    if ind > -1:
        print(ind)
        exit()
#print(next)
