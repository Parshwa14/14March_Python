# displaying the app/program name
print("\t\tWELCOME TO FRUIT MARKET\n")

# creating a function for main menu
def mmenu():
    return print("\t\t1) Manager\n \t\t2) Customer\n")

# creating a function for menu
def menu():
    return print("\t\tFruit Market Manager\n\n \t\t1) Add Fruit Stock\n \t\t2) View Fruit Stock\n \t\t3) Update Fruit Stock")

# calling main menu
mmenu()     
# created a variable role for taking an input from user 
role = int(input("\tSelect Your Role : "))

# for 1 it will take to manager's roles
if role == 1:
    
    # in manager's role there is 3 options
    # showing all 3 option with the help of menu funtion
    menu()

    # making user chose from the menu 
    choice = int(input("\tSelect Your Choice : "))

    # for 1 user can add fruit stock
    if choice == 1:
        print("\n\t\tYou have selected to add fruit stock")

    # for 2 user can view fruit stock
    elif choice == 2:
        print("\n\t\tYou have selected to view fruit stock")
    
    # for 3 user can update fruit stock
    elif choice == 3:
        print("\n\t\tYou have selected to update fruit stock")
    
    # for any other input it will show an error    
    else:
        print("\n\t\tInvalid Choice!")

# for 2 it will take to customer's role
elif role == 2:
    print("\n\t\tYou have select customer role")

# for any other input it will show an error
else:
    print("\n\t\tInvalid Role!!")