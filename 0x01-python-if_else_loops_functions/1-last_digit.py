#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_number = number_str[-1]

last_number = int(last_number)

if last_number > 5:
    print(f"Last digit of {number} is {last_number} and is greater than 5")
elif last_number == 0:
    print(f"Last digit of {number} is {last_number} and is 0")
else:
    print(f"Last digit of {number} is {last_number} and is less than 6 and not 0")
