from collections import defaultdict as dd
from fetch import fetch, fetchlines
import sys

data = sys.stdin.readlines()#fetchlines(4)
prep = []

print(len(data))
for d in data:
    datum = d[:19]
    datum = datum.replace('[', '')
    datum = datum.replace(']', '')
    day = datum.split()
    minute = int(day[1].split(':')[1])
#    print(datum)
#    print(day[0])
#    print(minute)
    log = d[19:]

#    print(log)
    prep.append((day[0], minute, log))
#print(events)
prep.sort()
events= []
cnt = {}
curr= 0
mode = 1
for date, minute, log in prep:
    if 'Guard' in log:
        gg = log.split()
        gid= int(gg[1][1:])
        curr = gid
        mode = 1
    if 'falls' in log:
        mode = 0
    if 'wakes' in log:
        mode = 1

    events.append((date, minute, curr, mode))
cntsleep = dd(int)

#print(events)
lastmin = 0
curr = -1
guardtot = 0
currmode = 1
guards = set()
for date, minute, guard, mode in events:
    #print(date, minute, guard, mode)

    if curr != guard:
        guards.add(guard)
        if curr != -1:
    #        print('minute', minute, 'lastmin', lastmin)
            if currmode == 0:
                guardtot += max(0, (minute - lastmin)%60)

        #    print('added to ', curr, guardtot)
            cntsleep[curr] += guardtot
        guardtot = 0
        curr = guard
        lastmin = minute
    else:
        if currmode == 1 and mode == 0:
            # wakesup
            lastmin = minute
        else:
            if currmode == 0 and mode == 1:
                # falls asleep
        #        print('minute', minute, 'lastmin', lastmin)
                guardtot += max(0, (minute - lastmin)%60)
                lastmin = minute
    currmode = mode
#    print('total', guardtot, 'lastmin', lastmin)
if mode == 1:
    guardtot += max(0, minute - lastmin)

#    print('lastly to ', curr, guardtot)
    cntsleep[curr] += guardtot
mostsleep = -1
most = 0
#print(cntsleep)
for g in guards:
    if cntsleep[g] > most:
        most = cntsleep[g]
        mostsleep = g
#print(mostsleep)
#print(most)

def findworst(g):
    currmode = 1
    lastmin = 0

    minutes = dd(int)
    for date, minute, guard, mode in events:
        if guard == g:
        #    print('minute', minute, 'lastmin', lastmin)
            if mode == 1 and currmode == 0:
                for m in range(lastmin, minute):
                    minutes[m] += 1

            #        print('sleeping at ', m)
            if mode == 1:
                lastmin = minute
            currmode= mode
            lastmin = minute
    worstmin = 0
    cntmin = 0
    #print(minutes)
    for m, c in minutes.items():
        if c > cntmin:
            worstmin = m
            cntmin = c
    return worstmin, cntmin
#print(worstmin)
#print(cntmin)
mostmins = 0
theguard= 0
themin = 0
for guard in guards:

    worstmin, cntmin = findworst(guard)
    #print('guard',guard, worstmin, cntmin)
    if cntmin > mostmins:
        mostmins = cntmin
        theguard = guard
        themin = worstmin
#print(mostmins)
#print(theguard)
#print(themin)
print(themin*theguard)
