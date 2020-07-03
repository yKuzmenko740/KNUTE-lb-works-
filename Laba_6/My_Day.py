import random


class My_Day():
    def __init__(self, num):
        self.num = num

    def morning(self, a):
        if a == 1:
            return " Прокинулась пізніше "
        elif a == 2:
            return " Прокинулась раніше "

    def day(self):
        return " Займаюся программуванням "

    def evening(self):
        return " Вийшла на прогулянку "

    def events(self):
        i = random.randint(1, 3)
        if i == 1:
            return self.morning(i), " Зробила каву ", self.day(), self.evening() + " Зустріла подругу"
        elif i == 2:
            return "Погладила собаку"

        elif i == 3:

            return "Позаймалась спортом"

    def night(self):
        return "Лягла спати"


b = My_Day(0)
