
"""
Exercise 1: Print First 10 natural numbers using while loop
"""

num = 1
while num <= 10:
    print(num)
    num+=1

"""
Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.
"""

n = int(input("Enter number of rows: "))

for i in range(1, n +1):
    for j in range(1, i+1):
        print(j, end= " ")
    print()


# reverse order for above:

# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print (j, end= " ")
#     print()


"""
Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
"""

num = int(input("enter a number: "))
sum = 0
for i in range(1, num +1):
   sum = sum + i
# print(sum)

"""
Exercise 4: Write a program to print multiplication table of a given number
"""

mul = int(input("enter number: "))

for i in range(1, 11):
   product =  mul * i
print(product)


multiple =  int(input("enter number: "))

for i in range(1, 11):
    print(f"{i} x {multiple} = {i * multiple}")


"""
Exercise 5: Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
"""
num_list = [12, 75, 150, 180, 145, 525, 50]

for i in num_list:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
    

"""
Exercise 6:  
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
"""

counter = 0
number = 75869455
while number != 0:
    number = number // 10 # full division 
    counter = counter + 1 # number of digits in number

print(f"total digits are: {counter}")


"""
print patters 54321, etc... 
"""

for i in range(0, 6):
    for j in range(5-i,0, -1):
        print(j, end= " ")
    print()

"""
Exercise 8: Print list in reverse order using a loop

"""

# l = [10, 20, 30, 40, 50]
# new_l = reversed(l)

# for item in new_l:
    #print(item)

#or
l = [10, 20, 30, 40, 50]
length = len(l) -1 # because index starts at 0
for i in range(length, -1, -1):
    print(l[i])

"""
Exercise 9: Display numbers from -10 to -1 using for loop

"""
for i in range(-10, 0):
    print(i, end = ",")

"""
Exercise 10: Use else block to display a message “Done” after successful execution of for loop
"""

for i in range(0, 5):
    print(i)
else:
    print("done!")

"""
Exercise 11: Write a program to display all prime numbers within a range
Note: A Prime Number is only divisible by 1 and itself. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers
"""

start = int(input("enter start range no: "))
end =  int(input("enter end range no: "))

for i in range(start, end +1):
    for j in range(2, i): # start division by 2 onwards
        if i % j == 0:
            break
    else:
        print(i, end=" ")

"""
Fibonacci sequeence: first two numbers are 0 and 1.
"""
prev = 0
next = 1
for i in range(10):
   print(prev, end = " ")
   res = prev + next
   prev = next
   next = res


"""
Exercise 13: Find the factorial of a given number. Factorial means to multiply all whole numbers from the chosen number down to 1.
"""

# f = 5
# factorial = 1
  
# for i in range(1, f +1):
#      factorial = factorial * i
# print(f"factorial of {f} is, {factorial}")
   
def factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= i + 1
    return factorial

print(factorial(5))

"""
Exercise 14: Reverse a given integer number
"""


# find last digit: modulo %10 = 456 remainder of 7

# add last digit to answer

# remove last digit by substracting last digit and divide by 10: 4567- 7 = 4560 /10 =  456
# update answer by multiplying by 10 and adding last digit: 7 * 10= 70  + 6 = 76
# do it all over again 
x = 4567
answer = 0

while x > 0:
    last_digit = x % 10
    x = x // 10
    answer = (answer * 10) + last_digit
print(f"reverse number: ", answer)



