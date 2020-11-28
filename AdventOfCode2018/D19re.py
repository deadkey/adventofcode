a,b, c, d, e, f = 0, 10551383, 1, 0, 0, 0
while c <= b:
    if b % c == 0:
        a += c
    c += 1
print(a)