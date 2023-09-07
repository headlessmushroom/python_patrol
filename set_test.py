import random

d = [5,7,11,10,14,22,15,21,33]
#d = list[int]

c = random.choice(d)

print(c)
print(d)
    
d.remove(c)

print(d)