from fetch import fetch
import sys

fetch(9)
players = 430
last = 7158800

scores = [0 for _  in range(players)]
stones = [0, 1]
current = 1
for stone in range(2, last+1):
    if stone % 23 == 0:
        remove = (current - 7) % len(stones)
        scores[(stone % players)] += stone + stones[remove]
    #    print('removed at ', remove, stones[remove])
        del stones[remove]
        current = remove % len(stones)
    #    print(current, stones)

    else:
        insert = (current + 2) % len(stones)
        if insert == 0:
            stones.append(stone)
            current = len(stones) - 1
        else:
            stones.insert(insert, stone)
            current = insert
    #    print('added at ', insert)
    #    print(current, stones)
print(max(scores))
#for line in data:
