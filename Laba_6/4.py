class Mammals:
    def __init__(self, apprnc, height, weight, hair_color, eyes_color ):
        self.eyes_color = eyes_color
        self.hair_color = hair_color
        self.weight = weight
        self.apprnc = apprnc
        self.height = height
    def sleep(self):
        print("Я сплю")
    def eat(self):
        print("Я їм")
    def walk(self):
        print("Я йду")

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
            return  f'Баланс = {self.cash}'
        else:
            return "Невірна комманда"
