import random

n = int(input("Введіть кількість чисел: "))
i = 1
avg = 0
while n >= i:
    num = random.randrange(1, n + 1)
    print(num)
    avg = avg + num
    i += 1
print(f'Середнє арифметичне чисел = {avg / n}')


def func(n):
    i = 1
    fct = 1
    while n >= i:
        fct = fct * i
        i += 1
    return f"Факторіал {n} = {fct}"


print(func(4))
