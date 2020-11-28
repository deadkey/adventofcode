from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
from fetch import fetch, fetchlines
import sys
from z3 import *

def inrange(x, y, z, bots):
    cnt = 0
    for otherindex, (ox, oy, oz, r) in enumerate(bots):
        dist = abs(ox - x) + abs(oy - y) + abs(oz - z)
        if dist <= r:
            cnt+= 1
    return cnt


data = sys.stdin.readlines()
bots = []
maxx, minx, maxy, miny, maxz, minz = 0, 0, 0, 0, 0, 0
for index, line in enumerate(data):
    linespl = line.strip().replace('pos=<', '').replace('>,', '').replace('r=', ',').split(',')
    x, y,z, r= map(int, linespl)
    bots.append((x, y,z, r))
    minx= min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    minz = min(minz, z)
    maxy =max(maxy, y)
    maxz=max(maxz, z)

def my_abs(v):
    return If(v >= 0, v, -v)

x, y, z = Int('x'), Int('y'), Int('z')
bounds = [And(minx <= x, x <= maxx), And(miny <= y, y <= maxy), And(minz <= z, z <= maxz)]
opt = Optimize()
#in_ranges = [Int('in_range_' + str(i)) for i in lenr(bots)]
bot_constr = []
for i, (bx, by, bz, br) in enumerate(bots):
    b = Int('bot_{}'.format(i))
    opt.add(b == If(my_abs(x - bx) + my_abs(y - by) +  my_abs(z - bz) <= br, 1, 0))
    bot_constr.append(b)
    
bot_cnt = Int('sum')
opt.add(bot_cnt == sum(bot_constr))
dist_orig = Int('dist')
opt.add(dist_orig == my_abs(x) + my_abs(y) + my_abs(z))

h1 = opt.maximize(bot_cnt)
h2 = opt.minimize(dist_orig)
opt.check()
print ("b", opt.lower(h2), opt.lower(h1))



# not 75073074
# not 56170242
# not 55335876
# not 74217707
# not 75184672