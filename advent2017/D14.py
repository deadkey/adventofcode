from D10B import knothash
from collections import deque

test = 'flqrgnkx'
key = 'jzgqcdpd'
def hextobin(h):
    if h.isdigit():
        b = bin(int(h))[2:]
    else:
        dec = ord(h) - ord('a') + 10
        b=  bin(dec)[2:]
    return '0' * (4 - len(b)) + b
def torow(s):
    grid = []
    for c in s:
        r = hextobin(c)
        grid.append(r)
    return ''.join(grid)


rows = []
for i in range(128):
    tmp_key = key + '-' + str(i)
    hashcode = knothash(tmp_key)
    rows.append(torow(hashcode))


ones = ''.join(rows).replace('0', '')
print(len(ones))
# build graph!
# run bfs
def addNeighbours(graph, i, j, rows):

    node = 'i' + str(i) + 'j' + str(j)
    graph[node] = []
    coords = [(i, j -1), (i, j +1), (i -1, j), (i +1, j)]
    for x, y in coords:
        if 0<= x < 128 and 0<= y < 128 and rows[x][y] == '1':
            node2 = 'i' + str(x) + 'j' + str(y)
            #print('added neighbor!')
            graph[node].append(node2)

graph = {}
for i in range(128):
    for j in range(len(rows[i])):
        if rows[i][j] == '1':
            addNeighbours(graph, i, j, rows)

def dfs(unvisited, startnode, graph):
    q = deque()
    q.append(startnode)
    while len(q) > 0:
        node = q.pop()
        for neighbor in graph[node]:
            if neighbor in unvisited:
                unvisited.remove(neighbor)
                q.append(neighbor)


unvisited = set([n for n in graph])
regions = 0
while len(unvisited) > 0:
    startnode = unvisited.pop()
    dfs(unvisited, startnode, graph)
    regions += 1
print('regions', regions)
