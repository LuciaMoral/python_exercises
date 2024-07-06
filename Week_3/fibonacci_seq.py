class Fibonacci:
    def __init__(self, number):
        self.number = number

    def calculate_sequence(self):
        first = 0
        second = 1
        for i in range(self.number):
            print(first)
            temp = first 
            first = second
            second = temp + second

sequence = Fibonacci(30)
sequence.calculate_sequence()
