import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits

print(digits)

potential_password = lowercase + uppercase + digits

print(f"potential_password: {potential_password}")

password = ""
password_length = 8

for i in range(1, password_length + 1):
    r = random.choice(potential_password)
    print(f"index {i}: {r}")
    password += r

print(f"new password is {password}")