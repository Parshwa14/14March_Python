# creating a class
class Government:
    pm:str
    hm:str
    pres:str

    #creating a method for input
    def inputData(self):
        self.pm=input("Who is the Prime Minister of India ? :")
        self.pres = input("Who is the President of India ? :")
        self.hm = input("Who is the Home Minister of India ? : ")
    
    # creating a method for displaying
    def displayData(self):
        print("The Prime Minister of India is : ",self.pm)
        print("The President of India is : ",self.pres)
        print("The Home Minister of India is : ",self.hm)

# creating a object 

gov = Government()

# calling the methods
gov.inputData()
gov.displayData()