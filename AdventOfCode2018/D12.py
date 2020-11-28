from fetch import fetch, fetchlines
from collections import Counter, defaultdict as dd
import sys

limit = 200
tinit = '.' * (2 * limit) + '#...####.##..####..#.##....##...###.##.#..######..#..#..###..##.#.###.#####.##.#.#.#.##....#..#..#..' + '.' * (2 * limit)
data = sys.stdin.readlines()
rules= {}
for d in data:
    rule, res = d.split('=>')
    rules[rule.strip()] = res.strip()
plants = [ch for ch in tinit]
#print(rules)
def score(plants):
    cnt = 0
    for index, plant in enumerate(plants):
        if plant == '#':
            cnt+= (index - (2 * limit))
    return cnt
scores = []
for gen in range(limit):

#    print(''.join(plants))
    nextgen = ['.'] * len(tinit)
    for plant in range(2, len(tinit) -2):
        neigh = ''.join(plants[plant-2:plant+3])
        res = '.'
        if neigh in rules:
            res = rules[neigh]
        nextgen[plant] = res
    #    print(neigh, res)

    plants = nextgen
    scores.append(score(plants))
diffs = []
for index in range(len(scores)-1):
    diffs.append(scores[index +1] - scores[index])
print(scores)
print(diffs)
 # after 200 i have score 17480
gens = 50000000000 - 200
bigscore = scores[-1] + diffs[-1] * gens
print(bigscore)
