# QUE : Take two int values from user and print greatest among them.

# first we will take two int values A and B from the user

a = int(input("Enter A : "))
b= int(input("Enter B : "))

# now we will use if-else statement to check the greatest value among the two

if a>b:
    print(f"A = {a} is the greater value among A and B")

else:
    print(f"B = {b} is the greatest value among A and B")