dirs = input().strip()
coord = {(0, 0)}
x, y = 0, 0
rx, ry = 0,0
nesw = {'^': (0, 1), '>': (1, 0), 'v': (0,-1), '<': (-1, 0)}
for i, c in enumerate(dirs):
    xd, yd = nesw[c]
    if i % 2 == 1:
        x += xd
        y += yd
        t= (x, y)
        coord.add(t)
    else:
        rx += xd
        ry += yd
        t= (rx, ry)
        coord.add(t)
    #print('x, y', x, y, 'rx, ry', rx, ry, 'i', i)
print(len(coord))
