n = int(input("Введіть n "))

def func(n):
    res = 0.5
    i = 2
    while i <= n:
        res *= ( 1 / 1 + i * (i - 1))
        i = i + 1
    return res

print(func(n))