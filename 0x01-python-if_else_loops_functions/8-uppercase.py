#!/usr/bin/python3

# define prototype
def uppercase(str):

    # Convert each string to a list of characters
    chrList = list(str)

    # Convert only lowercase letters to uppercase
    for i in range(len(chrList)):
        asciiCode = ord(chrList[i])

        if 96 < asciiCode < 123:
            chrList[i] = chr(asciiCode - 32)

    uppercaseStr = "".join(chrList)

    print("{}".format(uppercaseStr))
