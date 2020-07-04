# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and
# makes a new list of only the first and last
# elements of the given list. For practice,
# write this code inside a function.

import random

def generate_list():
    return random.sample(range(20),random.randint(1,10))

def first_last(li):
    return [li[0],li[-1]]

original=generate_list()
print("Original list : ")
print(original)
new=first_last(original)
print("New list : ")
print(new)
