class student:
    stid = 509
    stnm = "Parshwa"


    def getdata(self):
        print("Student ID : ",self.stid)
        print("Student Name : ",self.stnm)


# creating an object of class

st = student()

st.getdata()