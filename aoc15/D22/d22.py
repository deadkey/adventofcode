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

from heapq import heappop as pop, heappush as push

def db(*a): 
    if DB: print(*a)

def parse(line):
    return lazy_ints(line.split())



def inf():return 10 ** 12

def p1(v):
    #mana = 500
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')

    hp = 50 #10#50
    mana = 500 # 250#
    bosshp = 55 #55
    bossdamage = 8
    mm_cost = 53
    mm_damage = 4
    d_cost = 73
    d_hp = 2
    d_damage = 2
    sh_cost = 113
    sh_arm = 7
    sh_eff = 6
    poi_eff = 6
    re_eff = 5
    poi_dam = 3
    re_mana = 101
    poi_cost = 173
    re_cost = 229
    testcost = re_cost + sh_cost + d_cost + poi_cost + mm_cost
    db(testcost) 
    spending = defaultdict(inf)
    pq = []
    startstate = (True, hp, mana, bosshp, bossdamage, 0, 0, 0)
    pq.append((0,startstate))
    spending[startstate] = 0
    done = False
    
    while pq and not done:
        spent, currstate = pop(pq)
        db(f'Spent {spent} currstate {currstate}')
        player, hp, mana, bosshp, bossdamage, sh, poi, rec = currstate
        if bosshp <= 0:
            
            return spent
        else:
            if not player:
                armor = int(sh >0) * sh_arm
                #boss. Deal damage from active spells;
                bosshp -= int(poi >0) * poi_dam
                if bosshp <= 0: return spent
                mana += int(rec >0) * re_mana
                hp -= max(1, bossdamage - armor)
                boss_alt = not player, hp, mana, bosshp, bossdamage, max(sh -1, 0), max(0, poi-1), max(rec-1, 0)
                if hp >0 and spending[boss_alt] > spending[currstate]:
                    spending[boss_alt] = spent
                    push(pq, (spent, boss_alt))
                    db(f'Boss done, current state {boss_alt}')
            else:
                bosshp -= int(poi >0) * poi_dam
                if bosshp <= 0: return spent
                mana += int(rec >0) * re_mana
                #active spells should be carried out.
                #deal damage.

                if player:
                    #cast magic missile
                    if mana >= mm_cost:
                        mm_alt = not player, hp, mana- mm_cost, bosshp- mm_damage, bossdamage, max(sh -1, 0), max(0, poi-1), max(rec-1, 0)
                        if spending[mm_alt] > spending[currstate] + mm_cost:
                            newcost = spent + mm_cost
                            spending[mm_alt] = newcost
                            push(pq, (newcost, mm_alt))
                    # cast drain

                    if mana >= d_cost:
                        d_alt = not player, hp+d_hp, mana- d_cost, bosshp-d_damage, bossdamage, max(sh -1, 0), max(0, poi-1), max(rec-1, 0)
                        if spending[d_alt] > spending[currstate] + d_cost:
                            newcost = spent + d_cost
                            spending[d_alt] = newcost
                            push(pq, (newcost, d_alt))

                    #cast shield

                    if mana >= sh_cost and sh == 0:
                        
                        sh_alt = not player, hp, mana- sh_cost, bosshp, bossdamage, sh_eff, max(0, poi-1), max(rec-1, 0)
                        if spending[sh_alt] > spending[currstate] + sh_cost:
                            newcost = spent + sh_cost
                            spending[sh_alt] = newcost
                            push(pq, (newcost, sh_alt))

                    #cast poison

                    if mana >= poi_cost and poi == 0:
                        
                        poi_alt = not player, hp, mana- poi_cost, bosshp, bossdamage, max(sh-1, 0),poi_eff, max(rec-1, 0)
                        if spending[poi_alt] > spending[currstate] + poi_cost:
                            newcost = spent + poi_cost
                            spending[poi_alt] = newcost
                            push(pq, (newcost, poi_alt))
                    #cast recharge

                    if mana >= re_cost and rec == 0:
                        
                        rec_alt = not player, hp, mana- poi_cost, bosshp, bossdamage, max(sh-1, 0), max(0, poi-1), re_eff
                        if spending[rec_alt] > spending[currstate] + re_cost:
                            newcost = spent + re_cost
                            spending[rec_alt] = newcost
                            push(pq, (newcost, rec_alt))
                    

    return best

def p2(v):
    #mana = 500
    hp = 50#10#50
    mana = 500 # 250#
    bosshp = 55 #55
    bossdamage = 8
    mm_cost = 53
    mm_damage = 4
    d_cost = 73
    d_hp = 2
    d_damage = 2
    sh_cost = 113
    sh_arm = 7
    sh_eff = 6
    poi_eff = 6
    re_eff = 5
    poi_dam = 3
    re_mana = 101
    poi_cost = 173
    re_cost = 229
    testcost = re_cost + sh_cost + d_cost + poi_cost + mm_cost
    db(testcost) 
    spending = defaultdict(inf)
    pq = []
    startstate = (True, hp, mana, bosshp, bossdamage, 0, 0, 0)
    pq.append((0,startstate))
    spending[startstate] = 0
    done = False
    
    while pq and not done:
        spent, currstate = pop(pq)
        db(f'Spent {spent} currstate {currstate}')
        player, hp, mana, bosshp, bossdamage, sh, poi, rec = currstate

        if bosshp <= 0:    
            return spent
        
        else:

            if not player:
                armor = int(sh >0) * sh_arm
                #boss. Deal damage from active spells;
                bosshp -= int(poi >0) * poi_dam
                
                if bosshp <= 0: return spent
                mana += int(rec >0) * re_mana
                hp -= max(1, bossdamage - armor)
                boss_alt = not player, hp, mana, bosshp, bossdamage, max(sh -1, 0), max(0, poi-1), max(rec-1, 0)
                if hp >0 and spending[boss_alt] > spending[currstate]:
                    spending[boss_alt] = spent
                    push(pq, (spent, boss_alt))
                    #db(f'Boss done, current state {boss_alt}')
            else:
                    
                hp -= 1
                if hp < 0: continue

                bosshp -= int(poi >0) * poi_dam
                if bosshp <= 0: return spent
                mana += int(rec >0) * re_mana

                sh, poi, rec = max(sh -1, 0), max(0, poi-1), max(rec-1, 0)

                #active spells should be carried out.
                #deal damage.

                if player:
                   

                    #cast magic missile
                    if mana >= mm_cost:
                        mm_alt = not player, hp, mana- mm_cost, bosshp- mm_damage, bossdamage, sh, poi, rec 
                        if hp > 0 and spending[mm_alt] > spending[currstate] + mm_cost:
                            newcost = spent + mm_cost
                            spending[mm_alt] = newcost
                            push(pq, (newcost, mm_alt))
                    # cast drain

                    if mana >= d_cost:
                        d_alt = not player, hp+d_hp, mana- d_cost, bosshp-d_damage, bossdamage, sh, poi, rec
                        if hp + d_hp > 0 and spending[d_alt] > spending[currstate] + d_cost:
                            newcost = spent + d_cost
                            spending[d_alt] = newcost
                            push(pq, (newcost, d_alt))

                    #cast shield

                    if mana >= sh_cost and sh == 0:
                        
                        sh_alt = not player, hp, mana- sh_cost, bosshp, bossdamage, sh_eff, poi, rec
                        if hp > 0 and spending[sh_alt] > spending[currstate] + sh_cost:
                            newcost = spent + sh_cost
                            spending[sh_alt] = newcost
                            push(pq, (newcost, sh_alt))

                    #cast poison

                    if mana >= poi_cost and poi == 0:
                        
                        poi_alt = not player, hp, mana- poi_cost, bosshp, bossdamage, sh,poi_eff, rec
                        if hp > 0 and spending[poi_alt] > spending[currstate] + poi_cost:
                            newcost = spent + poi_cost
                            spending[poi_alt] = newcost
                            push(pq, (newcost, poi_alt))
                    #cast recharge

                    if mana >= re_cost and rec == 0:
                        
                        rec_alt = not player, hp, mana- re_cost, bosshp, bossdamage, sh, poi, re_eff
                        if hp > 0 and spending[rec_alt] > spending[currstate] + re_cost:
                            newcost = spent + re_cost
                            spending[rec_alt] = newcost
                            push(pq, (newcost, rec_alt))
                    

    return best



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,22, p1, p2, cmds)
if stats: print_stats()
#manual()
