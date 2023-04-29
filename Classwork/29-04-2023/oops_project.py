# define a class for faculty
class faculty:
    # a blank dictionary
    db = {}

    # inout method for faculty
    def input(self):
        email=input("Enter your email : ")
        password=input("Enter your password : ")        

        
        # storing data in the dictionary db
        self.db[email]=password

    # to display 
    def display(self):
        # display all students
        for k,v in self.db.items():
            print("Email : ",k)
            print("Password : ",v)


# define a class for student
class student:
    # blank dictionary
    db = {}
    


    # input method - which accept from student user
    
    def input(self):
        email=input("Enter your email : ")
        password=input("Enter your password : ")

        # storing data in db
        # here email is key and password is value
        # e.g., parshwa@gmail.com: 98765
        
        self.db[email]=password
    

        # to display 
    def display(self):
        # display all students
        for k,v in self.db.items():
            print("Email : ",k)
            print("Password : ",v)

# object creation of student class
s1 = student()
f1 = faculty()
status = True
while status:

    data = """
            press 1 for student registration
            press 2 for faculty registration
            press 3 for view all students
            press 4 for exit
    """
    print(data)

    user_input = int(input("Enter Your Choice : "))
    if user_input == 1:
        s1.input()
    

    elif user_input == 2:
        f1.input()

    elif user_input == 3:
        s1.display()

    else:
        status = False
    
    choice = input("Do you want to perform more operations ? y/n : ")
    if choice == "n" or choice == "N":
        status = False
        print("Thank you for using our application")

    else : 
        status = True