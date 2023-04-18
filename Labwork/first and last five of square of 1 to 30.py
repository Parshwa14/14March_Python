'''Write a Python function to create and print a list where the values are the squares of 
numbers between 1 and 30'''

# creating an empty list
list1=[]

# using for loop from range 1 to 31, we took 31 to include 30
for i in range(1,31):
    #squaring each number from the range
    el=i**2
    # appending the squared number to the empty list
    list1.append(el)

# printing first and last five elements of the square list using list slicing
print("First Five :",list1[:5])
print("Last Five :",list1[-5:])