import random
# a = []
# b=[]
# for i in range(1,10):
#     a.append(random.randint(0, 100))
# for i in range(1,10):
#     b.append(random.randint(0,100))
# print(a)
# a.sort()
# print(b)
# b.sort()
# print(a)
# print(b)
lst_1 = []
lst_2 = []
n = int(input("Довжина першого списку: "))
m = int(input("Довжина другого списку: "))
for i in range(n):
    lst_1.append(random.randint(-100, 10))
lst_1 = sorted(lst_1)
print(lst_1)
for i in range(m):
    lst_2.append(random.randint(-100, 10))
lst_2 = sorted(lst_2)
print(lst_2)
lst_3 = lst_1 + lst_2
lst_3 = sorted(lst_3)
print(lst_3)
