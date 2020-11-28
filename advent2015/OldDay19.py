
import sys
from collections import defaultdict
import re

lines = sys.stdin.readlines()

mol = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

def applyRule(rule, mol):
    blah = set()
    for (res) in re.finditer(rule[0], mol):
        news = mol[:res.start()] + rule[1].strip() + mol[res.end():]
        #print(news)
        blah.add(news)
    return blah

def applyBackward(right, left, mol):
    return mol.replace(right, left)

backrules = defaultdict(list)
onestep = set()
count = 0

for line in lines:
    rule = line.split(' => ')
    backrules[rule[1].strip()] = rule[0].strip()

while 'Ca' in mol:
    for r in backrules.keys():
        if 'Ca' in r and r in mol:
            mol = applyBackward(r, backrules[r], mol)
            count += 1
print("No ca ", mol)
ArRules = ['SiRnFAr', 'CRnMgAr', 'NRnMgAr', 'ThRnFAr', 'TiRnFAr', 'CRnMgYFAr', 'CRnAlAr',
'CRnFYFAr', 'CRnFYFYFAr', 'CRnFYMgAr', 'NRnFYFAr', 'ORnFAr', 'CRnFAr', 'CRnMgAr', 'NRnFAr']

print(ArRules)


startcount = 0
while startcount != count:
    startcount = count
    for r in ArRules:
        if r in mol:
            mol = applyBackward(r, backrules[r], mol)
            print(mol)
            count += 1

print('count' , count)
print(mol)
#print(len(onestep))
