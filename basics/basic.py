"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""

def calculate(number1, number2):
    product = number1 * number2
    if product <=1000:
        return product
    else:
        return number1 + number2


print(calculate(40, 30))

"""
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
"""

previous_number = 0
for i in range(0, 11):
    sum = previous_number + i
    print("current number: ", i, "previous number: ", previous_number, "sum: ", sum)
    previous_number = i


"""
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""

word = input("enter any word: ")

word_length = len(word)
for i in range(0, word_length -1 , 2):
    print("index[", i, "]", word[i])


"""
Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.
"""

def remove_chars(s, n):
    print("original word", s)
    x = s[n:]
    return x

remove_chars("ducatti", 2)

"""
Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False
"""
def same_numbers(numList):
    first_num = numList[0]
    last_num = numList[-1]
    if first_num == last_num:
        return True
    else:
        return False

nums_x = [10, 20, 30, 10]
# print("result is", same_numbers(nums_x))

"""
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
"""

list = [10, 20, 33, 46, 55]
for n in list:
    if n % 5 == 0:
        print(n)

"""
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.
"""
string = "Lucia is a good developer. Lucia is a brave person"
substring = string.count("Lucia")
# print(substring)


"""
print following pattern:
1
22
333
4444
55555
"""

for num in range(10):
    for i in range(num):
        print(num, end= " ")
    print("\n")

"""
check if palindrome number
"""

def palindrome(number):
    print("original number", number)
    original_number = number

    reverse_num = 0
    while number > 0:
        # taking modulo with 10 gives us the last digit of num
        remainder = number % 10
        # appending the last digit of num to reversed_num
        # for this we multiply the reverse_num by 10 and add remainder to it
        reverse_num = (reverse_num * 10) + remainder
        # remove the last digit from num by dividing it by 10
        number = number // 10

    if original_number == reverse_num:
        print("this is a number palindrome")
    else:
          print("this is not a number palindrome")

# palindrome(121)
# palindrome(125)

"""
check if word is palindrome
"""
def is_palindrome(word):
    if word == word[::-1]:
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not a palindrome")

# is_palindrome("racecar")

"""
Create a new list from two list using the following condition:
Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
"""

def merge_list(list1, list2):
    result_list = []
    for n in list1:
        if n % 2 != 0:
            result_list.append(n)
    for n in list2:
        if n % 2 == 0:
                result_list.append(n)

    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
# print(merge_list(list1, list2))
