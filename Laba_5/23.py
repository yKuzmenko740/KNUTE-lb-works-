import random
m = int(input("Введіть кількість стовпців матриці: "))
n = int(input("Введіть кількість рядків матриці: "))
matrix = [[random.randrange(1, 11) for i in range(m)] for j in range(n)]
for line in matrix:
    print(line)
def diag(matrix):
    d = [matrix[i][i] for i in range(len(matrix))]
    for i in d:
        if i < 0 :
            return "Від'ємні числа існують!"
    return "Від'ємні числа не існують"
print(diag(matrix))





