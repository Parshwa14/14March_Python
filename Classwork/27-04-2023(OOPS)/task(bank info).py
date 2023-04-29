# creating a class bank
class Bank:
    b_name = str
    b_acc = int
    b_bal = float

    #creating a method for adding the data
    def addData(self):
        self.b_name = input("Enter Bank Name : ")
        self.b_acc = input("Enter Your Account Number :")
        self.b_bal = input("Enter Your Account Balance : ")
    

    # method for displaying the data

    def showData(self):
        print("Bank Name : ",self.b_name)
        print("Account Number : ",self.b_acc)
        print("Account Balance : ",self.b_bal)

    
# creting a object
bnk = Bank()

# calling the methods
bnk.addData()
bnk.showData()