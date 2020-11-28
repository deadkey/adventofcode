import sys
lines = sys.stdin.readlines()
grid = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]
for line in lines:
    on = 1
    if 'off' in line:
        line = line.replace('turn off', '')
        on = -1
    elif 'toggle' in line:
        on = 2
        line = line.replace('toggle', '')
    else:
        line = line.replace('turn on', '')

    line = line.replace('through', '')
    line = line.replace(',', ' ')
    coord = list(map(int, line.split()))
    startX = coord[0]
    startY = coord[1]
    endX = coord[2]
    endY = coord[3]

    for x in range(startX, endX +1):
        for y in range(startY, endY +1):
            grid[x][y] = max(0, grid[x][y] + on)

count = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        count += grid[x][y]
print(count)
