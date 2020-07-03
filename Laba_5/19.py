import random

lst = []
n = int(input("Довжина списку: "))
for i in range(n):
    lst.append(random.randint(0, 10))
print(lst)
c = int(input("Введіть число: "))
lst2 = sorted(lst)
print(lst2)

for i in range(1, len(lst2)+1):
    if i % 7 ==0:
        lst2.insert(i, c)
    else:
        print(f"Індекс {i} не кратний 7 ")
print(lst2)
