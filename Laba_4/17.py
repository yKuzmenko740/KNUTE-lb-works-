def func(x,y,z):
    if x + y < z or x + z < y or y + z < x or x < 0 or y < 0 or z < 0:
        return 0
    return 1

x = 7
y = 5
z = 2
print(func(x,y,z))