"""
15. Your friend is working on an app for jobseekers.
She sends you this bit of code (see code in jobseekers.py).
The code is almost correct, please fix the code so that it looks as follows:

    my name is Henry Jones, I am 20 years old
    my skills are
    - python (beginner)
    - java (veteran) - programming (semiprofessional)
    I am looking for a job with a salary of 2000-3000 pounds per
    month

"""

name = "Henry Jones"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is ", name, " , I am ", age, "years old")
print("my skills are")
print("- ", skill1, " (", level1, ")")
print("- ", skill2, " (", level2, ")", end=" ")
print("- ", skill3, " (", level3, " )")
print("I am looking for a job with a salary of", lower, "-", upper, "pounds per month")