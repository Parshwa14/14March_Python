# Que : Write a Python program to copy the contents of a file to another file.

# taking source file and destination file name/path from user
source_name = input("Enter filename you want to copy (Source File) : ")
dest_name = input("Enter filename where you want to copy (Destination File) : ")

# opening the source file in read mode
s_file = open(source_name,'r')

# opening the destination file in write mode
d_file = open(dest_name,'w')

# using for loop writing all the lines to the new file(copying all the lines from the file)
for line in s_file:
    d_file.write(line)

# printing the successfull file copying message        
print("File Copied Successfully!!") 

# opening the destination file in the read mode
d_file = open(dest_name,'r')

# printing the copied file content
print(d_file.read()) 
        