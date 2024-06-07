class Roman:

    def __init__(self):
        self.romans = {"I" : 1, "V" : 5, "X": 10, "L" : 50,  "C": 100, "D": 500, "M": 1000 }
        self.roman = input("Enter a Roman number with no more than 4 letters:\n")


    def roman_to_int(self):
        total = 0
        previous = 0
        for i in reversed(self.roman):
            value = self.romans[i]
            if value < previous:
                total -= value
            else:
                total += value
            previous = value
        return total


roman = Roman()
print(roman.roman_to_int())
