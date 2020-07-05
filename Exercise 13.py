# Write a program that asks the user how many Fibonnaci numbers to generate
# and then generates them. Take this opportunity to think about how you can
# use functions. Make sure to ask the user to enter the number of numbers in
# the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of
# numbers where the next number in the sequence is the sum of the previous
# two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

terms=int(input("Enter the no. of terms you want to generate : "))
fibo(terms)
print("Fibonacci Series : ")
for i in range(1,terms+1):
    print(fibo(i),end=" ")
