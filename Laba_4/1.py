print(12 > 44)  # False, т.к 12 меньше 44
print(12 == 44)  # False, т.к 12 не равно  44
print(12 < 44)  # True, т.к 12 меньше 44
print("*" * 50)
print(bool("Hi!"))
print(bool(1))
# Функция bool( ) возвращает True в случае если аргумент не равен нулю или если аргумент не пустая последовательность
# и если аргумент содержит текст, и возвращает False если аргумент равен нулю или если аргумент пустая
# последовательность.
print("*" * 50)
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("*" * 50)


def func():
    return 0


if func():
    print("Yes")
else:
    print("No")  # эта строка будет выполнена, т.к func() возвращает 0
