# Write a Python program to append text to a file and display the text.

# create and append text into the file
f = open("demo.txt","a")

# writing the text to the file
f.write("Hello world, You are seeing the python code.")

# opening the file in read mode
f = open("demo.txt","r")

# creating a variable to display the text of the file
x = f.read()

# closing the file
f.close()

# displaying the file
print(x)