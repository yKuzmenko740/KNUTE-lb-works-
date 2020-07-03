import math # импортируем библиотеку для работы с числами

while True: # означает что программа будет выполнятся бесконечно
    enteredSymbol = input("Введіть символ: ")
    if enteredSymbol == "exit": # если выполняется этот блок кода,то прогмамма завершается
        print("Завершення...")
        break
    # весь следующий блок кода выполняется если введен один из символов
    elif enteredSymbol == "+":
        x, y = int(input("Введіть першу цифру:")),int(input("Введіть другу цифру:"))
        print(f'{x} {enteredSymbol} {y} = {x+y}') # это formated string(используется для удобного вывода информации)
    elif enteredSymbol == "-":
        x, y = int(input("Введіть першу цифру:")),int(input("Введіть другу цифру:"))
        print(f'{x} {enteredSymbol} {y} = {x-y}')
    elif enteredSymbol == "*":
        x, y = int(input("Введіть першу цифру:")),int(input("Введіть другу цифру:"))
        print(f'{x} {enteredSymbol} {y} = {x*y}')
    elif enteredSymbol == "/":
        x, y = int(input("Введіть першу цифру:")),int(input("Введіть другу цифру:"))
        print(f'{x} {enteredSymbol} {y} = {x/y}')
    elif enteredSymbol == "**":
        x, y = int(input("Введіть першу цифру:")),int(input("Введіть другу цифру:"))
        print(f'{x} {enteredSymbol} {y} = {x**y}')
    elif enteredSymbol == "sqrt":
        x = int(input("Введіть цифру:"))
        print(f'{enteredSymbol} для {x} = {math.sqrt(x)}') # используем библиотеку math для вычисления квадратного кореня
    elif enteredSymbol == "sin":
        x = int(input("Введіть цифру:"))
        print(f'{enteredSymbol} для {x} = {math.sin(x)}')   # используем библиотеку math для вычисления синуса
    elif enteredSymbol == "cos":
        x = int(input("Введіть цифру:"))
        print(f'{enteredSymbol} для {x} = {math.cos(x)}')   # используем библиотеку math для вычисления косинуса
