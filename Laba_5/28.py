import random

m = int(input("Введіть кількість стовпців матриці: "))
n = int(input("Введіть кількість рядків матриці: "))
matrix = [[random.randrange(1, 11) for i in range(m)] for j in range(n)]
for i in range(len(matrix)):
    print("\t", matrix[i])
print()


def func(matrix, m, n):
    t = []
    for i in range(m):
        min = matrix[0][i]
        for x in range(n):
            if matrix[x][i] < min:
                min = matrix[x][i]
        t.append(min)
    return tuple(t)


print(func(matrix, m, n))
