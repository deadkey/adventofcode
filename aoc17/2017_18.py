from collections import defaultdict as dd
from collections import deque

# Guess 3175 is too low.
# Guess 4201 is too low. 

#last_sound = -1
#recovered = -1
cnt_prog0 = 0
cnt_prog1 = 0

def val(y, reg):
    if y.isdigit() or (y[0] == '-' and y[1:].isdigit()):
        return int(y)
    return reg[y]

def snd(x, y, id, reg):

    global cnt_prog0, cnt_prog1
    v = val(x, reg)

    #last_sound[id] = x
    if id == 1:
        cnt_prog1 += 1
    if id == 0:
        cnt_prog0 += 1
    other = (id +1) % 2
    print('{} sends {} to {}'.format(id, v, other))
    msg[other].append(v)

    return 1

def sett(x, y, id, reg):
    
    reg[x]=val(y, reg)

    print('Set {} to {}, reg {}'.format(x, y, reg[x]))
    return 1

def add(x, y, id, reg):

    reg[x]= reg[x] + val(y, reg)

    print('Add {} to {}, reg {}'.format(x, y, reg[x]))
    return 1

def mul(x, y, id, reg):

    reg[x]= reg[x] * val(y, reg)

    print('Mul {} to {}, reg {}'.format(x, y, reg[x]))
    return 1

def mod(x, y, id, reg):

    reg[x]=reg[x] % val(y, reg)

    print('Mod {} to {}, reg {}'.format(x, y, reg[x]))
    return 1

def rcv(x, y, id, reg):
    if len(msg[id]) > 0:
        v =  msg[id].popleft()
        reg[x] = v

        print('{} gets {}, {}'.format(id, v, reg[x]))
        return 1
    
    print('{} waits'.format(id))
    return 0 #waiting

def jgz(x, y, id, reg):
    v = val(x, reg)
    if v > 0:
        return val(y, reg)
    
    return 1

ins = {'snd':(snd, 1), 'set':(sett, 2), 'add':(add, 2), 'mul':(mul, 2), 'rcv':(rcv, 1), 'jgz':(jgz, 2), 'mod':(mod, 2)}


import sys
data = sys.stdin.readlines()

ilist = []
for d in data:
    cmds = d.split()
    func, no = ins[cmds[0]]
    x = cmds[1]
    y = '!!'
    if no == 2:
        y = cmds[2]
    ilist.append((func, x, y))


def prog1():
    return 1

pos = [0, 0]
last_pos = [-1, -1]
deadlock_cnt = 0
regs = [dd(int), dd(prog1)]

msg = [deque([]), deque([])]
i = 0
while True:
    id = i % 2
    i += 1
    func, x, y = ilist[pos[id]]
    pos[id] += func(x,y, id, regs[id])
    print('pos', id, pos[id])
    #deadlock
    if pos[0] == last_pos[0] and pos[1] == last_pos[1]:
        deadlock_cnt += 1
    else:
        deadlock_cnt = 0
    if deadlock_cnt == 10:
        print('TERMINATED', cnt_prog1,cnt_prog0, regs[0], regs[1])
        exit()
    if pos[id] < 0 or pos[id] >= len(ilist):
        print('Outside ', cnt_prog1)
        exit()
    #if recovered > -1:
    #    print('RECENT RECOVERED', recovered)
    #    exit()
    last_pos[id] = pos[id]
      