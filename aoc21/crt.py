def gcd(a, b):return gcd(b, a % b) if b else a

# x * a + y * b = gcd(a, b). Return gcd(a, b), x, y
def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = (a // b, b, a % b)
        x0, x1 = (x1, x0 - q * x1)
        y0, y1 = (y1, y0 - q * y1)
    return (a, x0, y0)

#If a list of t = a1 mod n1, t = a2 mod n2 ... Given a list of a and n, returns t, see d13 2020
def crt(la, ln):
    assert len(la) == len(ln)
    for i in range(len(la)):
        assert 0 <= la[i] < ln[i]
    prod = 1
    for n in ln:
        assert gcd(prod, n) == 1
        prod *= n
    lN = []
    for n in ln:
        lN.append(prod//n)
    x = 0
    for i, a in enumerate(la):
        print(lN[i], ln[i])
        _, Mi, mi = xgcd(lN[i], ln[i])
        x += a*Mi*lN[i]
    return x % prod   