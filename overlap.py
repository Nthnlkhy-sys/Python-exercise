import random

a = range(1, random.randint(1,30))
b = range(1, random.randint(10,40))

print(a)
print(b)

for x in b:
    if x in a:
        print (x)
