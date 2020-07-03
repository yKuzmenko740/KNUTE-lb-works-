import random

n = int(input('Введіть кількість чисел: '))
i = 1
max = 0
while n >= i:
    a1 = random.randrange(2, n + 1)
    print(a1)
    if a1 > max:
        max = a1
    i = i + 1
print(f"Максимальне число = {max}")
