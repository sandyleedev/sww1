"""
1. Write a program which asks the user for an integer number.
    The program should print “The war is over!!” if the number is
    exactly 1945, otherwise do nothing.
"""

# num = int(input("Please type a number "))
# if num == 1945:
#     print("The war is over!")


"""
2.  Write a program which asks the user for an integer number. 
    If the number is less than zero, the program should print out the number multiplied by -1.
    Otherwise, the program prints out the number as is. 
    For example, if -9 is inputted then the output should be 9. 
    If 150 is inputted, then the output should be 150. 
"""

# num2 = int(input("Please type a number "))
# if num2 < 0:
#     print(num2 * -1)
# else:
#     print(num2)


"""
3.  Write program that asks the user for 2 numbers and an operation.
    If the operation is add, multiply or subtract, the program should calculate
    and print out the result of the operation with the given numbers. 
    If the user types anything else, the program should print out nothing.
    For example, if the numbers are 4 and 5 and the operation is add, 
    then the output should be as follows:
    
    number 1: 4
    number 2: 5
    operation: add
    4 + 5 = 9
"""
# num3_1 = int(input("First number: "))
# num3_2 = int(input("Second number: "))
# operation = input("Operation: ")
#
# if operation == "add":
#     print(num3_1 + num3_2)
# elif operation == "subtract":
#     print(num3_1 - num3_2)
# elif operation == "multiply":
#     print(num3_1 * num3_2)


"""
4.  Write a program which asks for the hourly wage, hours worked and the day of the week.
    The program should then print out the daily wages, which equal hourly wage multiplied by hours worked,
    except on Sundays when the hourly wage is double. The output could look as follows:
        hourly wage: 8.5
        hours worked: 3
        day of the week: Monday
        daily wages: 25.5 pounds
        
        hourly wage: 12.5
        hours worked: 10
        day of the week: Sunday
        daily wages: 250.0 pounds
"""
# hr_wage = float(input("hourly wage: "))
# hr_worked = float(input("hours worked: "))
# day = input("day: ")
#
# daily_wages = hr_wage * hr_worked
# if day == "Sunday":
#     print(f"daily wages: {daily_wages * 2} pounds")
# else:
#     print(f"daily wages: {daily_wages} pounds")


"""
5.  Write a program which asks for tomorrow’s weather forecast and then suggests weather-appropriate clothing.
    The suggestion should change if the temperature is over 20, 10 or 5 degrees and if there is rain on the way.
    The output could look as follows:
    
    what is the weather forecast for tomorrow?
    temperature: 21
    will it rain (yes / no): no
        wear jeans and a T
    
    what is the weather forecast for tomorrow?
    temperature: 10
    will it rain (yes / no): no
        wear jeans and a T
        a jumper is recommended
    
    what is the weather forecast for tomorrow?
    temperature: 3
    will it rain (yes / no): yes
        wear jeans and a T
        a jumper is recommended
        take a warm coat
        take an umbrella
"""
# temp = int(input("Temperature tomorrow? "))
# rain = True if input("Will it rain? (yes / no) ") == "yes" else False
#
# if rain:
#     print("take an umbrella")
# if temp <= 5:
#     print("take a warm coat")
# if temp <= 10:
#     print("a jumper is recommended")
# print("wear jeans and a T")


"""
6. Write a program to produce a grade calculator. Ask the user
to ender a grade (0 to 100). Print the grade as follows:
    A -> 70+
    B -> 60 to 69
    C -> 50 to 59
    D -> 40 to 49
    Fail-> under 40
"""
# grade = int(input("Enter a grade from 0 to 100 "))
# if grade >= 70:
#     print("A")
# elif grade >= 60:
#     print("B")
# elif grade >= 50:
#     print("C")
# elif grade >= 40:
#     print("D")
# else:
#     print("Fail")
