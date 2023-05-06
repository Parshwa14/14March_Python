# Write a Python program to read an entire text file.

# opening a file in read mode
f = open("what is file function.txt","r")

# creating a variable to read file
x = f.read()

# printing the file content stored in the variable x
print(x)

# closing the file
f.close()