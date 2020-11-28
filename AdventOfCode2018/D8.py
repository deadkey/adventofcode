from fetch import fetch, fetchlines
from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
import sys

cnt = 0

def next(data, cnt):
    curr = int(data[cnt])
    cnt += 1
    return curr, cnt

def read(data, cnt, metas, children):
    index = cnt
    nbrOfNodes, cnt = next(data, cnt)
    nbrOfMeta, cnt = next(data, cnt)
    children[index] = nbrOfNodes
    s = 0
    score = []
    for inner in range(nbrOfNodes):
        cnt, subscore = read(data, cnt, metas, children)
        score.append(subscore)
    for meta in range(nbrOfMeta):
        m,cnt = next(data, cnt)
        metas[index].append(m)
    if nbrOfNodes == 0:
    #    print(index, sum(metas[index]))
        return cnt, sum(metas[index])
    for entry in metas[index]:
        if entry <= nbrOfNodes:
            s += score[entry - 1]
    #print(index, s)

    return cnt, s

metas = dd(list)
children = dd(list)
data = sys.stdin.read().split()
cnt, s = read(data, cnt, metas, children)

#print(metas)
#print(scores)
print(s)
