class Human:
    def __init__(self, name, gender, mood):
        self.name = name
        self.gender = gender
        self.mood = mood

    def __del__(self):
        print(f"{self.name, self.gender, self.mood}:видалено ")

    def show(self):
        return f"Мене звати {self.name}. Я - прикольна {self.gender}.У мене чудовий {self.mood}."

a = Human("Даша","дівчина","чудовий настрій")
del a