from functools import reduce
# anonymous function in one line: it takes any no of args followed by an expression that will be returned

add_1 = lambda x, y: x + y 

result = add_1(1, 6)
print(result)

# map and filter functions, lambda is used
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def square(x):
#     return x **2

# squares = list(map(square, my_numbers))
# print(squares)

#or with lambda

squares = list(map(lambda x: x**2, my_numbers))
print(squares)

#filter 
even_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x %2 == 0, even_nums))
print(evens)

#reduce 

nums = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda acc, x: acc + x, nums)
print(sum_of_numbers)

#find max value
# return acc if acc > x, otherwise return x and so on
max_value = reduce(lambda acc, x: acc if acc > x else x, nums)
print(max_value)