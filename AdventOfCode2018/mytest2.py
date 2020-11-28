a, b, c, d, e = 0, 0, 0, 0, 0
f = 0
a = 1
#f is control
while True: # f < 36
    f += 16 #0 !!!
    
    # second start
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

    f = 16 * 16 #16!!!!!!!!!! breaks!

    # here it starts
    b += 2 #17
    b = b * b #18
    b = b * 19 # 19 !!!!!!!!!!
    b = 11 * b
    d += 6
    d = d * 22 #22
    d += 15 # 23
    b += 3

    f = f + a # 25
    f = 0 #26 restarts!

    d = 27 # =  #27
    d = 28 * 27 # 28 = 756 
    d = 29 + d #= 785
    d = 30 * 785 #=23550  #30
    d = d * 14 #31 = 329700
    d = 32 * d #32 = 10550400 
    b = b + d 
    a = 0
    f = 0 # restarts!



    


##############################################
while True: # f < 36
    #restart!


    #######
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
    f = 16 * 16 #16!!!!!!!!!! breaks!
    b += 2 #17
    b = b * b #18
    b = b * 19 # 19 !!!!!!!!!!
    b = 11 * b
    d += 6
    d = d * f #22
    d += 15 # 23
    b += 3
    f = f + a # 25
    f = 0 #26 restarts!

    d = 27 # =  #27
    d = 28 * 27 # 28 = 756 
    d = 29 + d #= 785
    d = 30 * 785 #=23550  #30
    d = d * 14 #31 = 329700
    d = 32 * d #32 = 10550400 
    b = b + d 
    a = 0
    f = 0 # restarts!
