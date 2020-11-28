import sys

lines = sys.stdin.readlines()
paper = 0
ribbon = 0
for gift in lines:
    sides = list(map(int, gift.split('x')))
    s1 = sides[0]*sides[1]
    s2 = sides[1]*sides[2]
    s3 = sides[0]*sides[2]
    res = 2 *(s1 + s2 + s3) + min(s1, s2, s3)
    paper += res
    p1 = sides[0]+sides[1]
    p2 = sides[0]+sides[2]
    p3 = sides[2]+sides[1]
    pres = 2 * min(p1, p2, p3) + sides[0]*sides[1]*sides[2]
    ribbon += pres

print('paper ', paper)
print('ribbon', ribbon)
