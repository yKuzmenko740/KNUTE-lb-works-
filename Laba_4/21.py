import math

c = int(input("Введіть число: "))


def func(c):
    i = 1
    while math.factorial(i) < c:
        i+=1
    return i

print(func(c))