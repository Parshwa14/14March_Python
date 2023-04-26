import fm_manage
# create an empty dictionary
fruit_list = {}
# status for main menu repeatation and f_status for manager menu repeatation
status = True
f_status = True

# printing the welcome note
print("\n\t\tWelcome To Fruit Market\n\n")

while status:
    # printing main menu for choosing our choice from the module
    x=fm_manage.main_menu()
    print(x)
    
    # using role variable to select the role manager or customer 
    role = int(input("\tSelect Your Role : "))

    # for the manager section
    if role == 1:

        # printing the manager menu from the module
        y=fm_manage.menu()
        
        # f_status with while to repeat the fruit market manager menu
        while f_status:
            print(y)

            # choice variable for selecting from add,view,update
            choice = int(input("\tEnter Your Choice : "))
            
            #creating a dictionary in the main dictionary
            spec={}
        
            # for adding the fruit stock
            if choice == 1 :                                
                fruit_name=input("Enter Fruit Name : ")         # asking for fruit name
                fruit_qty = int(input("Enter Fruit Quantity (in kgs): "))           # asking for quantity of fruit
                amount = int(input("Enter Total Amount : "))            # asking for the total amount (amount per kg x quantity)
                
                # adding fruit stock to the dictionary 
                spec["fruit_qty"]=fruit_qty
                spec["amount"]=amount
                fruit_list[fruit_name]=spec

                # showing message after adding the stock successfully 
                print("Successfully added fruit stock")
                
            # for viewing the fruit stock
            elif choice == 2 :
                print(fruit_list)
            
            # for updating the fruit stock
            elif choice == 3 :

                # asking user for the fruit name,quantity and price
                fruit_name=input("Enter Fruit Name : ")
                fruit_qty = int(input("Enter Fruit Quantity (in kgs): "))
                # amount = int(input("Enter Total Amount : "))
                
                # if the fruit name is already in the dictionary
                if fruit_name in fruit_list.keys():
                    
                    # updating the quantity and price
                    spec["fruit_qty"] = fruit_list[fruit_name]["fruit_qty"] + fruit_qty
                    spec["amount"] = amount

                    # showing message for successful updation 
                    print("Successfully updated fruit stock")
            
            else:
                print("Invalid Choice !!!")

            # for the while loop in the fruit menu 
            f_choice =input("Do you want to add or view or update stock ? y/n : ")
            if f_choice == "n" or f_choice == "N":
                f_status = False

    # the customer section 
    elif role == 2:
        print("\t\t :: Buy Fresh Fruits Here :: ")
        
    # for exit using the status variable and declaring it False to exit the loop and program
    elif role == 3:
        print("Thank you for comming to Out Store!!")
        status = False    
    
    # for invalid input 
    else:
        print("Invalid Choice !!!")
        