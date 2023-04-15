'''Write a Python program to generate and print a list of first and last 5 elements 
where the values are square of numbers between 1 and 30.'''

# first we will take an empty list to add elemenets
sqlist = []

# using for loop to itereate between the given range
for i in range(1,31):
    i = i**2        #squaring each number from the range and storing in i
    sqlist.append(i)    #appending to the list 

# using slicing of list for first five and last five elements
print("First Five : ",sqlist[:5])
print("Last Five : ",sqlist[-5:])