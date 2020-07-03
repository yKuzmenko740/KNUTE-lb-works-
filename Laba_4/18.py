def geron(x, y, z):
    if x + y < z or x + z < y or y + z < x or x < 0 or y < 0 or z < 0:
        return 0
    p = (x + y + z) / 2
    s = (p * (p - x) * (p - y) * (p - z)) ** 0.5
    return f"Площа трикутника  = {s} см**2"



print(geron(6, 5, 2))
