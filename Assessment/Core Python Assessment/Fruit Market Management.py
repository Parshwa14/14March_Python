import fm_manage
# create an empty dictionary
fruits = {}
# status for menu repeatation 
status = True

# printing the welcome note
print("\n\t\tWelcome To Fruit Market\n\n")

while status:
    # printing menu for choosing our choice from the module
    x=fm_manage.menu()
    print(x)
    
    # creating an empty dictionary specification for fruit quantity and price
    specification = {}
    
    # getting input from the user for choice from the menu
    choice = int(input("Enter your choice : "))
    
    # choice 1 add fruits
    if choice == 1:
        
        # taking fruit name,quantity and price from user 
        fruit_name = input("Enter fruit name : ")
        qty = int(input("Enter qty of fruits : "))
        price = int(input("Enter price : "))

        # adding the name,quantity and price to the respective dictionaries
        specification['qty'] = qty
        specification['price'] = price

        fruits[fruit_name] = specification

    # choice 2 view fruits
    elif choice == 2:
        
        # using for loop to view fruits
        for k in fruits.keys():
            print("-----------------------------------")
            print(f"Fruit Name : {k} ")
            print(f"Fruit Qty :  ",fruits[k]["qty"])
            print(f"Fruit Price :  ",fruits[k]["price"])
            
    # choice 3 purchase fruits
    elif choice == 3:
        for k in fruits.keys():
            print("-----------------------------------")
            print(f"Fruit Name : {k} ")
            print(f"Fruit Price : (for 1 piece) ",fruits[k]["price"])

        fruit_name = input("Enter fruit which you want to purchase : ")
        if fruit_name in fruits.keys():
            qty = int(input("Enter no. qty you want : "))

            price = qty * fruits[fruit_name]['price']
            print("PRICE = ",price)
        
    # choice 4 for exit
    elif choice == 4:
        
        status = False
        break
    
    
    # for asking the user if they want to perform more operation
    user_choice = input("do you want to continue press 'y' for yes and press 'n' for no : ")
    if user_choice == 'n':
        status= False
    else:
        status = True
