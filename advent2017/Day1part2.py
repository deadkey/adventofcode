s = input()
tot = 0
l = len(s)
half = l//2
for i in range(0, l):
    if s[i] == s[i-half]:
        tot += int(s[i])
print(tot)
