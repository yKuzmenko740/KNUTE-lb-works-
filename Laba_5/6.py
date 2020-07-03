dict = {1: "Apple",
        2: "Samsung",
        3: "Htc",
        4: "Huawei",
        5: "Xiaomi",
        6: "Nokia",
        7: "Acer",
        8: "Asus",
        9: "Fly",
        10: "Meizu",
        }

for i in dict.keys():
    if i % 2==0:
        dict[i] = "Парне значення"
print(dict)