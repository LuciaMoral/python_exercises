class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meww")

#polymorphism
def print_sound(animal: Animal):
    animal.sound()

my_animal = Animal("animal")
print_sound(my_animal)
my_dog = Dog("dog")
print_sound(my_dog)
# my_animal = Animal("mouse")
# my_animal.sound()
# my_dog = Dog("dog")
# my_dog.sound()

#Extra exercise

class Employer:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)

class Manager(Employer):

    def coordinate_projects(self):
        print(f"{self.name} coordinates all projects")

class ProjectManager(Employer):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} coordinates one project")


class Developer(Employer):
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}" )

    def add(self, employee):
        print("Coders don't manage any employees")

my_manager = Manager(1, "moralDev")
my_manager.coordinate_projects()


project_manager = ProjectManager(2, "pro", "project1")
project_manager.coordinate_project()
programmer = Developer(3, "lili", "Java")
programmer2 = Developer(4, "lujan", "JS")
programmer2.code()
my_manager.add(project_manager)
project_manager.add(programmer)
project_manager.add(programmer2)

my_manager.print_employees()
project_manager.print_employees()
programmer.print_employees()
