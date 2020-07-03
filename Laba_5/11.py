# Конкатенація списків
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b
print(c)
# Конкатенація через extend
a.extend(b)
print(a)

# Функція len()
d = [1, 2, 3, 4]
e = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(len(d))
print(len(e))

# Конструкція if variable in collection
f = [3, 1, 9, 0]
print(f)
# 0 есть в списке f
if 0 in f:
    print("Існує")
else:
    print("Не існує")
