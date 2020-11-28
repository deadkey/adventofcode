from fetch import fetch, fetchlines
from collections import Counter
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
import sys

def getpath(xstart, ystart, target):
    visited = set()
    targets = []
    visited.add((xstart, ystart))
    q =[(xstart, ystart)]
    parents = {}
    found = False
    while q and not found:
        q2 = []
        for x, y in q:
            if (x, y) == target:
                found = True
            cand = [(-1, 0), (0, -1) , (0, 1), (1, 0)]
            for dx, dy in cand:
                if battlefield[x + dx][y + dy] == '.':

                    if (x + dx, y + dy) not in visited:
                        parents[((x + dx, y + dy))] = (x, y)
                        visited.add((x + dx, y + dy))
                        q2.append((x + dx, y + dy))




        q = q2
    x, y = parents[target]
    path = [target]
    while (x,y) != (xstart, ystart):
        path.append((x, y))
        x, y = parents[(x, y)]
    return path[::-1]


def bfs(x, y, enemy):
    visited = set()
    targets = []
    visited.add((x,y))
    q =[(x,y)]
    targetdist = 10 ** 12
    cnt = 1
    while q:
        q2 = []
        for x, y in q:
            cand = [(-1, 0), (0, -1) , (0, 1), (1, 0)]
            for dx, dy in cand:
                if battlefield[x + dx][y + dy] == '.':

                    if (x + dx, y + dy) not in visited:
                        visited.add((x + dx, y + dy))
                        q2.append((x + dx, y + dy))
                elif battlefield[x + dx][y + dy] == enemy and cnt <= targetdist :
                    targets.append((x, y))
                    targetdist = cnt


        q = q2
        cnt += 1
    if len(targets) > 0:
        #we're done!
        closest = targets[0]
        for tr, tc in targets:
            if readingorder[(tr, tc)] < readingorder[closest]:
                closest = (tr, tc)
        return closest
    return -1, -1

data = sys.stdin.readlines()

readingorder = {}
battlefield = []
ordering = []
coordtoid = {}
goblins = 0
elfs = 0
elves= []
cnt = 0
idx = 0

def printfield():
    for row in range(len(battlefield)):
        line = []
        for col in range(len(battlefield[0])):
             line.append(battlefield[row][col])
        print(''.join(line))
    print('')


INF = 10** 12

def calcdist(row, col, target, dists,visited):
    visited.add((row, col))
    if target == (row, col):
        dists[row][col] = 0
    #    print('target!!!!')
        return 0
    if dists[row][col] < INF:
        dists[row][col] = 0
        return dists[row][col]

    cand = [(-1, 0), (0, -1) , (0, 1), (1, 0)]
    best = INF

    for dx, dy in cand:
        if battlefield[row + dx][col + dy] == '.' and (row + dx, col + dy) not in visited:
            alt = calcdist(row + dx, col + dy, target, dists, visited)
            best = min(best, alt + 1)
    #        print('alt', alt)

    dists[row][col] = best
    return best


def move(row, col, target):
    cand = [(-1, 0), (0, -1) , (0, 1), (1, 0)]
    best = 10 ** 12
    bestcand =(0, 0)
    visited = set()
    path_to_target = getpath(row, col, target)
    return path_to_target[0]

def can_attack(row, col, enemy):
    cand = [(-1, 0), (0, -1) , (0, 1), (1, 0)]
    enemies= []
    for dir in cand:
        if battlefield[row + dir[0]][col + dir[1]] == enemy:
            en = (row + dir[0], col + dir[1])
            values = (hp[coordtoid[en]], readingorder[en],  en[0], en[1])

            push(enemies, values)
    if len(enemies) > 0:
        return True, enemies[0][2], enemies[0][3]
    return False, 0, 0


def attack(attacker, defender,enemy):
    global elfs, goblins
    hp[defender] -= power[attacker]
    if hp[defender] <= 0:
        hp[defender] = 0
        if enemy == 'E':
            elfs -= 1
        else:
            goblins -= 1
        return True
    return False

def reset(data):
    global ordering,power, battlefield, idx, readingorder, coordtoid, goblins, elves, elfs
    readingorder = {}
    battlefield = []
    ordering = []
    coordtoid = {}
    goblins = 0
    elfs = 0
    elves= []
    cnt = 0
    idx = 0

    for row, line in enumerate(data):
        battlefield.append([])
        for col, ch in enumerate(line.strip()):
            readingorder[(row, col)] = cnt
            battlefield[row].append(ch)
            if ch == 'E':
                elfs += 1
                elves.append(idx)
            if ch == 'G':
                goblins += 1

            if ch == 'E' or ch == 'G':
                push(ordering, (cnt, ch, row, col, idx))
                coordtoid[(row, col)] = idx
                idx += 1

            cnt += 1
    power = [3 for _ in range(idx)]



def testfight(tp):
    fighting = True
    global idx, hp, power, ordering, battlefield, elves

    hp = [200 for _ in range(idx)]
    #print('idx', idx)
    for el in elves:
        power[el] = tp
    cnt = 0
    #printfield()
    while fighting:
        norder = []
        cnt += 1

        fighting = False
        while len(ordering):
            _, ch, row, col, idx = pop(ordering)
            if hp[idx] > 0:
                if elfs <= 0 or goblins <= 0:
                    fighting = False

                    break

                can, ar, ac = can_attack(row, col, 'E' if ch == 'G' else 'G')
                if can:
                    died = attack(idx, coordtoid[(ar, ac)], 'E' if ch == 'G' else 'G')
                #    print('attack ', row, col, died)
                    if died:
                        coordtoid[(ar, ac)] = -1
                        battlefield[ar][ac] = '.'
                        lastround = cnt
                        if ch == 'G':
                            return False, 0

                    push(norder, (readingorder[(row, col)], ch, row, col, idx))

                    fighting = True
                else:
                    closest = bfs(row, col, 'E' if ch == 'G' else 'G')
                    if closest[0] == -1:
                        push(norder, (readingorder[(row, col)], ch, row, col, idx))
                        continue
                    else:

                    #    print('closest to {} {} is {}'.format(row, col, closest))
                        r, c = move(row, col, closest)
                    #    print('moved to ', r, c)
                        coordtoid[(row, col)] = -1
                        battlefield[row][col] = '.'
                        battlefield[r][c] = ch
                        coordtoid[(r, c)] = idx

                        fighting = True
                        can, ar, ac = can_attack(r, c, 'E' if ch == 'G' else 'G')
                        if can:
                            died = attack(idx, coordtoid[(ar, ac)], 'E' if ch == 'G' else 'G')
                #            print('attack ', r, c, died)
                            if died:
                                coordtoid[(ar, ac)] = -1
                                battlefield[ar][ac] = '.'


                        push(norder, (readingorder[(r, c)], ch, r, c, idx))
        ordering = norder
        #print(ordering)
        #if cnt > 5:
        #    fighting = False
        #printfield()
        #print(hp)

    full = cnt - 1
    rem = sum(hp)
    #print(hp)
    #print('full ', full)

    #print('rem ', rem)
    #print('score ', full * rem)
    return True, full * rem


someDied = 3
allLived = 3
livingScore = 0
#reset(data)
print(testfight(3))

exit()
for i in range(20):
    mid = (someDied + allLived)//2
    print('testpower ', mid)
    reset(data)
    res, score = testfight(mid)
    if res:
        # lived!
        allLived = mid
        livingScore = score
    else:
        someDied = mid

print(allLived, livingScore)
