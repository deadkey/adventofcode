line = input()
# av med alla !
for i, c in enumerate(line):
    if c == '!':
        line[i+1] = 'a'
ingarbage = False
for i, c in enumerate(line):
    if not ingarbage and c == '<':
        ingarbage = True
    elif ingarbage and x == '>':
        ingarbage = False
    elif ingarbage:
        line[i] = 'a'
s = 0
pars = 0

for c in line:
    if c == '{':
        pars += 1
        s += pars
    if c == '}':
        pars -= 1
print(s)
