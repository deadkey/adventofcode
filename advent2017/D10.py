i = map(int, input().split(','))
skip = 0
curr = 0
li = [x for x in range(256)]
for le in i:
    if curr + le >= len(li):
        sub = li[curr:] + li[0: curr + le - len(li)]
        sub.reverse()
        li[curr:] = sub[0:len(li) - curr]
        li[0:curr + le - len(li)] = sub[len(li) - curr:]
    else:
        sub = li[curr: curr + le]
        sub.reverse()
        li[curr: curr + le] = sub
    curr = (curr + le + skip) % len(li)
    skip += 1

    #print('curr', curr, 'list', li, 'skip', skip)

res = li[0]*li[1]
print(res)
