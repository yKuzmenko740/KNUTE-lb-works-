import random

m = int(input("Введіть кількість стовпців матриці: "))
n = int(input("Введіть кількість рядків матриці: "))
matrix = [[random.randrange(1, 11) for i in range(m)] for j in range(n)]
for i in range(len(matrix)):
    print("\t",matrix[i])
print()

matrix_2 = []
for x in range(len(matrix)):
    summa = 0
    for j in range(len(matrix[x])):
        summa += matrix[x][j]
    matrix_2.append(summa)

print("\t", matrix_2)