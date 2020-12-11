mm = 67
ms = 47
bm = 36 + 4
nh = 22
winall = 8 + 6
loseall = 4 + 2
for day in range(11, 26):
    left = 25 - day
    otherswin = winall * left
    welose = left * loseall
    if mm + ms + loseall > bm + nh + otherswin:
        print(f'Day {day} we have won') 