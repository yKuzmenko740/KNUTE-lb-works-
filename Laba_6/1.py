class Human:
    name = "Даша"
    gender = "дівчина"
    mood = "чудовий настрій"
    def show(self):
        return f"Мене звати {self.name}. Я - прикольна {self.gender}.У мене чудовий {self.mood}."

a = Human()
print(a.show())