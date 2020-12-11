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
    db(line)
    db(line.split())
    return lazy_ints(line.split())

def simulate(player, hp, damage, armor, otherhp, otherdamage, otherarmor):
    if hp <= 0: return -player

    dam = max(1, damage - otherarmor)
    otherhp -= dam
    #db(f'Player {player} has {hp} hitpoints and other has {otherhp} hitpoints')
    return simulate(-player, otherhp, otherdamage, otherarmor, hp, damage, armor)


def p1(v):
    weapons_lines = open("weapons.txt", 'r').read().strip('\n').split('\n')
    armor_lines = open("armor.txt", 'r').read().strip('\n').split('\n')
    rings_lines = open("rings.txt", 'r').read().strip('\n').split('\n')
    weapons = [parse(line) for line in weapons_lines]
    armor = [parse(line) for line in armor_lines]
    rings = [parse(line) for line in rings_lines]
    db(weapons)
    #won = simulate(1, 8, 5, 5, 12, 7, 2)
    hitpoints = 100
    boss = (103, 9, 2)  
    best = 10 ** 10  
    
    for w in weapons:
        wcost = w[1]
        damage = w[2]
        for a in armor:
            acost = a[1]
            arm = a[3]
            for i in range(len(rings)):
                r1 = rings[i]
                d1diff = r1[3]
                r1cost = r1[2]
                r1arm = r1[4]
                for k in range(i+1, len(rings)):
                    r2 = rings[k]
                    d2diff = r2[3]
                    r2cost = r2[2]
                    r2arm = r2[4]

                    totcost = wcost + acost + r1cost + r2cost
                    totdamage = damage + d1diff + d2diff
                    totarmor = arm + r1arm + r2arm
                    won = simulate(1, hitpoints, totdamage, totarmor, boss[0], boss[1], boss[2])
                    if won == 1:
                        best = min(best, totcost)


    return best

def p2(v):
    weapons_lines = open("weapons.txt", 'r').read().strip('\n').split('\n')
    armor_lines = open("armor.txt", 'r').read().strip('\n').split('\n')
    rings_lines = open("rings.txt", 'r').read().strip('\n').split('\n')
    weapons = [parse(line) for line in weapons_lines]
    armor = [parse(line) for line in armor_lines]
    rings = [parse(line) for line in rings_lines]
    db(weapons)
    #won = simulate(1, 8, 5, 5, 12, 7, 2)
    hitpoints = 100
    boss = (103, 9, 2)  
    best = 0
    
    for w in weapons:
        wcost = w[1]
        damage = w[2]
        for a in armor:
            acost = a[1]
            arm = a[3]
            for i in range(len(rings)):
                r1 = rings[i]
                d1diff = r1[3]
                r1cost = r1[2]
                r1arm = r1[4]
                for k in range(i+1, len(rings)):
                    r2 = rings[k]
                    d2diff = r2[3]
                    r2cost = r2[2]
                    r2arm = r2[4]

                    totcost = wcost + acost + r1cost + r2cost
                    totdamage = damage + d1diff + d2diff
                    totarmor = arm + r1arm + r2arm
                    won = simulate(1, hitpoints, totdamage, totarmor, boss[0], boss[1], boss[2])
                    if won == -1:
                        best = max(best, totcost)


    return best


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2015,21, p1, p2, cmds)
if stats: print_stats()
#manual()
