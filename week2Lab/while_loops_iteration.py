import random
from datetime import datetime, timedelta

"""
1. This program has some syntactic issues, fix them so that the
output is correct:

num = int(input(“Enter a number:”)
while num = 0:
 print(num)
 print(“DONE!!!”)

Output:
Enter a number:5
5
4
3
2
1
DONE!!!
"""

# num = int(input("Enter a number: "))
#
# while num > 0:
#  print(num)
#  num -= 1
#
# print("DONE!!!")


"""
2.  You have been tasked with developing a small shop “print a receipt” for items bought.
    The shopkeeper enters the item name, quantity and price of each item.
    Your program should:
    
    a. Use a loop to repeat the input and calculation until no more items are to be entered.
    b. Calculate the total price for each item.
    c. If the quantity is more than 10 then apply a 10% discount to the total price.
    d. Print each item’s details and the total.
    e. Accumulate each total to show a grand total at the end. To end the application, enter XXX.
    
    Enter item: Apples
    Enter quantity: 5
    Enter unit price: 0.50
    Total for Apples: £2.50
    
    Enter item: Milk
    Enter quantity: 12
    Enter unit price: 2.50
    Total for Milk: £27.00 (10% discount applied)
    
    Enter item: Bread
    Enter quantity: 2
    Enter unit price: 1.45
    Total for Bread: £2.90
    
    Grand total: £32.40
"""
# grand_total = 0
#
# while True:
#     enter_item = input("Enter item: ")
#     if enter_item == "XXX":
#         break
#     enter_quantity = int(input("Enter quantity: "))
#     enter_unit_price = float(input("Enter unit price: "))
#     print(f"""
#         Enter item: {enter_item}
#         Enter quantity: {enter_quantity}
#         Enter unit price: {enter_unit_price:.2f}
#     """)
#     total = enter_quantity * enter_unit_price
#     if enter_quantity > 10:
#         total = total * 0.9
#         print(f"Total for {enter_item}: £{total:.2f}")
#     else:
#         print(f"Total for {enter_item}: £{total:.2f}")
#     grand_total += total
#
#
# if enter_item != "XXX":
#     print(f"Grand total: £{grand_total:.2f}")


"""
3.  In the game of Lucky Sevens, the player rolls a pair of dice.
    If the dots add up to 7, the player wins £4,
    otherwise the player loses £1.
    You need to write a program that should take as input the amount of money that the player wants to put
    into the pot and ask the user if they want to play – yes / no - quite while they are ahead. 
    Play the game until the pot is empty or they don’t want to play.
    At that point, the program should print the number of rolls it took to break the player,
    or print the maximum amount of money in the pot.
"""

# rolls = 0
# money = float(input("enter the money you want to put in the pot"))
#
# while money > 0:
#     res = input("Do you want to play the game? ")
#     if res == "no":
#         break
#     else:
#         dice1 = random.randint(1, 7)
#         dice2 = random.randint(1, 7)
#         print(f"dice1: {dice1}, dice2: {dice2}")
#
#         if dice1 + dice2 == 7:
#             money += 4
#         else:
#             money -= 1
#         rolls += 1
#     print(f"money pot : {money}")
#
# if money <= 0:
#     print(f"The number of rolls took to break you: {rolls}")
# else:
#     print(f"You have {money} left in your pot.")


"""
4. Create a math game for small children to practise their basic maths.
    Question 1: What is 9 + 2?
    Your answer: 11
    Correct!!
    
    Question 1: What is 5 + 6?
    Your answer: 15
    Inorrect. The correct answer was 11
    
    (and so on, do this 10 times and then print
    You got 9 out of 10 correct (as an example)
    
    Hint: play around with the game, include other elements. 
"""
# count = 5
# index = 1
# correct = 0
# while count > 0:
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     res = int(input(f"Question {index}. What is {num1} + {num2}? "))
#     if res == (num1 + num2):
#         print("Correct!!")
#         correct += 1
#     else:
#         print(f"Incorrect. The correct answer was {num1 + num2}")
#
#     count -= 1
#     index += 1
#
# print(f"Well done! You got {correct} out of {count}")


"""
5. Make use of a nested while loop to achieve the following
output of building a pyramid of numbers:
    0 1 2 3 4
    0 1 2 3
    0 1 2
    0 1
    0
"""
# num = int(input("Enter the number: "))
# while num >= 0:
#     num2 = num
#     while num2 >= 0:
#         print(num - num2, end=" ")
#         num2 -= 1
#     num -= 1
#     print("")


"""
6. Create a mini food delivery app (console simulation),
include the following features as part of your code:

    a.  Login simulation, create a username = “student” and a password = “python4Ever”
    b.  Ask the user to enter their username/password
    c.  verify if it is valid (it should match what is in “a”)
    d.  ask the user the choose a delivery time (1 – standard 30- 40min, 2 Express - less than 30min)
    e.  if the delivery time is 1, then there is no fee, otherwise express means a fee of 3.50
        if they don’t choose the correct choice then a message must be displayed.
    f.  print the delivery time chosen and the fee
    g.  ask the user to enter the order total
    h.  if the total is less than £20 then print that they can use contactless payment,
        otherwise they need to use a pin
    i.  ask them to enter the pin, if the pin is “12345” then this is correct otherwise it is incorrect
    j.  print that the order has been place successfully
    k.  what the delivery time will be
    l.  ask them to rate the service
    m.  5 to 1, if they enter 5 then print a message
            *** thank you, you are awesome,
        a rating less than 5 but at least 3, print
            – thank you for your feedback we’ll keep improving,
        lastly sorry you are unhappy we will be in contact!!
"""
def delivery_app():
    username = "student"
    password = "python4Ever"
    pin = "12345"
    login_attempt = 3
    pin_attempt = 3
    delivery_fee = 0

    # is_valid = False
    # while not is_valid:
    #     if login_attempt < 1:
    #         print("Too many login attempts. Sorry.")
    #         return
    #
    #     username_input = input("Enter your username: ")
    #     password_input = input("Enter your password: ")
    #     if username == username_input and password == password_input:
    #         is_valid = True
    #         print("Valid User.")
    #     else:
    #         print("Incorrect.")
    #         login_attempt -= 1

    # if the time option is neither 1 nor 2
    while True:
        try:
            time_option = int(input("""Choose a delivery time
                                    1 - standard 30-40 min
                                    2 - express less than 30 min
            """))
            if time_option == 1 or time_option == 2:
                break
            print("Invalid input. Please enter 1 or 2")
        except ValueError:
            print("Invalid input. Please enter 1 or 2")

    if time_option == 2:
        delivery_fee += 3.50

    print(f"Thank you. Your delivery fee is {delivery_fee} pounds.")
    order_fee = float(input("Please enter your order total fee - "))
    if order_fee < 20:
        print("You can use a contactless payment.")
    else:
        print("You need to use a pin")

        while pin_attempt > 0:
            pin_input = input("Please enter the pin code")
            if pin_input == pin:
                print("Correct pin. Your order has been place successfully.")
                break
            else:
                print("Incorrect pin. Please try again.")
            pin_attempt -= 1

        if pin_attempt == 0:
            print("Too many pin attempts. Sorry.")
            return

    delivery_time = "30-40 mins" if time_option == 1 else "less than 30 mins"
    print(f"You will get your food in {delivery_time}")

    now = datetime.now()
    eta1 = now + timedelta(minutes=30)
    eta2 = now + timedelta(minutes=40)
    format_string = "%H:%M"

    print(f"Estimate Delivery time is {eta1.strftime(format_string)} - {eta2.strftime(format_string)}")


delivery_app()