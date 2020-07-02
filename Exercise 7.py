# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even
# elements of this list in it.

import random

a=random.sample(range(50),random.randint(1,10))
print("List : {}".format(a))

# a=list(map(int,list(input("Enter list elements : ").split())))
print("Even numbers list : {}".format(list(filter(lambda x: x%2==0,a))))
