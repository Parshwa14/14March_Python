# Que : Write a Python program to count the number of lines in a text file.

# for this we will store the lines of the text file in a list

# opening the file in the read mode
file = open("explain this code.txt",'r')

# creating an empty list
mylist = []

# using for loop to add each line as an individual element 
for line in file:
    mylist.append(line)

# now for number of lines we will get the length of the list and print it
print("Number of line in the text file is :",len(mylist))

