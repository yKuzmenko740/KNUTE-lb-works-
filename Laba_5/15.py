import random

lst = []
n = int(input("Довжина списку: "))
for i in range(n):
    lst.append(random.randint(0, 10))
print(lst)


def double(a):
    zero_double = set(a)
    if len(zero_double) == len(a):
        return False
    else:
        return True


print(double(lst))
