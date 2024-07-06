# Value and Reference

# data structure with value: unique element
my_int_a = 10
my_int_b = my_int_a
print(my_int_a)
# my_int_b = 20
print(my_int_b)

# data structure with reference: all that are not primitive: list, tuple, dict, set, etc- these inherit their position in memory
my_list_a = [10, 20]
my_list_b = my_list_a # returns same value
my_list_b.append(30)
print(my_list_a)
print(my_list_b) # both return [10, 20, 30]

"""
examples with functions with variables with value and reference
and how these behave anytime they are modified.
"""
# function with data by value

my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# functions with data by reference:



def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)
    print(my_list)
    print(my_list_d)

my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

# how to avoid reference in memory: by slicing, .copy() or deepcopy()

# interchange values
def value(value_a: int, value_b: int) -> tuple:
    temp = value_a # using auxilliary var
    value_a = value_b
    value_b = temp
    return value_a, value_b

int_a = 10
int_b = 20
value_c, value_d = value(int_a, int_b)

print(f"{int_a}, {int_b}")
print(f"{value_c}, {value_d}")

# interchage by ref
def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_list_f = [10, 20]
my_list_g = [30, 40]

my_list_h, my_list_i = ref(my_list_f, my_list_g)
print(f"{my_list_f}, {my_list_g}")
print(f"{my_list_h}, {my_list_i}")
