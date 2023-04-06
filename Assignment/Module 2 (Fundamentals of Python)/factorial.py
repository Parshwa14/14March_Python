# Write a Python program to get the Factorial number of given number.


#taking input from user
n = int(input("Enter a number : "))   

#taking a variable named  factorial's value 1 for further code 
factorial =1                           


#condition if the entered number is '0'
if n==0:                                        
    print("The Factorial of [0] is [ 1 ]")

#condition if the entered number is negative
elif n<0:
    print("There cannot be Factorial of Negative Number")

#condition for positive numbers
else:
    #using for loop with range to take all the numbers from 1 to n
    for i in range(1,n+1):                 #here taking n+1 so the n can be considered
        
        #we are multiplying factorial with i where i starts with 1 and ends with n
        #so we can satisfy the formula for factorial
        factorial = factorial * i                   


        #printing the final answer
    print(f"The Factorial of [{n}] is [ {factorial} ]")
