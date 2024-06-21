#!/usr/bin/python3
# Multiply two numbers

def pow(a, b):

        if (b < 0):
            a = 1 / a
            b = -b

        elif (b == 0):
            return 1

        result = 1
        for _ in range(b):
            result *= a 

        return result
