import math
deg = 80
rad= deg/180 * math.pi
x =math.cos(rad)
y =math.sin(rad)
deg2 = 35
rad2= deg2/180 * math.pi
x2 =math.cos(rad2)
y2 =math.sin(rad2)
scal = x * x2 + y * y2
ang = math.asin(scal)
deg3 = ang /math.pi * 180
print(deg3)
