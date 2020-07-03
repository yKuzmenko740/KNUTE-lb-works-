import random

lst = []
n = int(input("Довжина списку: "))
for i in range(n):
    lst.append(random.randint(0, 10))
print(lst)

def func(lst):
    for i in range(len(lst)):
        if lst[i]>lst[i+1]:
            return True
        else:
            return False
print(func(lst))
