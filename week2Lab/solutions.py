import random
import string
import datetime

#1
num = int(input("Enter a number"))
if num == 1945:
    print("The war is over!!")

#2
num = int(input("Enter a number"))
if num < 0:
    print(num * -1)
else:
    print(num)

#3
num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
operation = input("Please enter operation to perform - +, - *, /")
ans = 0
if operation == '+':
    ans = num1 + num2
elif operation == '-':
    ans = num1 - num2
elif operation == '*':
    ans = num1 * num2
elif operation == '/':
    ans = num1 / num2
else:
    print("Invalid operation")
print(f'The answer is {ans}')

#Q4
wage = float(input("Enter hourly wage"))
hours = int(input("Enter hours worked"))
day = input("Enter the day of the week")
if not day == "Sunday":
    pay = wage * hours
else:
    pay = 2 * (wage * hours)
print(pay)

#Q5 - look at better ways to write the code
temp = 23
rain = 'no'
if temp > 20:
    if rain == 'yes':
        print("The weather is warm, wear shorts / T, however bring an umbrella, it may rain")
    else:
        print("A lovely warm day with no rain expected")
elif temp > 10:
    if rain == 'yes':
        print("The chilly, wear a jacket, however bring an umbrella, it may rain")
    else:
        print("A chilly day with no rain expected, wear a jacket")
else:
    if rain == 'yes':
        print("Very cold and bring an umbrella, it may rain")
    else:
        print("A cold day with no rain expected, wear a jacket")

#6
"""
create your own solution and ask CoPilot to check your solution
ask Copilot for other ways of doing the solution
"""
#1
# while num == 0, DONE is being printed every time, it needs to be un-indented, counter is missing

#Q2
grand_total = 0.00
item = input("Enter an item name, if you want to end the app press 'XXX")
while item.upper() != 'XXX':
    price = float(input("Enter the price of the item"))
    quant = int(input("Enter the quantity to buy"))
    total = (price * quant)
    if quant > 10:
        disc = (price * quant) * 0.10
        total -= disc
    print(f'Total for {item} is {total}')
    grand_total += total
    item = input("Enter an item name, if you want to end the app press 'XXX")
print(f'The grand total is {grand_total}')

#Q3
count = 0
money_pot = float(input("Enter the money to put into the pot"))
play = input("Want to role the dice, yes / no - quit while you are ahead")
while money_pot > 0.00:
    if play == 'yes':
        dice = random.randint(1, 7)
        print(f"The dice rolled {dice}")
        if dice == 7:
            money_pot += 4.00
        else:
            money_pot -= 1.00
            count += 1
        print(f'Your money pot is {money_pot}')
    else:
        break
    play = input("Want to role the dice, yes / no - quit while you are ahead")
if money_pot < 0.00:
    print(f'It took {count} tries to break the player')
else:
    print(f'You came out of it with {money_pot} money left')

#Q6
row = 5
while row > 0:
    col = 0
    while col < row:
        print(col, end=" ")
        col += 1
    print()  # move to the next line after each row
    row -= 1

#Q7


# Strings
print(string.ascii_lowercase)
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
print(chars)
password = ""
for _ in range(8):
    password += "".join(random.choice(chars))

print("Generated password:", password)

# some more
event = input("Enter event: ")
date_str = input("Enter date (YYYY-MM-DD): ")
event_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
today = datetime.datetime.now()

days_left = (event_date - today).days

if days_left > 0:
    print(f"{days_left} days left until {event}! Keep working hard!")
elif days_left == 0:
    print(f"Today is {event} day!")
else:
    print(f"{event} was {-days_left} days ago.")

