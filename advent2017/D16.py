import sys
lines = sys.stdin.readlines()
#print(lines)
i = ','.join(lines).split(',')
#print(i)
testprogs = [chr(ord('a') + i) for i in range(5)]
progs = [chr(ord('a') + i) for i in range(16)]
#progs = testprogs
times = 1000000000

def spin(progs, nbr):
    if nbr >= len(progs):
        print("Handle length!")
    if nbr == 0:
        print("Haha!")
        return progs
    end = progs[-nbr:]
    beginning = progs[:- nbr]
    #end.reverse()
    return end + beginning

def exchange(progs, a, b):
    tmp = progs[a]
    progs[a] = progs[b]
    progs[b] = tmp
    return progs

def partner(progs, A, B):
    index1 = progs.index(A)
    index2 = progs.index(B)
    if 0<= index1 < len(progs) and 0 <= index2 < len(progs):
        return exchange(progs, index1, index2)
    else:
        print("Hahahha")
        return progs
#jhdgpeobfklmaicn
def dance(progs, i):
    for cmd in i:
        cmd = cmd.strip()
        if cmd[0] == 's':
            progs = spin(progs, int(cmd[1:]))
        #    print(cmd, ' ', str(int(cmd[1:])))

        if cmd[0] == 'x':
            index1, index2 = map(int, cmd[1:].split('/'))
            progs = exchange(progs, index1, index2)
        #    print(cmd, ' ', index1, ', ',index2)
        if cmd[0] == 'p':
            name1, name2 = cmd[1:].split('/')
            progs = partner(progs, name1.strip(), name2.strip())
        #    print(cmd, ' ', name1, ', ',name2)
        #print(progs)
    return progs
turn = 0
dances = {}
noloop = True
while turn < times and noloop:
    progs = dance(progs, i)
    #print(progs)
    turn += 1
    key = ''.join(progs)
    if key in dances:
        loop = turn - dances[key]
        times_left = (times - turn) % loop
        for k in dances:
            if dances[k] == dances[key] + times_left:
                print(k)
                noloop = False  
                break

    dances[key] = turn
#print(''.join(progs))
