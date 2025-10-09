num = 0

while num < 5:
    print(num)
    num += 1

print("finished")



# While True - NEEDS break. otherwise it becomes an infinite loop
num = 0
while True:
    num = int(input("Please type a number, enter 999 to quit"))
    if num == 999:
        break
    print(f"The number is {num}")
print("Thank you")


while True:
    code = int(input("Please type your pin code"))
    if code == 1234:
        print("Correct!")
        break
    print("Incorrect code. Please try again.")
print("Well done")



attempts = 0
while True:
    code = int(input("Please type you pin code"))
    attempts += 1

    if code == 1234:
        success = True
        break

    if attempts == 3:
        success = False
        break

    print("Incorrect. Try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")



# continue -> goes back to the beginning of the loop
