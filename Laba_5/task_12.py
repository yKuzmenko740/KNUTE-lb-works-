import random
n = int(input("Довжина списку: "))
list = []
for i in range(n):
    list.append(random.randint(0, 20))
print(list)


def syma(a):
    summ = 0
    for i in a:
        summ += i
    return summ


print(syma(list))
