'''def greet():                    # function declaration
    print("Hello and Welcome to Functions")             #block of code

greet()                             # function calling
greet()
greet()


'''

'''----------------------------------------------------------------------------'''


'''def sum():          # function declaration

    # block of code
    a = int(input("Enter the Value of A : "))
    b = int(input("Enter the Value of B : "))
    print(a+b)

#function calling
sum()
sum()'''


'''----------------------------------------------------------------------------'''


# function with parameter and no return type
def getdata(id,name,sub):
    print("Student ID : ",id)
    print("Student Name : ",name)
    print("Student Subject : ",sub)

'''
# getdata(509,"Parshwa","Python")             #static

# dynamic
stid = int(input("Enter ID : "))
stnm = input("Enter Name : ")
stsub = input("Enter Subject : ")

getdata(stid,stnm,stsub)'''

n = int(input("How many students data you want to add ? "))

for i in range(n):
    stid = int(input("Enter ID : "))
    stnm = input("Enter Name : ")
    stsub = input("Enter Subject : ")

    getdata(stid,stnm,stsub)