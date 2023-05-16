# Que : Write a Python program to read a file line by line and store it into a list.

# creating a empty list to store the file data into it
lines = []

# opening the file in the read mode 
file = open("how to define a python class.txt", 'r')

# using for loop to strip the blank space from the end of the lines and then append line into the empty list we have created
for line in file:
    lines.append(line.strip())


# Print the lines stored in the list
for line in lines:
    print(line)


# closing the file
file.close()
