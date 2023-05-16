# Que : Write a Python program to write a list to a file.

# taking filename from user
filename = input("Enter the file name: ")

# taking list content input from the user
data_list = input("Enter the list elements (comma-separated): ").split(',')

# opening the file in read mode
file = open(filename, 'w') 

# using the for loop for writing list elements to the file with a new line at the end of each element
for item in data_list:
    file.write(str(item) + '\n')

# printing the message for file written successfully
print("List written to the file successfully.")

# opening the file in the read mode to print the file content
file = open(filename,'r')
print("File Content : ")
print(file.readlines())

# closing the file
file.close()