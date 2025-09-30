ans = 15 / 4
print(ans)

ans = 17 % 3
print(ans)

ans = 5 ** 3
print(ans)

val1 = 42
val2 = 3.14159
val3 = "Hello World"
print(type(val1), type(val2), type(val3))

#using f-string, try some of the other formatting styles
first = "Adam"
last = "Smith"
print(f"{first} {last} ")

age = 35
current_year = 2025
when = (100 - age) + current_year
print(f"You will be 100 in {when}")

colour = input("What is your favourite colour?")
print(colour)

print(len(colour))

height = "2.453"
ans = float(height) * 2
print(ans)

is_monday = True
is_sunny = False
print(is_monday and is_sunny)
print(is_monday or is_sunny)
print(not is_monday)

x = 12
y = 8
print(x > y)
print(x == y)
print(x <= 25)

name = input("Please enter your name")
age = input("Please enter your age")
print(f"Hello {name}, you are {age} years old.")
print(int(age) > 18)

print("Humpty Dumpty sat on a wall \n"
      "Humpty Dumpty had a GREAT fall\n"
      "All the kings horses and all the kings men\n"
      "Couldn't put Humpty together again!!!")

name = input("What is your name?")
pattern = "!"+name
print(pattern * 2+"!") #try it using f-string much more readable

# Ask for user input
weight = input("Enter your weight in kg: ")
height = input("Enter your height in meters: ")

# Convert to correct types
weight = float(weight)
height = float(height)

# Calculate BMI
bmi = weight / (height ** 2)

# Display results in different print styles
print("Your BMI is", round(bmi, 2))              # simple print
print("Your BMI is {:.2f}".format(bmi))          # format()
print(f"Your BMI is {bmi:.2f}")                  # f-string





