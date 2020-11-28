from fetch import fetch
import sys

fetch(9)
forward = {}
backward = {}
players = 430
last = 7158800

scores = [0 for _  in range(players)]
forward[0] = 0
backward[0] = 0
current = 0


for stone in range(1, last+1):
    if stone % 23 == 0:
        remove = current
        for n in range(7):
            remove = backward[remove]
        linkback = backward[remove]
        linkin = forward[remove]
        forward[linkback] = linkin

        backward[linkin] = linkback
        current = linkin
        scores[(stone %players)] += stone + remove
    #    print('removing ', remove, linkback, linkin)
    #    print(forward)
    #    print(backward)

    else:
        insertion = current
    #    print(insertion)
        insertion = forward[insertion]
        linkback = backward[insertion]
        linkin = forward[insertion]
        forward[insertion] = stone
        forward[stone] = linkin
        backward[stone] = insertion
        backward[linkin] = stone
        current = stone
    #    print(insertion, stone)
    #    print(forward)
    #    print(backward)
    #    print('added at ', insert)
    #    print(current, stones)
print(max(scores))
#for line in data:
