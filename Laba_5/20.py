import random
lst = []
summa = 0
n = int(input("Довжина списку: "))
for i in range(n):
    lst.append(random.randint(0, 10))
print(lst)
for i in range(1, len(lst)):
    if i % 2 == 0:
        summa += lst[i]
print(f"Сумма елементів з парними індексами = {summa}")