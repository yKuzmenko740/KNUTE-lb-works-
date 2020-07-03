import random

n = int(input("Введіть довжину списку: "))
c = int(input("Ліве обмеження: "))
d = int(input("Праве обмеження: "))

lst = []
for i in range(n):
    lst.append(random.randint(-10,10))
print(lst)
def func(lst, c, d):
    cnt = 0
    for i in lst:
        if c <= i <= d:
            cnt +=1
    return cnt

print(func(lst,c,d))

