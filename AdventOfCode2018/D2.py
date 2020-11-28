from fetch import fetch
from collections import defaultdict as dd
data = fetch(2).split()
part= 2

def comp(box, box2):
    diff = 0
    difch = ''
    for index, ch in enumerate(box):
        if box2[index] != ch:
            if diff == 0:
                diff = 1
                difch = box2[:index] + box2[index+1:]
            else:
                return
    if diff== 1:
        print(len(box))
        print(len(difch))
        print(difch)



if part ==1:
    hasTwo = set([])
    hasThree = set([])
    for box in data:
        letters = dd(int)
        for ch in box:
            letters[ch] += 1
        for item, cnt in letters.items():
            if cnt == 2:
                hasTwo.add(box)
            if cnt == 3:
                hasThree.add(box)
    print('Res1')
    print('boxes', len(box))
    print('2 boxes', len(hasTwo))

    print('3 boxes', len(hasThree))
    print(len(hasTwo) * len(hasThree))
else:
    for box in data:

        #print(letters1)
        for box2 in data:
            if box != box2:
                comp(box, box2)


    print('Res2')
