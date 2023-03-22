# Write a Python program to get the Fibonacci series of given range.

n=int(input("Enter a Number : "))
n1=0
n2=1
print("Fibonacci Sequence :",n1,n2,end=" ")         #printing first 2 members
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
