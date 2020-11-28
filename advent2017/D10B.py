from functools import reduce

def knothash(raw):

    i = [ord(c) for c in raw] + [17, 31, 73, 47, 23]
    skip = 0
    curr = 0
    #print(i)
    li = [x for x in range(256)]
    def hashy(curr, skip):
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

        return curr, skip
    for x in range(64):
        curr, skip = hashy(curr, skip)

    chunks = [li[ii:ii + 16] for ii in range(0, len(li), 16)]
    def tohex(c):
        s = hex(c)[2:]
        if len(s) < 2:
            return '0' + s
        return s

    chars = []
    for chunk in chunks:
        val = reduce(lambda a, b: a ^ b, chunk, 0)
        chars.append(tohex(val))

    return ''.join(chars)
if __name__ == '__main__':
    knothash(input())
