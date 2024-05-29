
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
