# Write a python program to sum of the first n positive integers.

# taking input from user 
n = int(input("Enter a Number for sum : "))

# taking a variable for sum valued 0
sum = 0

# using for loop to run from 1 to n (took n+1 in range so n can be included)
for i in range(n+1):

    # adding i into the sum every time the loop runs
    sum+=i

# printing the final sum 
print(sum)