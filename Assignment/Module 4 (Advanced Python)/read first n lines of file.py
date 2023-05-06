# Write a Python program to read first n lines of a file.
 
# opening a file in read mode
f = open("what is file function.txt","r")

# Asking user for a number of the lines they want to read from the file
n = int(input("How many lines you want to read? : "))

# using for loop 
for i in range(n):
    print(f.readline())

# closing the file
f.close()