class Integer:
    def __init__(self):
         self.numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
         self.romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
         self.roman_numeral = ""
         self.num = int(input("enter any number: \n"))

    def int_to_roman(self):
         i = 0
         while self.num > 0:
              for _ in range(self.num // self.numbers[i]):
                self.roman_numeral = self.roman_numeral + self.romans[i]
                self.num -= self.numbers[i]
              i += 1
         return self.num

num = Integer()
num.int_to_roman()
