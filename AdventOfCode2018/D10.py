from fetch import fetch, fetchlines
from collections import Counter, defaultdict as dd
import sys

def checkWidth(points):
    startX = INF
    startY = INF
    endX =  -INF
    endY = - INF
    for x, y in points:
        startX = min(startX, x)
        startY = min(startY, y)
        endX = max(endX, x)
        endY = max(endY, y)
    return endX - startX, endY - startY

INF = 10 **8
def draw(points):
    startX = INF
    startY = INF
    endX =  -INF
    endY = - INF
    for x, y in points:
        startX = min(startX, x)
        startY = min(startY, y)
        endX = max(endX, x)
        endY = max(endY, y)
    for ty in range(startY, endY + 1):
        row = []
        for tx in range(startX, endX + 1):
            if len(points[(tx,ty)]) > 0:
                row.append('#')
            else:
                row.append('.')


        print(''.join(row))
    print('')

def update(points):
    newp= dd(list)
    for x, y in points:
        for vx, vy in points[(x, y)]:
            nx = x + vx
            ny = y + vy
            newp[(nx, ny)].append((vx, vy))
    return newp

points = dd(list)

for line in data:
    line = line.replace('position=<', '')
    line = line.replace('> velocity=<', ' ')
    line = line.replace('>', '')
    line = line.replace(',', ' ')
    x, y, vx, vy = map(int, line.split())
    points[(x, y)].append((vx, vy))
#print(points)
#draw(points)
wx, wy = checkWidth(points)
i = 0
prevpoints= points
#exit()
while True:
    #draw(points)
    prevpoints = points
    points = update(points)

    wtx, wty = checkWidth(points)
    if wtx <= wx or wty <= wy:
        wx = min(wtx, wx)
        wy = min(wty, wy)
    else:
        break
    i+= 1

#draw(points)
draw(prevpoints)
print(i)
