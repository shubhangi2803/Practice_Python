# Create a program that asks the user for a number and then prints out
# a list of all the divisors of that number.

number=int(input("Enter a number :"))
li=list(filter(lambda x:number%x==0,[n for n in range(1,number+1)]))
print(li)
