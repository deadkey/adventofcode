from fetch import fetch
import sys

data = sys.stdin.readlines()
squares = []

maxX =0
maxY=0
for s in data:
    d= s.split()
    id= int(d[0][1:])
    x,y= map(int, d[2][:-1].split(','))
    wx, wy = map(int, d[3].split('x'))
    squares.append((id, x, y, wx, wy))
    maxX = max(maxX, x + wx)
    maxY = max(maxY, y + wy)


cloth = [[0] * (maxY+1) for _ in range(maxX+1)]
cnt= 0
for id, x,y, dx, dy in squares:
    for rx in range(x, x + dx):
        for ry in range(y, y +dy):
            if cloth[rx][ry] == 0:
                cloth[rx][ry] = id
            else:
                cloth[rx][ry] = -1

for rx in range(maxX):
    for ry in range(maxY):
        if cloth[rx][ry] == -1:
            cnt+=1

print(cnt)
#print(cloth)

def check(x, y, dx, dy):
    for rx in range(x, x + dx):
        for ry in range(y, y +dy):
            if cloth[rx][ry] == -1:
                return False
    return True

for id, x,y, dx, dy in squares:
    if check(x,y, dx,dy):
        print(id)
        exit()
