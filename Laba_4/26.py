num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return f'Нсд = {num1}'
print(gcd(num1,num2))