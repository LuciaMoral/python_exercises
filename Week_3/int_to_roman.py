class Integer:
    def __init__(self):
        self.num = int(input("enter any number: \n"))

    def int_to_roman(self):
        roman_numeral = ""
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12

        while self.num:
            div = self.num // numbers[i]
            self.num %= numbers[i]

            while div:
              roman_numeral += romans[i]
              div -= 1
            i -= 1
        return roman_numeral

num = Integer()
print(num.int_to_roman())
