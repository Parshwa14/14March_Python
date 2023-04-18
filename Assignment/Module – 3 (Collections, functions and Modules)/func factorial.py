# Write a Python function to calculate the factorial of a number (a nonnegative integer)

# taking a number from user to find its factorial
n = int(input("Enter a Number : "))


# defining a function named factorial
def factorial():
    # creating a variable ans with initial value of 1 for the final answer
    ans = 1

    # using for loop from 1 to n+1 to go till the n
    for i in range(1,n+1):
        # multiplying ans with i till i=n
        ans *=i

    # returning the final ans
    return ans

# calling the function and storing it in a variable result
result = factorial()

# printing the result variable
print(f"The Factorial of {n} : ",result)