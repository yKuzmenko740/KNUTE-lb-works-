import random

lst = []
n = int(input("Довжина списку: "))
for i in range(n):
    lst.append(random.randint(-100, 10))
print(lst)

for i in range(2,len(lst)):
    if i % 2 == 0:
        if lst[i] < 0:
            print(f"Відємне число{lst[i]} під індексом {i}")
