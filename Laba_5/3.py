import random
list = []
for i in range(10):
    list.append(random.randint(0,10))
print(list)
del list[2::3]
print(list)