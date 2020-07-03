import random
lst = []
n = int(input("Довжина списку: "))
for i in range(n):
    lst.append(random.randint(0, 101))
print(lst)


def fnc(lst):
    average= sum(lst)/len(lst)
    print(average)
    g=[i for i in lst if i > average]
    return g

print(fnc(lst))
