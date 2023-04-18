# Define a function that accepts radius and returns the area of a circle.

# defining a variable pi with a constant value 22/7
pi = 22/7

# taking input from user for the radius of the circle
r = float(input("Enter Number :"))

# defining a function areaofcircle with parameter radius
def areaofcircle(radius):
    # area =  pi * (r**2)
    return pi*(radius**2)

# calling function with radius as an argument and storing it in variable area 
area = areaofcircle(r)

# printing the area variable 
print("Area of Circle : ",area) 