#Generator A starts with 289
#Generator B starts with 629
#generator A uses 16807; generator B uses 48271
div = 2147483647
A = 289# 65 #289
B = 629#8921# 629

def loop(V, fac, dev):
    while 1:
        V = (V * fac) % div
        if V % dev == 0:
            break
    return V

def next(A, B):
    A_fac = 16807
    B_fac = 48271
    A = loop(A, A_fac, 4)
    B = loop(B, B_fac, 8)
    return (A, B)

c = 0
for i in range(int(5e6)):
#for i in range(5):
    A, B = next(A, B)
    a_bin = A & ((1 << 16) - 1)
    b_bin = B & ((1 << 16) - 1)

    if a_bin == b_bin:
        c += 1
        print('tick', i)
        #print('A', A, 'B', B)
print(c)
