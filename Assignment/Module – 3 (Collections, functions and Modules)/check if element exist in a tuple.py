# Write a Python program to check whether an element exists within a tuple.

# creating a tuple
mytup = (1,2,3,4,5)

# getting input from user to check 
element = int(input("Enter element to check : "))

# using conditional statement to check if element exist in tuple or not
if element in mytup:
    print(f"{element} is in Tuple")

else: 
    print(f"{element} is not in Tuple")