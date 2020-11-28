from fetch import fetch, fetchlines
from collections import Counter, defaultdict as dd
from heapq import heappush as push, heappop as pop
import sys

def movecar(y, x, dir, turn):
    dy, dx = carcoord[dir]
    if grid[y + dy][x + dx] == '+':
        if turn == 0:
            dir = leftturn[dir]
        elif turn == 2:
            dir = rightturn[dir]
        turn += 1
        turn %= 3

    if grid[y + dy][x + dx] == '\\':
        if dir == '>':
            dir = 'v'
        elif dir == '^':
            dir = '<'
        elif dir == 'v':
            dir = '>'
        elif dir == '<':
            dir = '^'

    if grid[y + dy][x + dx] == '/':
        if dir == '<':
            dir = 'v'
        elif dir == '^':
            dir = '>'
        elif dir == '>':
            dir = '^'
        elif dir == 'v':
            dir = '<'
    return y + dy, x + dx, dir, turn

cardirs = {'>': '-', '<':'-', 'v':'|', '^':'|'}

leftturn = {'>': '^', '^':'<', '<':'v', 'v':'>'}
rightturn = {'>': 'v', 'v':'<', '<':'^', '^':'>'}


carcoord = {'>': (0, 1), '<':(0, -1), 'v':(1, 0), '^':(-1, 0)}
fetch(13)
data = sys.stdin.readlines()
grid = [[] for _ in range(len(data))]
X = 0
Y = len(data)
carlocs = []
for d in (data):
    X = max(X, len(d) -1)

idx = 0
for y, d in enumerate(data):
    for x, ch in enumerate(d[0:-1]):
        if ch in cardirs:
            push(carlocs, (y, x, ch, 0, idx))
            idx+= 1
            grid[y].append(cardirs[ch])
        else:
            grid[y].append(ch)

def printgrid(carlocs):
    rows = []
    for y in range(Y):
        row = []
        for x in range(X):
            row.append(grid[y][x])
        rows.append(row)
    for y, x, dir, turn in carlocs:
        rows[y][x] = dir
    for row in rows:
        print(''.join(row))
    print('')
cnt = 0
currpos = dd(list)
for y, x, _, _, idx in carlocs:
    currpos[(y, x)] = [idx]

while True:
    tick = []
    cnt += 1
    oldpos = currpos
    currpos = dd(list)
    incolls = set()
    candidates = []
    print(cnt)
    for y, x, dir, turn, idx in carlocs:
        print('{} {} {} {}'.format(y, x, dir, grid[y][x]))
        ny, nx, ndir, nturn = movecar(y, x, dir, turn)
        currpos[(ny, nx)].append(idx)
        if len(currpos[(ny, nx)]) > 1:

            print('collision', nx, ny)
            for idy in currpos[(ny, nx)]:
                incolls.add(idy)
                print(idy)
        if len(oldpos[(ny, nx)]) > 0:
            incolls.add(idx)
            print('collision', nx, ny)
            for idy in oldpos[(ny, nx)]:
                incolls.add(idy)
                print(idy)

        candidates.append((ny, nx, ndir, nturn,idx))
        oldpos[(y, x)].remove(idx)
#    print(collisions)
#    print(candidates)
    for y, x, dir, turn, idx in candidates:
        if idx not in incolls:
            push(tick, (y, x, dir, turn, idx))
#    print(tick)
    carlocs = tick
    if len(carlocs) < 1:
        exit()
    if len(carlocs)==1:
        y, x, dir, turn, idx = carlocs[0]
        print(x, y)
        exit()
#    if cnt >= 456:
    print('Nbr of cars ', len(carlocs))
    assert len(carlocs)%2==1
#        print(carlocs)
#        printgrid(carlocs)
