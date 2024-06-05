class Number:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        if self.number % 2 == 0:
            print(f"{self.number} is even")
        else:
            print(f"{self.number} is odd")


num = Number(4)
num.is_even()
