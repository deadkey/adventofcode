line = input()
f = 0
pos = 0
for i, c in enumerate(line):

    if c == '(':
        f += 1
    if c == ')':
        f -= 1
    if f == -1 and pos == 0:
        pos = i + 1

print(pos)
