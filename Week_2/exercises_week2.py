
# 1. calcula el índice de masa corporal a partir de su peso en Kg y altura en metros

weight = float(input("enter our weight in Kg: "))
height = float(input("enter your height in metres: "))

def calculate_body_mass_index():
    body_mass_index = weight / (height * height)
    if body_mass_index <=18.5:
        print(f"your body mass index is: {round(body_mass_index, 1)}. You are underweight.")
    elif body_mass_index >18.5 and body_mass_index <=24.9:
        print(f"your body mass index is:  {round(body_mass_index, 1)}. Your weight in normal.")
    elif body_mass_index >=25 and body_mass_index <=29.9:
        print(f"your body mass index is: {round(body_mass_index, 1)}. Your weight is above average." )
    elif body_mass_index >=30:
        print(f"your body mass index is:  {round(body_mass_index, 1)}. You are overweight.")


calculate_body_mass_index()

# 2. convert Celsius to Fahrenheit and vice versa


def calculate_fahrenheit():
    celsius = int(input("enter temperature in celsius: "))
    celsius_to_fahrenheit = (celsius * 1.8) + 32
    print(f" {celsius}ºC are {round(celsius_to_fahrenheit)}ºF")

def calculate_celsius():
    fahrenheit = int(input("enter temperature in fahrenheit: "))
    fahrenheit_to_celsius = (fahrenheit - 30) / 1.8
    print(f"{fahrenheit}ºF are {round(fahrenheit_to_celsius)}ºC")



while True:

    print("1. convert celsius to fahrenheit")
    print("2. convert fahrenheit to celsius")
    print("3. exit")
    temp = int(input("select an option "))

    if temp == 1:
        calculate_fahrenheit()
    elif temp == 2:
        calculate_celsius()
    elif temp == 3:
        print("exiting...")
        break
    else:
        print("enter a valid number")


def show_contacts(contact_list: dict):
        if len(contact_list) > 0:
            for contact, data in contact_list.items():
                print(f"Contact: {contact}")
                print(f"Phone: {data[0]}")
                print(f"Email: {data[1]}")
        else:
            print("There are no contacts registered")

# 3. contact list: name, phone no and email. Search user info and display

def search_contact(contact_list: dict):
     if len(contact_list) > 0:
          name = input("Enter name: ")
          found_contacts = 0
          for contact, data in contact_list.items():
               if name in contact:
                    print(f"Name: {contact}")
                    print(f"Phone: {data[0]}")
                    print(f"Email: {data[1]}")
                    found_contacts +=1
               if found_contacts == 0:
                print(f"this {contact} was not found.")
               else:
                 print(f"{found_contacts} contact was found")

     else:
        print("There are no contacts registered")

def add_contact(contact_list: dict):
        name = input("Enter name: ")
        if name in contact_list:
            print("this contact already exists")
        else:
            phone = int(input("Enter phone number: "))
            email = input("Enter email address: ")
            contact_list[name] = [phone, email]
            print("Contact added successfully")

my_agenda = {}
while True:

    print("1. Show contacts")
    print("2. Search contact")
    print("3. Add contact")
    print("4. Exit")

    option = int(input("Select an option: "))
    if option == 1:
        show_contacts(my_agenda)
    elif option == 2:
        search_contact(my_agenda)
    elif option == 3:
        add_contact(my_agenda)
    elif option == 4:
        print("Exiting...")
        break
# 4. calculate average of school marks

user_input = float(input("Enter the number of marks you have: "))

sum = 0
i = 1
while(i <= user_input):
    print(f"Enter mark", i )
    mark = float(input())
    sum = sum + mark
    i +=1
average = sum / user_input
print(f"Your average mark is: {round(average, 2)}")

# 6. create discount calculator that calculates final price of a product that the user enters

price = int(input("Enter price of product you wish to purchase: "))

discount = 0
if price <= 50:
   discount = price * 0.10
elif price > 150:
   discount = price * 0.15
elif price > 300:
   discount = price * 0.2

print(f"Final price is {price - discount}")


# 7. verify if 2 words are anagrams:

def is_anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        print(f"{word1} and {word2} are anagrams")
    else:
        print(f"{word1} and {word2} are not anagrams")

is_anagram("roma", "amor")

# 8. random password generator

import random

chars = "abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ10123456789!%$#/().,;-"

length = int(input("Enter length of password: "))

password = ""
for i in range(length):
    next_char = random.choice(chars)
    password += next_char

print(f"Your password is: {password} ")
