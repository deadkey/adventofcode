from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
import sys

def count(R, C, grid):
    cnt= dd(int)
    for r in range(max(0, R -1), min(len(grid), R + 2)):
        for c in range(max(0, C -1), min(len(grid[0]), C + 2)):
            if r != R or c != C:
                cnt[grid[r][c]] += 1
    return cnt

def printgrid(grid):
    for row in range (len(grid)):
        prow = []
        for col in range(len(grid[0])):
            prow.append(grid[row][col])
        print(''.join(prow))      
    print('')

data = sys.stdin.readlines()
wood = [[] for _ in range(len(data))]
nextgen = [[] for _ in range(len(data))]

for index, line in enumerate(data):
    for ch in line.strip():
        wood[index].append(ch)
        nextgen[index].append(ch)

#printgrid(wood)

#wood[2][5] = 'X'
def score(grid):

    cnt = dd(int)                               
    for r in range (len(wood)):
            for c in range(len(wood[0])):
                cnt[wood[r][c]] += 1
    wooded = cnt['|']
    yards = cnt['#']
    return (wooded * yards)  

scoring = [score(wood)]
for gen in range(1000):
    # copy
    
    for row in range (len(wood)):
        for col in range(len(wood[0])):
            nextgen[row][col] = wood[row][col]
    
    for r in range(len(wood)):
        for c in range(len(wood[0])):
            neigh = count(r, c, wood)
            #print(r, c, wood[r][c], neigh)
            if wood[r][c] == '.' and neigh['|']>= 3:
                #print('to wood')
                nextgen[r][c] = '|'
            elif wood[r][c] == '|' and neigh['#']>= 3:
                #print('to lumber')
                nextgen[r][c] = '#'
            elif wood[r][c] == '#':
                if neigh['#']>= 1 and neigh['|'] >= 1:
                    nextgen[r][c] = '#'
                 #   print('to lumber')
                else:
                    nextgen[r][c] = '.'
                 #   print('to open')
    
    for row in range (len(wood)):
        for col in range(len(wood[0])):
            wood[row][col] = nextgen[row][col]
    scoring.append(score(wood))

   # printgrid(wood)
print(scoring)
looprev = []
end = scoring[-1]
index = len(scoring) -2
while scoring[index] != end:
    looprev.append(scoring[index])
    index -= 1
    print(index)
looprev.append(end)   
loop = looprev[::-1]
print(loop)
print(len(loop))
print(scoring[1000])
turnsleft = (1000000000 - len(scoring) +1)
rest= turnsleft % len(loop)
print(loop[rest])