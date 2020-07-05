# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to
# largest) and another number. The function decides whether
# or not the given number is inside the list and returns
# (then prints) an appropriate boolean.

# Extras:
# Use binary search.

import random

def search(li,n):
    for num in li:
        print("{} traversed".format(num))
        if num>x:
            break
        if x==num:
            return True
    return False

def binary_search(li,n):
    low=0
    high=len(li)-1
    mid=None
    while low<=high:
        mid=(low+high)/2
        if li[mid]>n:
            high=mid
        elif li[mid]<n:
            low=mid
        else:
            return True
    return False

        
    

l=random.sample(range(50),random.randint(20,40))
l.sort()
print("List : {}".format(l))
x=int(input("Enter number to search : "))
p=binary_search(l,x)
p=search(l,x)
if p==True:
    print("{} found in list".format(x))
if p==False:
    print("{} not found !".format(x))
    
