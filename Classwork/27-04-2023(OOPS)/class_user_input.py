# creating a class
class Student:
    stid:int
    stnm:str

# creating method for getting input
    def inputData(self):
        self.stid = input("Enter Student ID : ")
        self.stnm = input("Enter Student Name : ")

# creating method for displaying 
    def displayData(self):
        print("Student ID : ",self.stid)
        print("Student Name : ",self.stnm)
    

# object creation

st = Student()

# calling the methods

st.inputData()
st.displayData()