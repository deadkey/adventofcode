a, b, c, d, e = 0, 0, 0, 0, 0
f = 0
#f is control
while True: # f < 36
    f += 16 #0 !!!
    c = 1 #1
    e = 1 #2
    d = c * e #3
    if d == b:
        d = 1
    else:
        d = 0
    #4
    f = d + f #5 !!
    f += 1 #6 !!!
    a = a + c #7
    e += 1 #8
    if e > b:
        d = 1
    else:
        d = 0
    # 9
    f += 3 # 10 !!!
    f = 2 #11
    c += 1 #12
    if c > b:
        d = 1
    else:
        d = 0
    f = d + 3 #14 !!!
    f = 1 #15 !!!!!
    f = f * f #16!!!!!!!!!!
    b += 2
    b = b * b
    b = b * f # 19 !!!!!!!!!!
    b = 11 * b
    d += 6
    d = d * f #22
    d += 15 # 23
    

    



