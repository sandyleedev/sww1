# concatenation (appending)
s1 = "hello"
s2 = "world"
new = s1 + s2
print(new)

a = "Apple"
b = a * 5
# c = a * 5.0

print(a)
print(b)


# 6 ways to append a string
# +
print("hello" + "\n" + "world")

# +=
message = "my name is "
message += "Sandy"
print(message)

# .join()
another_message = ".".join(message)
print(another_message)
fruit = ["apples", "pears", "berries"]
result = "/".join(fruit)
result2 = " and ".join(fruit)
print(result)
print(result2)

# f-string
user = "Jay"
print(f"Welcome, {user}!")

# %
print("My name is %s and I am %d years old." %("Sandy", 26))

# .format
num1 = 100
num2 = 300
print('The value of num1 is {} and the value of num2 is {}'.format(num1, num2))
print('{}, {}, {}'.format("a", "b", "c"))
print('{2}, {0}, {1}'.format("a", "b", "c"))
print('{a} {b} {c}'.format(a = 1, b = 2, c = 3))    # replacement fields