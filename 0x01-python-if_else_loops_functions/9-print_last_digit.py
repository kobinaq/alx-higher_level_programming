#!/usr/bin/python3

# define prototype
def print_last_digit(number):
    if number > 0:
        return number % 10
    elif number == 0:
        return 0
    else:
        return -(-number % 10)
