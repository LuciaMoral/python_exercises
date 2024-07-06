class Programmer:

    surname: str = None
    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def printer(self):
        print(f"name: {self.name} surname: {self.surname} - age: {self.age} - languages: {self.languages}")

# leo = Programmer("Leo", 34, ["Python", "JS"])
# print(leo)
# leo.surname = "Smith"
# leo.printer()

#Extra:

class Stack:

    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def delete(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
           print(item)

# my_stack = Stack()

# my_stack.add("Python")
# my_stack.add("JS")
# my_stack.add(3)
# print(my_stack.count())
# my_stack.print()

#FIFO
class Queue:

    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def delete(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def print(self):
        for item in self.queue:
            print(item)


my_queue = Queue()
my_queue.add("1")
my_queue.add("2")
my_queue.add("3")
print(my_queue.count())
my_queue.print()
my_queue.delete()
my_queue.delete()
my_queue.delete()

my_queue.delete()

print(my_queue.delete())
my_queue.print()
