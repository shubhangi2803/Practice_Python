# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. 

# Extras:

# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and
#    one number to divide by (check). If check divides evenly into num,
#    tell that to the user. If not, print a different appropriate message.

number=int(input("Enter a number : "))
if number%2==0:
    print("Even number")
    if number%4==0:
        print("Also a multiple of 4 ")
    else:
        print("Not a multiple of 4 ")
else:
    print("Odd number")
    print("Not a multiple of 4 ")


num=int(input("Enter another number : "))
check=int(input("Enter the number to check if above number is multiple of it : "))
if num%check==0:
    print("{} is multiple of {} ".format(num,check))
else:
    print("{} is not a multiple of {} ".format(num,check))
