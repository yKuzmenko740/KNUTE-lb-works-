n = int(input("Введіть номер числа Фібоначчі : "))

def fib(n):
    fib1 = 1
    fib2 = 1
    i = 2
    fib_sum = 0
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    return fib_sum


print(f"Число = {fib(n)}")
