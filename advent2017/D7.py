import sys
lines = sys.stdin.readlines()
#parents = dict()

progs = dict()
c = set()
g = dict()
weights = dict()
for line in lines:
    data = line.split('->')
    prog = data[0].split()
    name = prog[0]
    w = int(prog[1][1:-1])
    g[name] = list()
    progs[name] = w
    if len(data) > 1:
        children = data[1].strip().split(', ')
        c.update(children)
        g[name] = children

for prog in progs:
    if prog not in c:
        break
print(prog)

root = prog

def balance(r):
    w = progs[r]
    wc = list()
    wc_sum = 0
    for ch in g[r]:
        balance(ch)
        wc.append(weights[ch])
    if len(wc)> 0:
        wc_sum = sum(wc)
        val = wc[0]
        bal = True
        for i, v in enumerate(wc):
            if v != val:
                # too high

                print('Found unbalanced ', r)
                print('nbr of children ', wc)
        


    weights[r] = w + wc_sum
    #if all the same, add to w
    # if 2 ch?
balance(root)
