def string_literals():
    print("The string literals are:")
    a_sent = 'let us learn Python'
    another_sent = "let us learn Python"
    and_another = '''let us
                        learn \n
                            Python'''
    using_lets = "let\'s learn Python"      # \ escape sequence character
    print(a_sent)
    print(another_sent)
    print(and_another)
    print(using_lets)


def char_literals():
    print("The character literals are:")
    a_char = 'j'
    print(f"type of a_char is {type(a_char)}")
    another_char = "k"
    yet_another = 'P'
    print("print them like this", a_char, "and another", another_char, "the last one is", yet_another)


def number_literals():
    print("The number literals are:")
    a_number = 5
    in_binary = 0b10100        #0b means binary. can also have it in octal(0o24) and hex(0x14)
    floating_point_number = 8.945
    complex_number = 10 + 5j        #real part + imaginary part
    another_complex = 10j
    print(a_number)
    print(in_binary)
    print(floating_point_number)
    print(complex_number)
    print(another_complex)


def boolean_literals():
    #1 is always True and 0 is always False
    a = (1 == True)     # True
    b = (1 == False)    # False

    ans = a + 4         # True (1) + 4
    ans2 = b + 10       # False (0) + 10

    print("a is ", a)
    print("b is ", b)
    print("The first answer is", ans, "and the second answer is", ans2)


def literal_collections():
    print("The literal collections are:")
    #a list
    the_list = [5, 7, "Jane", "Waseem"]
    print(the_list)

    #a tuple
    even_numbers = (2, 4, 6, 8, 10)
    odd_numbers = (1, 3, 5, 7, 9)
    print(even_numbers)
    print(odd_numbers)

    #a dictionary
    student_modules = {'12345':'software workshop 1', '54321':'data algorithms'}
    print(student_modules)


string_literals()
char_literals()
number_literals()
boolean_literals()
literal_collections()


'''
[None]
Absense of a value / null value
NOT False, NOT zero, NOT an empty string/list
'''
special_none = None
print(special_none)

