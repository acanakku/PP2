#1

import math

def multiply_list(numbers):
    return math.prod(numbers)

#2
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

#3
def is_palindrome(string):
    return string == string[::-1]

#4
import time
import math

def square_root_with_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

#5
def all_true(elements):
    return all(elements)

