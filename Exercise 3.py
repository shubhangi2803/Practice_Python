# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list
# that are less than 5.

# Extras:

# 1. Instead of printing the elements one by one, make a new list
# that has all the elements less than 5 from this list in it and
# print out this new list.
# Write this in one line of Python.

# 2. Ask the user for a number and return a list that contains only
# elements from the original list a that are smaller than that number
# given by the user.

x=input("Enter space separated numbers to form a list : ")
li=list(map(int,x.split()))
print("List : {}".format(li))
print("Numbers less than 5 : ")

##for num in li:
##    if num<5:
##        print(num)

li2=list(filter(lambda x:x<5,li))
print(li2)

num=int(input("Enter a number to have a list with numbers less than that number : "))
li3=list(filter(lambda x:x<num,li))
print(li3)
