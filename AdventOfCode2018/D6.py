from fetch import fetch, fetchlines
from collections import Counter
import sys

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


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

#for d in data:
for d in range(6):

#    x,y = map(int, d.split(','))
    x,y = map(int, input().split(','))

    points.append((x,y))
    minX=  min(minX, x)
    maxX=  max(maxX, x)
    minY=  min(minY, y)
    maxY=  max(maxY, y)
#print(minX, minY,maxX, maxY)

locs = {}
cnt = Counter()

for xl in range(minX -1, maxX+2):
    for yl in range(minY -1, maxY +2):
#area = Counter()
        mindist = INF
        closestpoint = -1
        mult = []
        for index, p in enumerate(points):
            alt = man(p[0], p[1], xl, yl)
            if alt < mindist:
                mindist = alt
                closestpoint = index
                mult=[]
                mult.append(closestpoint)
            elif alt == mindist:
                mult.append(index)
        #if len(mult) > 1:
        #    print('Ties', xl, yl)
        if len(mult) == 1:
            locs[xl, yl] = closestpoint
            cnt[closestpoint] += 1
border = []
for x in range(minX -1, maxX+2):
    border.append(locs[x][minY -1])
    border.append(locs[x][maxY + 1])
for y in range(minY -1, maxY+2):
    border.append(locs[minX -1][y])
    border.append(locs[maxX +1][y])


#hull = convex_hull(points)
hasInf = set(border)
#for p in hull:
#    i = pointstoindex[p]
for index, p in enumerate(points):
    x = p[0]
    y = p[1]
    if x== minX or x == maxX or y == minY or y == maxY:
        hasInf.add(index)
maxArea=  -1
hasMax= -1
#{2, 5, 38, 9, 43, 45, 14, 47, 19, 24, 26, 31}
#{5, 38, 9, 47, 26}

cnt2 = Counter()
testmax = 0
testval = -1
# for yl in range(minY, maxY +1):
# #    s = ''
#     for xl in range(minX, maxX+1):
#         if locs[xl][yl] >-1:
#
#             cnt2[locs[xl][yl]] += 1
#             if testmax < cnt2[locs[xl][yl]]:
#                 testval = locs[xl][yl]
#             testmax  = max(cnt2[locs[xl][yl]],  testmax)


    #        s += ('.')

#
print(hasInf)
#print(cnt)
for c in cnt:
    if cnt[c] > maxArea and c not in hasInf:
        maxArea = cnt[c]
        hasMax= index
print(maxArea)
