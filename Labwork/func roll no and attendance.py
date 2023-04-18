# Define a function that accepts roll number and returns whether the student is present or absent

# first creating a dictionary with rollno as keys and attendance as values
atten = {1 : "Present", 2 : "Present", 3 : "Absent", 4 : "Present", 5 : "Present", 6 : "Absent", 7 : "Present", 8 : "Present", 9 : "Absent", 10 : "Present" }

# then asking user to enter roll no for checking the attendance
n = int(input("Enter Roll no. from 1 to 10 : "))

# creating a function to check attendance and passing a parameter of roll no in it
def checkat(rno):
    
    # using for loop and i,j to iterate all the key,value pairs from the dictionary
    for i,j in atten.items():

        # putting a condition for getting the value from the given key by the user
        if rno == i:

            # printing the final answer/output
            print(f"Roll No. : {i}\nAttendance : {j}")

# calling the function with variable n as an argument which is asked to the user to enter
checkat(n)
