import random

for i in range(1, 6):   # row
    for j in range(1, 6):   # column
        print(f"{i * j:3}", end=" ")    # end means do not skip the line, :3 means 3 spaces
    print()     # skip the line


"""
:3
최소 3자리 공간을 차지하도록 오른쪽 정렬해 출력하라
"""

# strip out unwanted space -> leading or trailing spaces
# some string methods - upper, lower, capitalize, strip, in, palindrome ...

word = "hannah"
if word == word[::-1]:
    print(f"The word {word} is a palindrome")

sentence = "we are getting tired now"
words = sentence.split()
print(words)

total_chars = 0
for word in words:
    total_chars += len(word)

average_length = total_chars / len(words)
print(f"Average word length is {average_length}")


# random
name = "student"
num = random.randint(100, 999)
username = name + "_" + str(num)
print(username)

# datetime strift