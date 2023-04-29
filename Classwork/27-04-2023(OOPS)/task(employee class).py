# creating a class

class Employee:
    Emp_id : int
    Emp_name : str
    Emp_dep : str
    Emp_sal : float

# creating  method for data input

    def inputData(self):
        self.Emp_id = input("Enter Employee ID : ")
        self.Emp_name = input("Enter Employee Name : ")
        self.Emp_dep = input("Enter Employee Department : ")
        self.Emp_sal = input("Enter Employee Salary : ")

# creating method for data display

    def displayData(self):
        print("Employee ID : ",self.Emp_id)
        print("Employee Name : ",self.Emp_name)
        print("Employee Department : ",self.Emp_dep)
        print("Employee Salary : ",self.Emp_sal)

# creating object

emp= Employee()

# calling methods

emp.inputData()
emp.displayData()
