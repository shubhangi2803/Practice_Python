# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.

# Extras:

# 1. Add on to the previous program by asking the user for another number
#    and printing out that many copies of the previous message.

# 2. Print out that many copies of the previous message on separate lines. 

import time

name=input("Enter your name : ")
age=int(input("Enter your age : "))
print("Name : {}".format(name))
print("You will be 100 years old in the year : {}".format(time.localtime()[0]-age+100))
times=int(input("Enter the no. of times you want to print the message : "))
for i in range(times):
    print("{}. You will be 100 years old in the year : {}".format(i+1,time.localtime()[0]-age+100))
