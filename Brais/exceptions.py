# control of errors with exceptions that system already has built-in

try:
    print(10/0) # code that may not work
except Exception as e: # capture the error with a msg
    print(f"there has been an error: {e}")

try:
    my_list = [1, 2, 3]
    print(my_list[4])
except Exception as e:
    print(f"there has been an error: {e}")


class StrTypeError(Exception):
    pass

# extra personalized exceptions

def process_params(params: list):
    if len(params) < 3:
        raise IndexError()
    elif params[1]== 0:
        raise ZeroDivisionError()
    elif type(params[1]) == str:
        raise StrTypeError("second element cannot be a str")

    print(params[2])
    print(params[0]/params[1])
    print(params[2] + 5)

try:
    process_params([1,3, 2])
except IndexError as e:
    print(f"number of elements in list must be bigger than 2 {e}")
except ZeroDivisionError as e:
    print(f"number cannot be divided by 0 {e}")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"there has been an error: {e}")
else:
    print("no errors produced")
finally:
    print("programme ends without stopping") # this line will always be executed.
