
n = int(input("Введіть число : "))


def func_summ(n):
    i = 1
    fct = 1
    summ = 0
    while n >= i:
        fct = fct * i
        i += 1
        summ += fct
    return f"Сумма факториалов равняется {summ}"


print(func_summ(n))
