#!/usr/bin/python3

# Define prototpye
def islower(c):
    
    # convert alphabeth to Ascii code
    asciicode = ord(c)

    # conditinal statements to check if ASCII code 
    # falls within the lowercase number range

    if 92 < asciicode < 123:
        return True
    else:
        return False
