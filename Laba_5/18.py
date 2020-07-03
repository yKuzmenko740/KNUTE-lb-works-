import random

lst = []
n = int(input("Довжина списку: "))
for i in range(n):
    lst.append(random.randint(0, 10))
print(lst)

lst = sorted(lst, reverse=True)
print(lst)
# lst2 = sorted(lst)
# lst2 = reversed(lst2)
# print(lst2)
