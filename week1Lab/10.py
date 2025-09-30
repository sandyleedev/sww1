"""
10. Write the code that asks the user for their name and age and prints it as follows
(where Jack is the name inputted and age is the age inputted):

Hello Jack, you are 21 years old.
a. Print whether their age is older than 18.
"""

name = input("What is your name? ")
age = int(input("How old are you? "))

statement = "You are older than 18" if age > 18 else "You are NOT older than 18"

print(statement)