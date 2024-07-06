"""
recursion: a function that calls itself - recurrent function
like a loop
"""
#not best used case - instead use a normal loop
# def countdown(number: int):
#     if number >=0:
#         print(number)
#         countdown(number - 1)

# countdown(100)

#factorial: correct use of recursion with hierarchies of diff problems

def factorial_number(number: int):
    if number < 0:
        print("there are no negative factorials!")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial_number(number - 1)

print(factorial_number(5))

# fibonacci sequence

def fibonacci(number: int):
   if number <= 0:
    print("number must be greater than 0")
    return 0
   elif number == 1:
    return 0
   elif number == 2:
    return 1
   else:
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(3))
