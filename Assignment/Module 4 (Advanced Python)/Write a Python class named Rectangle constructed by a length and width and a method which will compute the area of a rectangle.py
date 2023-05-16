# Que :  Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

# creating a class rectangle

class rectangle:
    l : float
    w : float
    a : float

    # creating a method for getting input
    def getdata(self):
        self.l=float(input("Enter Length  : "))
        self.w=float(input("Enter Width : "))
        self.a = self.l * self.w
        
    # creating a method for displaying the output
    def area(self):
        print("Area of Rectangle = ",self.a,"sq. mtr")
    
# creating object
rect = rectangle()

# calling the methods
rect.getdata()
rect.area()