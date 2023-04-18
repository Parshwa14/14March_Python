# Write a Python program to returns sum of all divisors of a number

# taking a number from user
n = int(input("Enter a Number : "))
# declaring sum variable with 0 as initial value 
sum = 0

# using for loop to iterate from 1 to n
for i in range(1,n+1):

    # putting the condition to find divisor of n
    if n%i==0:
        # if the condition is true it will be added to sum variable
        sum+=i

# display the sum of divisor of n
print(f"Sum of Divisors of [{n}] : ",sum)