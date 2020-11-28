from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
from fetch import fetch, fetchlines
import sys

def inrange(x, y, z, bots):
    cnt = 0
    for otherindex, (ox, oy, oz, r) in enumerate(bots):
        dist = abs(ox - x) + abs(oy - y) + abs(oz - z)
        if dist <= r:
            cnt+= 1
    return cnt


def inrangebot(index, bots):
    x, y, z, r= bots[index]
    cnt = 0
    for otherindex, (ox, oy, oz, _) in enumerate(bots):
        dist = abs(ox - x) + abs(oy - y) + abs(oz - z)
        if dist <= r:
            cnt+= 1
    return cnt

data = sys.stdin.readlines()
bots = []
strongest = 0
maxR = 0
for index, line in enumerate(data):
    linespl = line.strip().replace('pos=<', '').replace('>,', '').replace('r=', ',').split(',')
    x, y,z, r= map(int, linespl)
    bots.append((x, y,z, r))
    if r >maxR:
        maxR= r
        strongest = index


#res = inrangebot(strongest, bots)
#print(res)

#candidate points, all corners around the points, 6000
#for all points with maxcnt
# binsearch walk towards origo
cand_points = []
for bx, by, bz, br in bots:
    left = (bx - br, by, bz, 0)
    right = (bx + br, by, bz, 1)
    back = (bx, by - br, bz, 2)
    forw = (bx, by + br, bz, 3)
    down = (bx, by, bz - br, 4)
    up = (bx, by, bz + br, 5)
    cand_points.extend([left, right, up, down, forw, back])
cnt = [0 for _ in cand_points]
for index, (x, y, z,_) in enumerate(cand_points):
    pcnt = inrange(x, y, z, bots)
    cnt[index] = pcnt

best =[]
maxcnt= 0
for index in range(len(cnt)):
    if cnt[index] > maxcnt:
        best= [index]
        maxcnt = cnt[index]
    elif cnt[index] == maxcnt:
        best.append(index)

print('len best', len(best))
x, y, z, wdir = cand_points[best[0]]
manh = abs(x) + abs(y) + abs(z)
print(x, y,z, cnt[best[0]])
print(wdir)
print(manh)

# walk towards origo
walkdir = [(-1, 0, 0), (0, 0, -1), (0, -1, 0)]
dx, dy , dz = walkdir[0]
sx, sy, sz = x, y, z
temp_cnt = cnt[best[0]]
bestpos = cand_points[best[0]]
print('bestpos', bestpos)
best_cnt = cnt[best[0]]
for dx, dy, dz in walkdir:
    while temp_cnt >= best_cnt:
        sx, sy, sz = sx + dx, sy + dy, sz + dz
        temp_cnt = inrange(sx, sy, sz, bots)
       # print(temp_cnt)
        if temp_cnt >= best_cnt:
            print(temp_cnt)
            best_cnt = temp_cnt
            bestpos = (sx, sy, sz)
            print(bestpos)
    # undo 
    sx, sy, sz = sx - dx, sy - dy, sz - dz
    

manh = abs(bestpos[0]) + abs(bestpos[1]) + abs(bestpos[2])
print('bestmanh', manh)

# not 75073074
# not 56170242
# not 55335876
# not 74217707
# not 75184672