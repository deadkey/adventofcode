import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())

def cp(d):
    newd = {}
    for key in d.keys():
        newd[key] = d[key]
    return newd

def tostring(activespells):
    li = []
    for key in activespells:
        li.append((key, activespells[key][0]))
    li.sort(reverse = True, key = lambda x: x[1])
    return ''.join(map(str, li))

def debug(player, values, spellorder, spells, activespells, seen, depth):
    atc = tostring(activespells)
    if (values['hp'], values['bosshp'], values['armor'], values['mana'], atc) in seen:
        db(len(seen))
        return seen[ (values['hp'], values['bosshp'], values['armor'], values['mana'], atc)] , 1
    #db(f'Calling for player {player} with values {values} and active spells {activespells}')
    hp = values['hp'] if player == 1 else values['bosshp']
    if hp <= 0: return 0, -player
    
    nextspells = {}
    temparmor = values['armor'] #ignored for now
    
    for spell in activespells.keys():
        time, dameff, armeff, manaeff = activespells[spell]
        time -= 1
        values['bosshp'] -= dameff
        temparmor += armeff
        values['mana'] += manaeff 
        temparmor += armeff   
        if time >0:
            nextspells[spell] = (time, dameff, armeff, manaeff)
    
    if values['hp'] <= 0 or values['bosshp'] <= 0:
        return 0, 1 if values['bosshp'] <= 0 else -1

    dam = values['bossdamage'] if player == -1 else values['damage']
    otherarmor = temparmor if player == -1 else values['bossarmor']
    dam = 0 if dam == 0 else max(1, dam - otherarmor)
    if player == 1:
        values['bosshp'] -= dam
    else:
        values['hp'] -= dam
    best = 10 ** 10
    canwin = 0
    '''
    if player == 1 and len(spellorder) > 0:
        spell = spellorder[0]
        spellorder = spellorder[1:]
        cost, instantdamage, healhp, effectL, dameff, armeff, manaeff = spells[spell]
    else:
        cost, instantdamage, healhp, effectL, dameff, armeff, manaeff = 0, 0, 0, 0, 0, 0, 0
    '''
    #if values['mana'] >= cost:
    best = 10 ** 10
    canwin = 0
    #db(f'Times = {depth}')
    for spell in spellorder:
           if spell not in nextspells:
               cost, instantdamage, healhp, effectL, dameff, armeff, manaeff = spells[spell]
               if spell == 'Recharge' and values['mana'] > 229 + 180:
                   continue
               if values['mana'] >= cost:

                    tempval = cp(values)
                    tempval['mana'] -= cost
                    tempactivespells = cp(nextspells)
                    tempval['bosshp'] -= instantdamage
                    tempval['hp']  += healhp
                    if effectL > 0:
                        tempactivespells[spell] = (effectL, dameff, armeff, manaeff)
                    #db(f'After calling for player {player} with values {tempval} and active spells {tempactivespells}\n')
                    
                    spent, winner = debug(-player, tempval, spellorder, spells, tempactivespells, seen, depth + 1)
                    if winner == 1:
                        best = min(cost + spent, best)
                        #db(f'Best {best}')
                        canwin = 1

    seen[(values['hp'], values['bosshp'], values['armor'], values['mana'], atc)] = best
    return best, canwin


def p1(v):
    #mana = 500
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    spell_lines = open("spells.txt", 'r').read().strip('\n').split('\n')
    spellList = [parse(line) for line in spell_lines]

    spells = {}
    for sp in spellList:
        name, cost, damage, healhp, effectL, dameff, armeff, manaeff = sp
        spells[name] = (cost, damage, healhp, effectL, dameff, armeff, manaeff)
    #name, cost, damage, healhp, effecttime, dameff, armoreff, manaeff
    hp = 10 #50
    mana = 250 # 500
    bosshp = 13 #55
    bossdam = 8
    values = {}
    values['hp'] = hp
    values['bosshp'] = bosshp
    values['mana'] = mana
    values['damage'] = 0
    values['bossdamage'] = bossdam
    values['armor'] = 0
    values['bossarmor'] = 0
    spellorder = ['MagicMissile', 'Drain', 'Shield','Poison', 'Recharge']
    spent, winner = debug(1, values, spellorder, spells, {}, {}, 0)

    return spent 

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,22, p1, p2, cmds)
if stats: print_stats()
#manual()
