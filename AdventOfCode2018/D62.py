from fetch import fetch, fetchlines
from collections import Counter
import sys


def man(x, y, a, b):
    return abs(x - a) + abs(y - b)

INF = 10**12
data= fetchlines(6)

minX = INF
minY = INF
maxY =-INF
maxX = -INF
points = []

limit = 10000

for d in data:
#for d in range(6):

    x,y = map(int, d.split(','))
#    x,y = map(int, input().split(','))

    points.append((x,y))
    minX=  min(minX, x)
    maxX=  max(maxX, x)
    minY=  min(minY, y)
    maxY=  max(maxY, y)
#print(minX, minY,maxX, maxY)

cnt = Counter()
region = 0
for xl in range(minX - 200, maxX+ 202):
    for yl in range(minY -200, maxY + 202):
        totdist = 0
        for index, p in enumerate(points):
            alt = man(p[0], p[1], xl, yl)
            totdist += alt
        #if len(mult) > 1:
        #    print('Ties', xl, yl)
        if totdist < limit:
            region += 1
print(region)
