# Task : write a program to append the student ID, student name,student subject in one file.

f = open("studentinfo.txt","a")
name = input("Enter Student Name : ")
sid = int(input("Enter Student ID : "))
sub = input("Enter Student Subject : ")

f.write(name)
f.write(str(sid))
f.write(sub)

print(f"Student Name : {name}")
print(f"Student ID : {sid}")
print(f"Student Subject : {sub}")

f.close()
