# creating a class circle
class circle:
    r:float
    a:float
    p:float

    # creaing method for getting radius from user
    def getData(self):
        self.r = float(input("Enter Radius of Circle : "))
    
    # creating method for area
    def areaCircle(self):
        self.a = (22/7)*(self.r**2)

    # creating method for perimeter
    def perimeter(self):
        self.p = 2*(22/7)*(self.r) 

    # creating method for displaying data
    def displayData(self):
        print("Area of Circle : ",self.a)
        print("Perimeter of Circle : ",self.p)

# creating object
cir = circle()

# calling the methods
cir.getData()
cir.areaCircle()
cir.perimeter()
cir.displayData()