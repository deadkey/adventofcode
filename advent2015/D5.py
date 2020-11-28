import sys
lines = sys.stdin.readlines()

def hasDouble(s):
    ch = s[0]
    for c in s[1:]:
        if c == ch:
            return True
        ch = c
    return False

def hasForbidden(s):
    return ('ab' in s or
        'cd' in s or
        'pq' in s or
        'xy' in s)

def hasVowels(s):
    vowels = 'aeiou'
    vov = 0
    for c in s:
        if c in vowels:
            vov += 1
    return vov >= 3

def hasOneBetween(s):
    for i, c in enumerate(s[0:-2]):
        if c == s[i + 2]:
            return True
    return False

def hasRepeats(s):
    for i, y in enumerate(s[0:-3]):
        pair = s[i:i+2]
        for k in range(i + 2, len(s)):
            pair2 = s[k: k+2]

            if pair == pair2:
                return True


def nice(s):
#    return (not hasForbidden(s)) and hasDouble(s) and hasVowels(s)
    return hasRepeats(s) and hasOneBetween(s)


niceStrings = 0
for line in lines:
    if nice(line.strip()):
        niceStrings += 1
print(niceStrings)
