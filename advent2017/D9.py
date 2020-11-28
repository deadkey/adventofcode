line = list(input())
# av med alla !
garbage = 0
for i, c in enumerate(line):
    if c == '!':
        line[i+1] = 'a'
line = list(''.join(line).replace('!a', ''))

ingarbage = False
for i, c in enumerate(line):
    if not ingarbage and c == '<':
        ingarbage = True
    elif ingarbage and c == '>':
        ingarbage = False
    elif ingarbage:
        line[i] = 'a'
        garbage += 1
s = 0
pars = 0

for c in line:
    if c == '{':
        pars += 1
        s += pars
    if c == '}':
        pars -= 1
print(s)
print('garbage ', garbage)
