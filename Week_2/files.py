# # reading files
# file = open("text.txt", "r")
# file.read()
# file.close()

# creating files
file = open("greet2.txt", "w")
file.write("Second file created from PY")

# add to file
file = open("greet2.txt", "a")
file.write("Another line added....\n")
file.close()

with open("greet2.txt", "r") as file:
    print(file.name)
    print(file.mode)
    print(file.encoding)
    print(file.read())
