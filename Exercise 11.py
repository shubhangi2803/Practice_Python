# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.)
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions.

def isprime(num=-1):
    li=list(filter(lambda x:num%x==0,[n for n in range(1,num+1)]))
    if len(li)==2:
        print("Prime number")
    else:
        print("Not a prime number")

number=int(input("Enter a number :"))
isprime(number)
isprime()
