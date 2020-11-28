s = input()
tot = 0
for i in range(0, len(s)):
    if s[i] == s[i-1]:
        tot += int(s[i])
print(tot)
