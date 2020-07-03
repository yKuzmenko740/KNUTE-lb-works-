import random

num = int(input("Введіть кількість чисел для порівняння: "))


def max(num):
    nums = [random.randint(1, 100) for i in range(num)]
    print(nums)

    max = nums[0]

    for i in range(num):
        if nums[i] > max:
            max = nums[i]

    return f"Максимальне значення = {max}"

print(max(num))
