import time

a_name = "John"
age = 20

print("My name is", a_name, "and I am", age, "years old")
print("My name is", a_name, "\nand I am", age, "\nyears old")

print("My name is", a_name, "and I am", age, "years old", end=".@@@ ")
print("This is all I have")

print("Printing it all on", end='')
print("one line")
print("Printing it all on", end=' ')
print("one line")
print("Printing it all on", end=', ')
print("one line")

num1, num2 = 50, 500
# using f-string
print(f"num1 is {num1} and num2 is {num2}")

# .format
print("num1 is {} and num2 is {}".format(num1, num2))

# C-style formatting
print("num1 is %d and num2 is %d" %(num1, num2))


# input and output
print("Let's take a look at input and output")
get_number = input("Please enter a number to be inputted: ")
print(f"The number is {get_number} and its type is {type(get_number)}")

# wrap it in an int to convert the string to a number
get_number = int(input("Please enter a number to be inputted: "))
print(f"The number is {get_number} and its type is {type(get_number)}")
print("The id is {}".format(id(get_number)))

name = input("What is your name?")
print("The name is %s. Welcome to the APP" % name)


count_sec = 3
for x in reversed(range(count_sec + 1)):
    if x > 0:
        print(x, end='>>>')
        time.sleep(1)
    else:
        print('Start!')