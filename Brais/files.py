import os

# file_name = "Lucia.txt"

# with open(file_name, "w") as file:
#     file.write("Lucia Moral\n")
#     file.write("45\n")
#     file.write("Python")

# with open(file_name, "r") as file:
#     print(file.read())


# os.remove(file_name)

# extra

file_name = "attachment.txt"
open(file_name, "a") # file already exists

while True:
    print("1. Add product")
    print("2. Consult product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Calculate sales total")
    print("6. Calculater sales per product")
    print("7. Consult all products")
    print("7. Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        with open(file_name, "a") as f:
            f.write(f"{name}, {quantity}, {price}\n")
    elif option == 2:
        name = input("Enter name of product: ")
        with open(file_name, "r") as f:
            for line in f.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    elif option == 3:
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        with open(file_name, "r") as f:
            lines = f.readlines()
        with open(file_name, "w") as f:
            for line in lines:
                if line.split(", ")[0] == name:
                    f.write(f"{name}, {quantity}, {price}\n")
                else:
                    f.write(line)
    elif option == 4:
        name = input("Enter name of product you wish to delete: ")
        with open(file_name, "r") as f:
            lines = f.readlines()
        with open(file_name, "w") as f:
            for line in lines:
                if line.split(", ")[0] != name:
                    f.write(line)
    elif option == 5:
        total = 0
        with open(file_name, "r") as f:
            for line in f.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total = quantity * price
            print(total)
    elif option == 6:
        product = input("enter name of product: ")
        total = 0
        with open(file_name, "r") as f:
            components = line.split(", ")
            for line in f.readlines():
                components = line.split(", ")
                if components[0] == product:
                    quantity = int(components[1])
                    price = float(components[2])
                    total = quantity * price
                    break
    elif option == 7:
        with open(file_name, "r") as f:
            print(f.read())
    elif option == 8:
        os.remove(file_name)
        break
