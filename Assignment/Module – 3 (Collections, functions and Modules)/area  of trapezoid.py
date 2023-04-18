# Write a Python program to calculate the area of a trapezoid

# taking length of base a and b from user 
base_a = float(input("Enter Base A : "))
base_b = float(input("Enter Base B : "))

# taking height of trapezoid from user
height = float(input("Enter Height : "))

# area of trapezoid = (a+b/2)*h
print("Area of Trapezoid : ",((base_a+base_b)/2)*height)