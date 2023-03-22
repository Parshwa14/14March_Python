# Write a Python program to get the Factorial number of given number.

n = int(input("Enter a number : "))    #taking input from user
factorial =1                           #taking a variable value 1 for further code


#condition for the number '0'
if n==0:                                        
    print("The Factorial of [0] is [ 1 ]")

#condition for the negative numbers
elif n<0:
    print("There cannot be Factorial of Negative Number")

#for positive numbers
else:
    for i in range(1,n+1):                 #using for loop with range to take all the numbers from 1 to n
        factorial = factorial * i                   
    print(f"The Factorial of [{n}] is [ {factorial} ]")
