steps = 314
spinlock = [0]
index = 0
for i in range(1, 2018):
    index = (index + steps) % i
    spinlock.insert(index + 1, i)
    index = index + 1
    #print(spinlock)
#print(spinlock[1])
# part 2
steps = 314
val = 0
index = 0
for i in range(1, 50000000):
    index = (index + steps) % i
    if index == 0:
         val = i
    index = index + 1
    #print(val)
print(val)
