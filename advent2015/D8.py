from collections import Counter
import sys
lines = sys.stdin.readlines()
regs = Counter()
for line in lines:
    #ioe dec 890 if qk > -10
    r1, ins, v, _, r2, c, v2 = line.split()
    regs.add(r1)
    regs.add(r2)
