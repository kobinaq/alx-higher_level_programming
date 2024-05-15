#!/usr/bin/python3

# define prototype
def uppercase(str):

    # Convert each string to a list of characters
    chrList = list(str)

    # Convert only lowercase letters to uppercase
    for i in range(len(chrList)):
        chrList = ord(chrList[i])
        if 96 < i < 123:
            chrList[i] -= 32

    print(''.join(chr(chrList)))


