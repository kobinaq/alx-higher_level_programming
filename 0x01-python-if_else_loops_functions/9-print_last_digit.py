#!/usr/bin/python3

# define prototype
def print_last_digit(number):

    last_digit = abs(number) % 10
    print(f"{last_digit}", end="")
    return last_digit
