"""
14. Write Python code that calculates and prints the BMI (body mass index) for a person, given their weight and height as variables.
Display the result as rounded to 2 decimal places. Play around with a variety of different ways to print(), use f-strings, .format(), etc.
Weight: 70kg
Height: 1.75m
BMI: 22.86

BMI = Weight (kg) / Height (m)²
"""

weight = 70
height = 1.75

# bmi = round(70 / 1.75 ** 2, 2)
# print(f"BMI: {bmi}")
# print("BMI: {}", format(bmi))
# print("BMI: %.2f" %bmi)

bmi = 70 / 1.75 ** 2

print(f"BMI: {round(bmi, 2)}")
print(f"BMI: {bmi:.2f}")

print("BMI: {:.2f}".format(bmi))
print("BMI: %.2f" %bmi)



