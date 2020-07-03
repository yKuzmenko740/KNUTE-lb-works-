class Human:
    def __init__(self, name, gender, mood, cash):
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


a = Human("Даша", "дівчина", "чудовий настрій", int(input()))
a.show()
a.my_cash()
del a