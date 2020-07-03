class Mammals:
    def __init__(self, apprnc, height, weight, hair_color, eyes_color):
        self.eyes_color = eyes_color
        self.hair_color = hair_color
        self.weight = weight
        self.apprnc = apprnc
        self.height = height

    def sleep(self):
        return "Я сплю"

    def eat(self):
        return "Я їм"

    def walk(self):
        return "Я йду"


class Human(Mammals):
    def __init__(self, name, gender, mood, cash, apprnc, height, weight, hair_color, eyes_color):
        super().__init__(apprnc, height, weight, hair_color, eyes_color)
        self.name = name
        self.gender = gender
        self.mood = mood
        self.cash = cash

    def __del__(self):
        print(f"{self.name, self.gender, self.mood}:видалено ")

    def show(self):
        return f"Мене звати {self.name}. Я - прикольна {self.gender}.У мене чудовий {self.mood}."

    def my_cash(self):
        command = input("Введіть: 'Поповнення', 'Оплата' чи 'Баланс': ")
        if command == 'Поповнення':
            num = int(input("Введіть сумму: "))
            return f'Баланс = {self.cash - num}'
        elif command == 'Оплата':
            num = int(input("Введіть сумму: "))
            return f'Баланс = {self.cash - num}'
        elif command == 'Баланс':
            return f'Баланс = {self.cash}'
        else:
            return "Невірна комманда"


class Human_2(Mammals):
    def __init__(self, name, gender, mood, cash, apprnc, height, weight, hair_color, eyes_color):
        super().__init__(apprnc, height, weight, hair_color, eyes_color)
        self.name = name
        self.gender = gender
        self.mood = mood
        self.cash = cash

    def human_sleep(self):
        sleep = super().sleep()
        h_s = sleep + "Мене розбудила моя собака,їй потрібно вийти на прогулянку"
        return h_s

    def human_eat(self):
        eat = super().eat()
        h_eat = eat + "Потрібно і собаці дати їжі"
        return h_eat

    def human_walk(self):
        walk = super().walk()
        h_walk = walk + "Повертаюсь дододу,тому що згадала,що забула гаманець"
        return h_walk


    def show(self):
        return f"Мене звати {self.name}. Я - прикольна {self.gender}.У мене чудовий {self.mood}."

    def my_cash(self):
        command = input("Введіть: 'Поповнення', 'Оплата' чи 'Баланс': ")
        if command == 'Поповнення':
            num = int(input("Введіть сумму: "))
            return f'Баланс = {self.cash - num}'
        elif command == 'Оплата':
            num = int(input("Введіть сумму: "))
            return f'Баланс = {self.cash - num}'
        elif command == 'Баланс':
            return f'Баланс = {self.cash}'
        else:
            return "Невірна комманда"
