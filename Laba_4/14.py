#
# def index(i):
#     x = (1 - 1 / (i + 1) ** 2)
#     return x
#
# x = 1
# i = 1
#
# while i > 0:
#     i += 1
#     test = abs(index(i) - index(i - 1))
#     num = test > 0
#     if num:
#         break
#
# n = int(input("Введіть значення:  "))
# if n > num:
#     print(test)
# else:
#     print("Число не підпадає під умови математичного прикладу")
# def index(i):
#     x = (1 - 1 / (i + 1) ** 2)
#     return x
n = int(input("Введіть значення:  "))
def func(n):
    x = 1
    i = 1

    while i > 0:
        i += 1
        test = abs((1 - 1 / (i + 1) ** 2) - (1 - 1 / ((i-1) + 1) ** 2))
        num = test > 0
        if num:
            break


    if n > num:
        print(test)
    else:
        print("Число не підпадає під умови математичного прикладу")

func(n)