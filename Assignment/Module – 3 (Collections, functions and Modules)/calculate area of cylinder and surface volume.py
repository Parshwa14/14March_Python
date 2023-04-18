# Write a Python program to calculate surface volume and area of a cylinder

# declaring a varivable named pi with constant value
pi = 22/7
# asking user for entering radius
r = float(input("Enter Radius : "))
# asking user for entering height
h = float(input("Enter Height : "))

# area of cylinder  = 2(pi)(r)(r+h)
print("Surface Area of Cylinder = ",(2*pi*r*(r+h)))

# surface volume of cylinder = (pi)(r*r)(h)
print("Surface Volume of Cylinder = ",(pi*r*r*h))