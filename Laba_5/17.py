import random

lst = []
n = int(input("Довжина списку: "))
for i in range(n):
    lst.append(random.randint(0, 10))
print(lst)
lst.sort()
print(lst)
dct_1 = dict()
a = 0

for i in lst:
    if i % 2 == 0:
        dct_1[i] = a
    if i % 2 != 0:
        a = i
print(dct_1)
