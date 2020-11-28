from fetch import fetch, fetchlines
from collections import Counter, defaultdict as dd
import sys


size = 3

def power(x, y, serial):
    x = x + 1
    y = y + 1
    rackid = x + 10
    pl= rackid * y
    pl += serial
    pl *= rackid
    pl = (pl//100) % 10
    pl -= 5

    return pl

def runtest():
    serial = 18

    grid = calcpower(serial)

    return findmax(grid)


def run():
    serial = 1788
    grid = calcpower(serial)


    return findmax(grid)


grid = [[0] * 300 for _ in range(300)]
def calcpower(serial):
    for x in range(300):
        for y in range(300):
            grid[x][y] = power(x, y, serial)
    return grid

def getpower(grid, x, y):
    p = 0
    for dx in range(size):
        for dy in range(size):
            p += grid[x + dx][y +dy]
    return p

def findmax(grid):
    maxp = -10* 12
    maxx, maxy = 0, 0
    for startx in range(300-size + 1):
        for starty in range(300-size +1):
            alt =getpower(grid, startx, starty)
            if alt > maxp:
                maxp = alt
                maxx, maxy =startx+1, starty + 1
    return maxx, maxy, maxp

maxp = - 10 ** 12
rx, ry, sz = 0, 0, 0
calcpower(1788)
for s in range(1, 4):
    size = s
    x, y, p = findmax(grid)
    if p > maxp:
        maxp = p
        rx, ry = x, y
        sz = s
    print(s)
print(rx, ry, sz)
#print(run())
#data  = sys.stdin.readlines()
