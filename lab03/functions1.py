# 1
def grams_to_ounces(grams):
    return 28.3495231 * grams

# 2
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return "No solution found"

# 4
def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return list(filter(lambda x: is_prime(x), numbers))

# 5
from itertools import permutations

def string_permutations(s):
    perms = permutations(s)
    for perm in perms:
        print(''.join(perm))

# 6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# 8
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

# 9
def sphere_volume(radius):
    return (4/3) * 3.14159 * radius**3

# 10
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# 11
def is_palindrome(word):
    return word == word[::-1]

# 12
def histogram(lst):
    for num in lst:
        print('*' * num)

# 13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)

    guesses_taken = 0
    while guesses_taken < 6:
        print("Take a guess.")
        guess = int(input())

        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
    else:
        print(f"Sorry, {name}. The number I was thinking of was {secret_number}.")
