# creating an empty dictionary
product_menu = {}

# menu for choosing our choice
menu = """
press 1 for product manager
press 2 for customer
press 3 for exit"""


status = True
p_status = True

# while status is true the below block will run
while status:
    # displaying the menu
    print(menu)
    # taking input from user according to menu
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        while p_status:
            spec = {}  # created a dictionary for specifications in the main dictionary
            print("Welcome to Product Manager") 
            # taking product name from user
            product_name =input("Enter the Product Name : ")
            # taking product quantity from user
            qty = int(input("Enter the Quantity : "))            
            # taking product amount from user
            amount = int(input("Enter Amount : "))
            
            # this if block will check product name is in product_menu
            # if yes then it will add in the quantity
            if product_name in product_menu.keys():
                spec["qty"] = product_menu[product_name]["qty"]+qty
                spec["amount"] = amount
            
            # in this block it will add as a fresh entry to the dictionary
            else:
                spec["qty"] = qty
                spec["amount"] = amount

            product_menu[product_name]=spec
            print(product_menu)

            # asking user if they wants to add more product 
            p_choice=input("Do You want to Add more Products (y/n) : ")

            if p_choice == "n":
                p_status = False
    
# if choice entered by user is 2 then this will run
    elif choice == 2:
        print("Customer")

# if choice entered by user is 3 then this will run
    else:
        print("Thank you !")
        # this will stop the program for further operating because status is declared false
        status= False