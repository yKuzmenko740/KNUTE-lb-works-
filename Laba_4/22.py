n = int(input("Введіть число: "))


def fact(n):
    i = 1
    x = 0
    while i > 0:
        x += 1 / i
        i = i + 1
        if x > n:
            return f'Число більше заданого = {x}.Кількість циклів {i}'

print(fact(n))