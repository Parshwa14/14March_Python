db={}

def register(fname,email,password):
    db["name"] = fname
    db["email"] = email
    db["password"] = password

    print("Registration Successful")
    print(db)

def login(email,password):
    if db["email"]==email and db["password"]==password:
       return print( "Welcome, ",db["name"])
    
    else:
        return print("Invalid Email or Password")
status=True
while status:    

    Menu = """
        1) press 1 for Registration
        2) press 2 for login
        3) press 3 for exit

    """

    print(Menu)

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        name = input("Enter Your Name : ")
        email = input("Enter Your Email : ")
        password = input("Enter Your Password : ")

        register(name,email,password)

    elif choice == 2:
        email = input("Enter Your Email ID : ")
        password = input("Enter Your Password : ")

        login(email,password)

    elif choice == 3:
        status = False
        print("Thank you for using our application")