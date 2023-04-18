# Write a Python function to multiply all the numbers in a list
# taking a list
mylist = [5,4,3,6,7,8]

# defining a function for multiplication with parameter number
def mult(number):

    # taking variable ans with initial value as 1 
    ans = 1

    # using for loop to iterate each element of the list
    for i in number:
        # multiplying ans with i and store it in ans
        ans*=i

    # returnin ans as a final output after all the iterations completed
    return ans

# calling the function with mylist as an argument in it and storing it in a variable result 
result = mult(mylist)


# printing the variable result to get the final ans
print(result)