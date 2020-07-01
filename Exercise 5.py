# Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the
# elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# Extras:

# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python

a=list(map(int,list((input("Enter list one elements separated by spaces : ").split()))))
b=list(map(int,list((input("Enter list two elements separated by spaces : ").split()))))

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

li=list(set(filter(lambda x:x in b,a)))
print(li)
