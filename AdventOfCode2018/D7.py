from fetch import fetch, fetchlines
from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop


import sys

# dep, is parent count, g = parents
def topsort(nodes, dep,g):
    li = []
    q = []
    for node in nodes:
        push(q, (dep[node], node))
    while q:
        p, f = pop(q)
        if p == 0:
            li.append(f)
            for d in g[f]:
                dep[d] -= 1
                push(q, (dep[d], d))
    return li

data  = sys.stdin.readlines()
nodes = set()
parentcnt = Counter()
parentcnt2 = Counter()

g = dd(list)
parents = dd(list)


for line in data:
    d=line.split()
    nodes.add(d[1])
    nodes.add(d[7])
    parentcnt[d[7]] += 1

    parentcnt2[d[7]] += 1
    g[d[1]].append(d[7])
    parents[d[7]].append(d[1])
#print(nodes)
#print(parentcnt)
#print(parents)
li = topsort(nodes, parentcnt, g)
print('Order ' + ''.join(li))
#print(parents)
time = 0
av = []
for task in nodes:
    if len(parents[task]) == 0:
        push(av, (0,task))

#print(av)
active = []
limit = 5
order = []
finished = set()
ina = set()
while av or active:
    print(av)
    if len(active) < limit and len(av) > 0 and av[0][0] <= time:
        _, next = pop(av)
        print(next, time)
        fintime = time + (ord(next) - ord('A') + 1) + 60
        push(active, (fintime ,next))


    else:
        fintime, th = pop(active)
        print('completed', th, fintime)
        if th not in ina:
            order.append(th)
            ina.add(th)

            for c in g[th]:
                parentcnt2[c] -= 1
                if parentcnt2[c] == 0:
                    push(av, (fintime, c))
        if th not in finished:
            time = fintime
        finished.add(th)


print(''.join(order))
print(time)
