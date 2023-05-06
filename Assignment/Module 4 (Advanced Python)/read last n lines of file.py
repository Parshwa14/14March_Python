# Write a Python program to read last n lines of a file.


# open a file 
f = open("what is file function.txt","r")

# taking a variable to read lines
lines = f.readlines()

# taking n from user for reading number of lines
n = int(input("Enter n for lines : "))

# taking a variable to read specific number of lines
lastlines = lines[-n:]

# printing the lines
print(lastlines)

# closing the file
f.close()