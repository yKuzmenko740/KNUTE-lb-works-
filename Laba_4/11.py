beg = int(input("beg = "))
step = int(input("step = "))
end = int(input("end = "))


for i in range(beg,  end,  step):
    k = i ** 3 + i ** 2 + i - 1
    print(k)
