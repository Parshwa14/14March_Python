# Que : Write python program that user to enter only odd numbers, else will raise an exception.

# using try except method 
try : 
    
    # getting input from the user
    num=int(input("Enter Odd number:"))
    
    # using if statement to find whether the number is even or odd
    if num%2==0:
        
        # if the number is even the value error will be raised
        raise ValueError
except:    
    
    # if the error is raised the message is printed
    print("Provide Provide an ODD Number...")