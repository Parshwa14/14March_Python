# Write a Python function to find the maximum of three numbers

# declaring a function named max number for finding the max among three
def maxnum():
    
    # taking three numbers from user 
    n1 = int((input("Enter First Number : ")))
    n2 = int((input("Enter Second Number : ")))
    n3 = int((input("Enter Third Number : ")))

    # using if else statements to fulfil the condition
    if n1>n2 and n1>n3:  # for n1 is greater
            print((f"The Max Number from all three is {n1}"))
        
    elif n2>n3:          # for n2 is greater
        print((f"The Max Number from all three is {n2}"))

    elif n3>n2:          # for n3 is greater
        print((f"The Max Number from all three is {n3}"))
    
    else:       # for all the condition false this will be displayed
        print("All are Equal!")

#calling the function
maxnum()