# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# 1. Keep the game going until the user types “exit”
# 2. Keep track of how many guesses the user has taken,
#    and when the game ends,print this out.

import random
x=random.randint(1,9)
print("_____Random number generated_____")
count=0
while True:
    guess=int(input("Make a guess of number : "))
    count+=1
    if guess<x:
        print("Guess too low")
    elif guess>x:
        print("Guess too high")
    else:
        print("Exactly right")
        break
    choice=input("Press enter to continue or write 'exit' if you wish to end - ")
    if choice=='exit':
        break
print("_____You took {} guesses_____".format(count))
