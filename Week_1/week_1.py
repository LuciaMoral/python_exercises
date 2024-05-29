# problema 1: crear un programa que genere todas la tablas de multiplicar del 1 al 10

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{i} x {num} = {i * num}")

# problema 2: crear un programa que a partir de un nº sume el total de su secuencia, p. ej: si es 6 sería 1 + 2 + 3 + 4 + 5 +6, total 21.

number = int(input("enter a number: "))
result = 0

for i in range(1, number + 1):
    result+=i
print(f"the sum of 1 to {number} is {result} ")


# problema 3: crear un programa que en una lista tenga los nº pares del 1 al 100

print([i for i in range(1, 101) if i % 2 == 0])

# problema 4

user_input = input("enter your password: ")
password = "pythonista"

if password == user_input:
    print(" Correct password")
else:
    print("Wrong password")

# problema 5: crea un programa que calcule si dado un año es bisiesto o no.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap-year")
else:
    print(f"{year} is a not leap-year")
