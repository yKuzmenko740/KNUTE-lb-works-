n = int(input("Введіть число: "))


def func(n):
    i = 1
    res = 0
    while i <= n:
        res += (1 / (1 + i ** 2))
        i = i + 1
    return res


print(func(n))
