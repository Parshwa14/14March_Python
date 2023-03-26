# QUE : Python Program to check if the triangle is equilateral, scalene or isosceles.

# first we will ask user to enter the length of all three sides

x = int(input("Enter X : "))
y = int(input("Enter Y : "))
z = int(input("Enter Z : "))


# Equilateral Triangle : Length and Angles of all the sides are same

if x==y==z:
    print("It is Equilateral Triangle")

# Isosceles Triangle : Length and Angles of two opposite sides are same

elif x==y or y==z or z==x:
    print("It is Isoscelese Triangle")

# Scalene Triangle : nothing is same  

else:
    print("It is Scalene Triangle")