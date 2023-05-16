# Que : Write a Python program to read a file line by line store it into a variable.

# open file in the read mode
file = open("explain this code.txt",'r')

# store file in a variable
data = file.readlines()

# printing the data stored in the variable
print(data)

# closing the file 
file.close()

