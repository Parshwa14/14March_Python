# create class product

class product:


    # constructor 
    def __init__(self):
        self.__mobile=15000  # private mode
        self.laptop=50000

    

    # display method
    def display(self):
        print("Mobile : ",self.__mobile)
        print("Laptop : ",self.laptop)

    # change value through method
    def changeData(self,newmobileprice):
        self.__mobile=newmobileprice

# creating class object
p = product()

# before changing the price
p.display()

# trying to change data without method 
p.__mobile = 35000
p.laptop = 95000
p.display()

# after changing the data
print("\n\nThe price after changing the data")
# calling the changedata method
p.changeData(25000)
# calling method
p.display()