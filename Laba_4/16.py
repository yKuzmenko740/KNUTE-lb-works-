x= [i for i in range(1,11)]
y= [y for y in range(4,7)]
dot_x=int(input("Введіть x: "))
dot_y=int(input("Введіть y: "))


def func(x,y,dot_x,dot_y):
    if dot_x in x and dot_y in y:
        return "Ці точки належать прямокутній області"
    else:
        return "Ці точки не належать прямокутній області"

print(func(x,y,dot_x,dot_y))