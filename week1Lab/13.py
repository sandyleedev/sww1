"""
13. Fix this code so that the whole calculation, complete with the result is printed on a single line.
Do not change the number of print commands.
    print(10)
    print(“ + “)
    print(8)
    print(“ – “)
    print(5)
    print(“ = “)
    print( 10 + 8 – 5)
"""


def printWithoutNewLine(x) :
    print(x, end='')

printWithoutNewLine(10)
printWithoutNewLine("+")
printWithoutNewLine(8)
printWithoutNewLine("-")
printWithoutNewLine(5)
printWithoutNewLine("=")
printWithoutNewLine("10 + 8 – 5")