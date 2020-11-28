from fetch import fetch, fetchlines
from collections import Counter
from collections import namedtuple 
from collections import defaultdict as dd
from heapq import heappush as push
from heapq import heappop as pop
import sys

Group = namedtuple('Group', 'army id units hitpoints immuneto weaknesses power damagetype initiative comment')
data = sys.stdin.read()

def parse_line(army, id, s, boost):
    v = s.split()
    units = [int(v[0])]
    hp = int(v[4])
    immune = []
    weak = []
    i = 7
    if v[7][0] == '(':
        i = 8
        while i < len(v) and v[i][-1] != ')':
            i+=1
        S = ' '.join(v[7:i+1])
        L = S.split(';')
        for x in L:
            xs = x.split()
            if 'weak' in x:
                for s in xs[2:]:
                    weak.append(s.strip(',)'))
            else:
                for s in xs[2:]:
                    immune.append(s.strip(',)'))
        i+= 1

    attack_pw = int(v[i+5])
    attack_type = v[i+6]
    init = int(v[-1])
    if army == 'im':
        attack_pw += boost
    return Group(army, id, units, hp, immune, weak, attack_pw, attack_type, init, '')

def setup(boost):
    
    immunes, attackers = data.split('\n\n')
    idx = 0
    immune = set()
    attack = set()
    allgr = []
    for line in immunes.split('\n'):
        gr = parse_line('im', idx, line, boost)
        immune.add(idx)
        allgr.append(gr)
      #  print(gr)
        idx += 1

    for line in attackers.split('\n'):
        gr = parse_line('att', idx, line,boost)
        attack.add(idx)
      #  print(gr)
        allgr.append(gr)
        idx += 1
    

    return immune, attack, allgr


def select_enemy(gr, enemy_ids, allgr, selected):
    score = {}
    for enemy_id in enemy_ids:
        if enemy_id not in selected:
            enemy = allgr[enemy_id]
            if gr.damagetype in enemy.immuneto:
                score[enemy.id] = 0
            elif gr.damagetype in enemy.weaknesses:
                score[enemy.id] = 2 * gr.power * gr.units[0]
            else:
                score[enemy.id] = gr.power * gr.units[0]
          #  print('{} would deal {} {} damage'.format(gr.comment, enemy.comment, score[enemy_id]))
   
    ranking = []      
    for enemy_id in enemy_ids:
        if enemy_id not in selected and score[enemy_id] > 0:
            en = allgr[enemy_id]
            efp = en.units[0] * en.power
           # if score[enemy_id] >= en.hitpoints:
            ranking.append((score[enemy_id], efp, allgr[enemy_id].initiative, enemy_id))
    ranking.sort(reverse = True)
    
    if len(ranking)> 0:
        if ranking[0][0] == 0: return -1
        return ranking[0][3]    
    return -1


def do_attack(attacker, defender):
    attack_power = 0
    if attacker.damagetype in defender.weaknesses:
        attack_power = 2 * attacker.power * attacker.units[0]
    elif attacker.damagetype in defender.immuneto:
        attack_power = 0
    else:
        attack_power = attacker.power  * attacker.units[0]
    killed_units = min(attack_power // defender.hitpoints, defender.units[0])
    defender.units[0] = defender.units[0] - killed_units

  #  print('Attacking {} {} power {} killed {}'.format(attacker.comment, defender.comment, attack_power, killed_units))
    return killed_units

def selection(immuneleft, attackleft, dead, allgr):
    eff_pow = []

    for index, gr in enumerate(allgr):
        if gr.id not in dead:
            eff = gr.units[0] * gr.power
            if eff > 0:
                eff_pow.append((eff, gr.initiative, gr.id))
    eff_pow.sort(reverse = True)

    sel_imm = set(dead)
    sel_att = set(dead)
    attacks = {}
    for _, _, gr_id in eff_pow:
        gr = allgr[gr_id]
        selected = sel_imm if gr.army == 'att' else sel_att
        enemy_ids = immuneleft if gr.army == 'att' else attackleft
        to_attack = select_enemy(gr, enemy_ids, allgr, selected)
        selected.add(to_attack)
        attacks[gr.id] = to_attack
    return attacks


def printstatus(immune, attack, allgr, dead):
    print('Immune system')
    for gr_id in immune:
        if gr_id not in dead:
            gr = allgr[gr_id]
            print('Group {} contains {} units'.format(gr.comment, gr.units[0]))

    print('Infection')
    for gr_id in attack:
        if gr_id not in dead:
            gr = allgr[gr_id]
            print('Group {} contains {} units'.format(gr.comment, gr.units[0]))
    print('')
    

def runtest(boost):
    immune, attack, allgr = setup(boost)


    # selection phase
    #the ranking will not change!

    attack_order = []
    for gr in allgr:
        attack_order.append((gr.initiative, gr.id))
    attack_order.sort(reverse = True)



    immuneleft = set(immune)
    attackleft = set(attack)
    dead = set()
    hpstate = [v.units[0] for v in allgr]
   # printstatus(immuneleft, attackleft, allgr, dead)
    while len(immuneleft) > 0 and len(attackleft) > 0: 
    #for i in range(10):
        attacks = selection(immuneleft, attackleft, dead, allgr)
        #attack phase
       # print(attacks)
        
       # print(' '.join(map(str, [v.units[0] for v in allgr])))
        for _,  gr_id in attack_order:
            if gr_id not in dead and gr_id in attacks:
                gr = allgr[gr_id]
      
    Current frequency  0, change of +1; resulting frequency  1.
    Current frequency  1, change of -2; resulting frequency -1.
    Current frequency -1, change of +3; resulting frequency  2.
    Current frequency  2, change of +1; resulting frequency  3.
    (At this point, the device continues from the start of the list.)
    Current frequency  3, change of +1; resulting frequency  4.
    Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
          if gr.units[0] > 0 and attacks[gr.id] > -1:
                    to_attack =allgr[attacks[gr.id]]
            
                    kills= do_attack(gr, to_attack)
                 #   print('{} attacks {} killing {}'.format(gr.id, attacks[gr.id], kills))
            
                    if to_attack.units[0] <= 0:
                        remove_from = immuneleft if to_attack.army == 'im' else attackleft
                        remove_from.remove(to_attack.id)
                        dead.add(to_attack.id)
     #   print('tries to fight', immuneleft, attackleft)
     #   print('nbr of dead', len(dead))
        new_state = [v.units[0] for v in allgr]
        if hpstate == new_state:
            return 'inf', 'att'
        hpstate= new_state
    #printstatus(immuneleft, attackleft, allgr, dead)

    winning_army = 0
    for gr_id in immuneleft | attackleft:
        gr = allgr[gr_id]
        winning_army += gr.units[0]
    #print(winning_army)
    if len(immuneleft) > len(attackleft):
        return  'im', winning_army
    else:
        return 'att', winning_army

winning = 10000
losing = 0
cnt = 0
lastwon =  0 # 35
# 26
for boost in range(100):
    res, score = runtest(boost)
    print(boost)
    if res == 'im':
       print('won', score)
    
  #  print(mid, lastwon) 
