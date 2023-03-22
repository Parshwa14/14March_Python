# Write a Python program to check if a number is positive, negative or
# zero.

n = int(input("Enter a Number : "))   #taking input from user

if n<0:                            #condition for negative number
    print("The Number is Negative")

elif n>0:                           #condition for positive number
    print("The Number is Positive")

elif n==0:                          #condition for zero
    print("The Number is Zero")

else:
    print("Invalid Input...")
