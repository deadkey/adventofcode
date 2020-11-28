import hashlib
def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

key = "ckczppom"
c = 1
while 1:
    if md5(key+str(c)).startswith('000000'):
        break
    c += 1
print(c)
