'''

A constructor is a special method that is called when object is created.

The Purpose of python constructor is to assing value to the data members within the class when an object is created.

The name of the constructor method is always '__init__'

There are two types of constructor :

1) Default  constructor : A constructor which do not have parameters

2) Parameterized constructor : A constructor which have parameters

'''
'''
class student:

    # parameterized constructor
    def __init__(self,id,name):
        print("Student ID : ",id)
        print("Student Name : ",name)

st = student(509,"Parshwa")'''


'''
class employee:

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print("Employee ID : ",self.id)
        print("EMployee Name  : ",self.name)


e1 = employee(101,"Parshwa")
e2 = employee(102,"Lochan")
e3 = employee(103,"Mann")
e4 = employee(104,"Neel")

e1.display()
e2.display()
e3.display()
e4.display()'''

'''
# default constructor

class default:
    def __init__(self):
        print("This is Default Constructor.")

d = default()'''


'''
# if there is more than one default constructor is in the class then the latest one will be called.
class check:

    def __init__(self):
        print("This is first constructor..")
    def __init__(self):
        print("This is second constructor...")


c = check()
'''

class student:
    count = 0

    def __init__(self):
        student.count = student.count + 1


s1 = student()
s2 = student()
s3 = student()
s4 = student()
s5 = student()
s6 = student()
s7 = student()

print("The Number of Student is : ",student.count)
