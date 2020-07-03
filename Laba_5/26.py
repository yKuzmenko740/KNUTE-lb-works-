import random

m = int(input("Введіть кількість стовпців матриці: "))
n = int(input("Введіть кількість рядків матриці: "))
matrix = [[random.randrange(1, 11) for i in range(m)] for j in range(n)]
for i in range(len(matrix)):
    print("\t", matrix[i])
print()
min_lst = []

for i in range(len(matrix)):
    min = matrix[i][0]
    for j in range(len(matrix[i])):
        if matrix[i][j] < min:
            min = matrix[i][j]
    min_lst.append(min)
print("\t", min_lst)