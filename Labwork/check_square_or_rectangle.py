# QUE : Take values of length and breadth of a rectangle from user and check if it is square or not.

# first we will take two inputs of length and breadth from user
l = int(input("Enter Length : "))
b = int(input("Enter Breadth : "))

# now we will you if-else statement to check if it is square or rectangle

# condition for square
if l==b:
    print("It is a Square")

# the condition in if block is false then else block will executed
else:
    print("It is Rectangle")
