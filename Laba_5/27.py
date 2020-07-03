import random

lst = []
n = int(input("Довжина списку: "))
for i in range(n+1):
    lst.append(random.randint(0, 10))
print(lst)

def arif(lst, len):
    summa = 0
    for i in lst:
        summa += i
    return summa / len
print(arif(lst,n))
