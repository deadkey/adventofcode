import math
val = 312051
tests = [i for i in range(1, 25)]#[1, 12, 10, 23, 1024]
res = [0, 3, 3, 2, 31]

def dist(n):
    minSide = math.floor(math.sqrt(n))
    if minSide % 2 == 0:
        minSide -= 1
    index = n - minSide**2
    myside = minSide + 1
    #print(index)
    fromCenter = abs((index % myside) - (myside + 1)//2)
    res = fromCenter + (minSide +1 )//2
    #print(n, "index ", index, " fromCenter ", fromCenter, " res ", res)

    return res
#print(minSq)
#for i in range(2, len(tests)):
print(dist(val))
    #print(str(i) + " " + str(dist(i)))
