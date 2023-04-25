"""
File Handling : We can create, read and write in the file using file handling in python programming language.

modes of file handling : 

x - create file
r - read file
w - write file
a - append file


"""
# f = open("test.txt","x") # create a file

# f = open("test.txt","r")
# print(f.read())

# f =  open("test.txt","w")

# name = input("Enter Name : ")
# f.write(name)
# print(name)

# f.close()

# f = open("test.txt","a")

# name = input("Enter Name : ")
# f.write(name)

# f.close()


# # read random line from a file
# f = open("test.txt","r")
# print(f.readline())

# n = int(input("How many lines you want to read? : "))
# f=open("test.txt","r")
# for i in range(n):
#     print(f.readline())

from shutil import copyfile
copyfile("test.txt","test1.txt")

f = open("test1.txt","r")
print(f.read())