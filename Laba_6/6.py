class MY_MONEY:
    def __init__(self, summ, history):
        self.history = history
        self.summ = summ

    def balance(self):
        print(f"Ваш баланс = {self.summ}")
    def history(self):
        print(self.history)

    def fucn(self):

        num = int(input())
        if num < 0 :
            self.history.append(self.summ)
            self.summ+= int(num)
            self.history.append(num)
            self.history.append("-")
            self.history.append(self.summ)
            self.history.append(".")
        else:
            self.history.append(self.summ)
            self.summ += int(num)
            self.history.append('+')
            self.history.append(num)
            self.history.append("+")
            self.history.append(self.summ)
            self.history.append(".")
        return f"Баланс = {self.summ}"

